"""SEO básico e preparo para busca com IA (AEO/GEO)."""
from __future__ import annotations

import json
import re
from collections import Counter
from urllib.parse import urljoin, urlsplit

from bs4 import BeautifulSoup

from ..modelos import ESFORCO_MEDIO, ESFORCO_RAPIDO, Achado
from ..rastreador import mesmo_site
from .comum import caminho, code, lista_curta, pct, plural

TIPOS_ORGANIZACAO = {
    "organization", "localbusiness", "corporation", "professionalservice", "store", "restaurant", "foodestablishment",
    "medicalbusiness", "medicalclinic", "dentist", "legalservice", "attorney", "homeandconstructionbusiness",
    "automotivebusiness", "healthandbeautybusiness", "beautysalon", "dayspa", "sportsactivitylocation",
    "educationalorganization", "lodgingbusiness", "hotel", "financialservice", "realestateagent",
    "travelagency", "ngo", "onlinestore", "clothingstore", "bakery", "cafeorcoffeeshop", "physician",
}


# ---------------- extração por página (função pura) ----------------

def _tipos_jsonld(dados) -> list[str]:
    tipos = []
    if isinstance(dados, list):
        for d in dados:
            tipos += _tipos_jsonld(d)
    elif isinstance(dados, dict):
        t = dados.get("@type")
        if isinstance(t, str):
            tipos.append(t)
        elif isinstance(t, list):
            tipos += [x for x in t if isinstance(x, str)]
        for chave in ("@graph", "mainEntity", "publisher", "author", "provider"):
            if chave in dados:
                tipos += _tipos_jsonld(dados[chave])
    return tipos


def extrair_pagina(url: str, html: str) -> dict:
    sopa = BeautifulSoup(html or "", "html.parser")
    titulo = sopa.title.get_text(" ", strip=True) if sopa.title else None
    desc_tag = sopa.find("meta", attrs={"name": re.compile("^description$", re.I)})
    desc = (desc_tag.get("content") or "").strip() if desc_tag else None
    robots_tag = sopa.find("meta", attrs={"name": re.compile("^robots$", re.I)})
    canon = sopa.find("link", rel=lambda v: v and "canonical" in [x.lower() for x in (v if isinstance(v, list) else [v])])
    headings = [(int(h.name[1]), h.get_text(" ", strip=True)) for h in sopa.find_all(re.compile("^h[1-6]$"))]
    saltos = [f"h{a}→h{b}" for (a, _), (b, _) in zip(headings, headings[1:]) if b > a + 1]

    imgs = [i for i in sopa.find_all("img")
            if not i.find_parent("noscript") and not (i.get("width") in ("0", "1") and i.get("height") in ("0", "1"))]
    sem_alt = [i.get("src") or i.get("data-src") or "(sem endereço)" for i in imgs if not i.has_attr("alt")]

    tipos = []
    jsonld_invalido = 0
    for s in sopa.find_all("script", type=re.compile("ld\\+json", re.I)):
        try:
            tipos += _tipos_jsonld(json.loads(s.string or s.get_text() or ""))
        except (ValueError, TypeError):
            jsonld_invalido += 1
    tipos += [str(t.get("itemtype", "")).rstrip("/").split("/")[-1] for t in sopa.find_all(attrs={"itemtype": True})]
    tipos = [t for t in tipos if t]

    links = []
    for a in sopa.find_all("a", href=True):
        href = a["href"].strip()
        if href.startswith(("#", "mailto:", "tel:", "javascript:", "whatsapp:", "data:")):
            continue
        absoluto = urljoin(url, href).split("#")[0]
        if absoluto.startswith(("http://", "https://")) and mesmo_site(absoluto, url):
            links.append(absoluto)

    perguntas = [t for n, t in headings if n >= 2 and t.strip().endswith("?")]
    return {
        "url": url,
        "titulo": titulo,
        "descricao": desc,
        "meta_robots": (robots_tag.get("content") or "").lower() if robots_tag else "",
        "canonical": urljoin(url, canon.get("href")) if canon and canon.get("href") else None,
        "h1": [t for n, t in headings if n == 1],
        "saltos_hierarquia": saltos,
        "imagens": len(imgs),
        "imagens_sem_alt": sem_alt,
        "schema_tipos": sorted(set(tipos)),
        "jsonld_invalido": jsonld_invalido,
        "links_internos": sorted(set(links)),
        "perguntas_em_titulos": perguntas,
    }


# ---------------- critérios ----------------

def _v(n: int, singular: str, plural_: str) -> str:
    return singular if n == 1 else plural_


def _cap(t: str) -> str:
    return t[:1].upper() + t[1:]


def _a(id_, titulo, situacao, o_que_vimos, peso, *, evidencia="", significado="", correcao="", prioridade="",
       esforco="", impacto="", area="SEO", tipo="medido", nota_interna="") -> Achado:
    if situacao == "ok":
        prioridade, esforco, correcao, impacto = "", "", "", ""
    return Achado(id_, "seo", titulo, tipo, situacao, o_que_vimos, evidencia=evidencia, significado=significado,
                  correcao=correcao, prioridade=prioridade, esforco=esforco, impacto=impacto, peso=peso, area=area,
                  nota_interna=nota_interna)


def titulos(pags: list[dict]) -> list[Achado]:
    out = []
    sem = [p for p in pags if not p["titulo"]]
    fora = [p for p in pags if p["titulo"] and not (10 <= len(p["titulo"]) <= 65)]
    if sem:
        sit, vimos = "problema", f"{plural(len(sem), 'página')} sem título."
    elif fora:
        sit = "atencao"
        vimos = f"{plural(len(fora), 'página')} com título curto ou longo demais para o Google."
    else:
        sit, vimos = "ok", f"Todas as {len(pags)} páginas analisadas têm título com tamanho adequado."
    ev = "; ".join(f"{code(caminho(p['url']), 30)}: {code(p['titulo'] or '(vazio)', 70)} ({len(p['titulo'] or '')} caracteres)" for p in (sem + fora or pags)[:3])
    out.append(_a("seo-title", "Título das páginas no Google", sit, vimos, 2, evidencia=ev,
                  significado="O título é o texto azul que aparece no Google. Ele precisa dizer o que a página oferece em até cerca de 60 caracteres.",
                  correcao="Escrever um título para cada página com o serviço principal e, se fizer sentido, a cidade.",
                  prioridade="media" if sit == "problema" else "baixa", esforco=ESFORCO_RAPIDO,
                  impacto="o Google mostra um texto pouco atrativo e você perde cliques para concorrentes."))

    cont = Counter(p["titulo"].strip().lower() for p in pags if p["titulo"])
    dup = {t: n for t, n in cont.items() if n > 1}
    if len(pags) < 2:
        out.append(Achado("seo-title-dup", "seo", "Títulos repetidos entre páginas", "nao_medido", "na",
                          "Não foi possível medir: só uma página pôde ser analisada.", peso=1.5, confianca="baixa"))
    elif dup:
        t, n = max(dup.items(), key=lambda x: x[1])
        paginas_dup = [caminho(p["url"]) for p in pags if p["titulo"] and p["titulo"].strip().lower() == t]
        out.append(_a("seo-title-dup", "Títulos repetidos entre páginas", "problema",
                      f"{n} páginas usam exatamente o mesmo título.", 1.5,
                      evidencia=f"{code(t, 70)} em {lista_curta(paginas_dup)}.",
                      significado="Com títulos iguais, o Google tem dificuldade de saber qual página mostrar para cada busca.",
                      correcao="Dar um título próprio a cada página, descrevendo o conteúdo dela.",
                      prioridade="media", esforco=ESFORCO_RAPIDO,
                      impacto="o Google tem dificuldade de mostrar a página certa para quem busca um serviço específico."))
    else:
        out.append(_a("seo-title-dup", "Títulos repetidos entre páginas", "ok",
                      f"Cada uma das {len(pags)} páginas tem um título diferente.", 1.5))
    return out


def descricoes(pags: list[dict]) -> Achado:
    sem = [p for p in pags if not p["descricao"]]
    fora = [p for p in pags if p["descricao"] and not (50 <= len(p["descricao"]) <= 160)]
    cont = Counter(p["descricao"].strip().lower() for p in pags if p["descricao"])
    dup = sum(n for n in cont.values() if n > 1)
    if sem:
        sit = "problema" if len(sem) == len(pags) else "atencao"
        vimos = f"{len(sem)} de {len(pags)} páginas não têm descrição."
    elif fora or dup:
        sit = "atencao"
        partes = []
        if fora:
            partes.append(f"{plural(len(fora), 'página')} com descrição fora do tamanho ideal (50 a 160 caracteres)")
        if dup:
            partes.append(f"{dup} páginas com a mesma descrição")
        vimos = _cap("; ".join(partes)) + "."
    else:
        sit, vimos = "ok", "Todas as páginas analisadas têm descrição própria e de tamanho adequado."
    return _a("seo-desc", "Descrição das páginas (meta description)", sit, vimos, 1.5,
              evidencia=("sem descrição: " + lista_curta(caminho(p["url"]) for p in sem) + ".") if sem else "",
              significado="É o texto que costuma aparecer abaixo do título no Google. Sem ela, o Google escolhe um trecho qualquer da página.",
              correcao="Escrever uma frase de até 155 caracteres para cada página, com um convite para clicar.",
              prioridade="baixa", esforco=ESFORCO_RAPIDO)


def h1(pags: list[dict]) -> Achado:
    home = pags[0]
    sem = [p for p in pags if len(p["h1"]) == 0]
    varios = [p for p in pags if len(p["h1"]) > 1]
    if not home["h1"]:
        sit = "problema"
    elif sem or varios:
        sit = "atencao"
    else:
        sit = "ok"
    partes = []
    if sem:
        partes.append(f"{plural(len(sem), 'página')} sem título principal (H1)")
    if varios:
        partes.append(f"{plural(len(varios), 'página')} com mais de um H1")
    vimos = (_cap("; ".join(partes)) + ".") if partes else f"Todas as {len(pags)} páginas têm exatamente um título principal (H1)."
    ev = "; ".join(f"{code(caminho(p['url']), 30)}: {len(p['h1'])} H1" for p in (sem + varios)[:4])
    return _a("seo-h1", "Título principal único em cada página (H1)", sit, vimos, 1.5, evidencia=ev,
              significado="O H1 é o título de destaque dentro da página. O Google usa esse título para entender o assunto principal.",
              correcao="Garantir um único H1 por página, com o tema principal dela.",
              prioridade="media" if sit == "problema" else "baixa", esforco=ESFORCO_RAPIDO)


def hierarquia(pags: list[dict]) -> Achado:
    com = [p for p in pags if p["saltos_hierarquia"]]
    sit = "ok" if not com else "atencao"
    vimos = ("Os títulos e subtítulos seguem uma ordem lógica." if not com else
             f"{plural(len(com), 'página')} {_v(len(com), 'pula', 'pulam')} níveis de subtítulo (por exemplo, de H2 direto para H4).")
    ev = "; ".join(f"{code(caminho(p['url']), 30)}: {', '.join(p['saltos_hierarquia'][:3])}" for p in com[:3])
    return _a("seo-hierarquia", "Hierarquia de títulos", sit, vimos, 0.5, evidencia=ev,
              significado="Uma estrutura de títulos organizada ajuda o Google, as IAs e leitores de tela a entender o conteúdo.",
              correcao="Ajustar os níveis de título para seguir a ordem H1, H2, H3.", prioridade="baixa", esforco=ESFORCO_RAPIDO)


def canonical(pags: list[dict]) -> Achado:
    sem = [p for p in pags if not p["canonical"]]
    externo = [p for p in pags if p["canonical"] and not mesmo_site(p["canonical"], p["url"])]
    if externo:
        sit, vimos = "problema", f"{plural(len(externo), 'página')} {_v(len(externo), 'indica', 'indicam')} como endereço oficial uma URL de outro domínio."
    elif sem:
        sit, vimos = "atencao", f"{len(sem)} de {len(pags)} páginas não indicam o endereço oficial (canonical)."
    else:
        sit, vimos = "ok", "Todas as páginas indicam o próprio endereço oficial (canonical)."
    ev = "; ".join(f"{code(caminho(p['url']), 30)} → {code(p['canonical'], 60)}" for p in externo[:2]) if externo else ""
    return _a("seo-canonical", "Endereço oficial das páginas (canonical)", sit, vimos, 1, evidencia=ev,
              significado="A marcação canonical evita que o Google veja versões repetidas da mesma página como conteúdo duplicado.",
              correcao="Adicionar a tag canonical em todas as páginas apontando para o próprio endereço.",
              prioridade="media" if sit == "problema" else "baixa", esforco=ESFORCO_RAPIDO)


def indexacao(pags: list[dict]) -> Achado:
    bloqueadas = [p for p in pags if "noindex" in p["meta_robots"]]
    if not bloqueadas:
        return _a("seo-noindex", "Páginas liberadas para o Google", "ok",
                  "Nenhuma página analisada pede ao Google para não aparecer nas buscas.", 3)
    home = pags[0] in bloqueadas
    return _a("seo-noindex", "Páginas liberadas para o Google", "problema",
              f"{plural(len(bloqueadas), 'página')} {_v(len(bloqueadas), 'pede', 'pedem')} ao Google para não aparecer nas buscas" + (", incluindo a página inicial." if home else "."),
              3, evidencia=f"{code('noindex')} em {lista_curta(caminho(p['url']) for p in bloqueadas)}.",
              significado="Essas páginas não aparecem no Google, mesmo que tenham bom conteúdo.",
              correcao="Remover a instrução noindex das páginas que devem ser encontradas.",
              prioridade="alta", esforco=ESFORCO_RAPIDO,
              impacto="o site fica invisível no Google para essas páginas." if not home else "o site inteiro pode ficar fora do Google.")


def robots(dados: dict) -> Achado:
    if dados.get("erro") and not dados.get("status"):
        return Achado("seo-robots", "seo", "Arquivo de instruções para buscadores (robots.txt)", "nao_medido", "na",
                      f"Não foi possível medir: {dados['erro']}.", peso=1, confianca="baixa")
    if dados.get("bloqueia_buscadores"):
        return _a("seo-robots", "Arquivo de instruções para buscadores (robots.txt)", "problema",
                  "O robots.txt impede o Google de acessar a página inicial.", 1,
                  evidencia=f"{code(dados['url'])}.", significado="O Google pode deixar de mostrar o site nas buscas.",
                  correcao="Revisar as regras do robots.txt.", prioridade="alta", esforco=ESFORCO_RAPIDO,
                  impacto="o site pode sumir das buscas do Google.")
    if dados.get("existe"):
        return _a("seo-robots", "Arquivo de instruções para buscadores (robots.txt)", "ok",
                  "O arquivo robots.txt existe e permite o acesso dos buscadores.", 1, evidencia=f"{code(dados['url'])}.")
    return _a("seo-robots", "Arquivo de instruções para buscadores (robots.txt)", "atencao",
              "O site não tem arquivo robots.txt.", 1, evidencia=f"{code(dados['url'])} respondeu {dados.get('status')}.",
              significado="Não impede o Google de ler o site, mas é o lugar padrão para indicar o mapa do site.",
              correcao="Criar um robots.txt simples apontando para o sitemap.", prioridade="baixa", esforco=ESFORCO_RAPIDO)


def sitemap(dados: dict) -> Achado:
    if dados.get("existe"):
        return _a("seo-sitemap", "Mapa do site (sitemap.xml)", "ok",
                  f"O mapa do site existe e lista {plural(dados['total_urls'], 'endereço')}.", 1, evidencia=f"{code(dados['url'])}.",
                  significado="Ajuda o Google a encontrar todas as páginas.")
    return _a("seo-sitemap", "Mapa do site (sitemap.xml)", "atencao",
              "Não encontramos mapa do site nos endereços padrão.", 1,
              evidencia="tentativas: " + lista_curta(dados.get("tentativas", [dados.get("url")]), 3) + ".",
              significado="Sem o mapa, o Google pode demorar mais para descobrir páginas novas.",
              correcao="Gerar um sitemap.xml e informá-lo no Google Search Console.", prioridade="baixa", esforco=ESFORCO_RAPIDO)


def https(url_final: str, dados: dict) -> Achado:
    seguro = url_final.startswith("https://")
    if not seguro:
        return _a("seo-https", "Endereço seguro (HTTPS)", "problema", "O site abre sem conexão segura (HTTPS).", 2,
                  evidencia=f"endereço final {code(url_final)}.",
                  significado="O navegador mostra o aviso \"Não seguro\", o que afasta visitantes e prejudica o Google.",
                  correcao="Instalar certificado SSL (gratuito na maioria das hospedagens) e redirecionar tudo para HTTPS.",
                  prioridade="alta", esforco=ESFORCO_RAPIDO,
                  impacto="o aviso de site inseguro afasta visitantes logo na chegada.")
    if dados.get("erro") and not dados.get("destino"):
        return _a("seo-https", "Endereço seguro (HTTPS)", "ok", "O site usa HTTPS.", 2,
                  evidencia=f"não foi possível testar a versão sem HTTPS ({dados['erro']}).",
                  nota_interna="Redirecionamento http→https não verificado.")
    if not dados.get("redireciona_para_https"):
        return _a("seo-https", "Endereço seguro (HTTPS)", "atencao",
                  "O site usa HTTPS, mas a versão sem HTTPS não redireciona para a segura.", 2,
                  evidencia=f"{code(dados.get('url_testada'))} termina em {code(dados.get('destino') or '?')}.",
                  significado="Quem digita o endereço sem https pode cair numa versão sem cadeado.",
                  correcao="Configurar redirecionamento permanente (301) de http para https.", prioridade="media", esforco=ESFORCO_RAPIDO)
    return _a("seo-https", "Endereço seguro (HTTPS)", "ok",
              "O site usa HTTPS e redireciona a versão sem segurança para a segura.", 2,
              evidencia=f"{code(dados.get('url_testada'))} → {code(dados.get('destino'))}.",
              significado="O navegador mostra o cadeado e não exibe alerta de site inseguro.")


def redirecionamentos(cadeia: list) -> Achado:
    n = len(cadeia)
    sit = "ok" if n <= 1 else ("atencao" if n == 2 else "problema")
    ev = " → ".join([code(cadeia[0][1], 60)] + [f"{code(d, 60)} ({s})" for s, _, d in cadeia]) if cadeia else ""
    return _a("seo-redirect", "Redirecionamentos até a página inicial", sit,
              "O endereço informado abre direto, sem redirecionamentos." if n == 0 else
              f"Até chegar à página inicial, o endereço passa por {plural(n, 'redirecionamento')}.", 0.5, evidencia=ev,
              significado="Cada redirecionamento adiciona espera antes de a página começar a carregar.",
              correcao="Apontar links e anúncios direto para o endereço final e reduzir a cadeia a um salto.",
              prioridade="baixa", esforco=ESFORCO_RAPIDO)


def urls_amigaveis(pags: list[dict]) -> Achado:
    ruins = []
    for p in pags:
        partes = urlsplit(p["url"])
        if re.search(r"(^|&)(p|page_id|id|cat)=\d+", partes.query) or re.search(r"[A-Z_]", partes.path) or len(p["url"]) > 115:
            ruins.append(p["url"])
    sit = "ok" if not ruins else "atencao"
    return _a("seo-urls", "Endereços das páginas legíveis", sit,
              "Os endereços das páginas são curtos e legíveis." if not ruins else
              f"{plural(len(ruins), 'endereço')} com números, maiúsculas ou tamanho excessivo.", 0.5,
              evidencia=lista_curta(ruins, 3) + "." if ruins else "",
              significado="Endereços legíveis (como /servicos/consultoria) ajudam o Google e passam confiança no compartilhamento.",
              correcao="Ativar endereços amigáveis e usar palavras separadas por hífen.", prioridade="baixa", esforco=ESFORCO_MEDIO)


def imagens_alt(pags: list[dict]) -> Achado:
    total = sum(p["imagens"] for p in pags)
    sem = sum(len(p["imagens_sem_alt"]) for p in pags)
    if total == 0:
        return Achado("seo-alt", "seo", "Imagens com texto alternativo", "nao_medido", "na",
                      "Não foi possível medir: não encontramos imagens nas páginas analisadas.", peso=1)
    p = pct(sem, total)
    sit = "ok" if p <= 10 else ("atencao" if p <= 30 else "problema")
    return _a("seo-alt", "Imagens com texto alternativo", sit,
              f"{sem} de {total} imagens não têm texto alternativo." if sem else f"Todas as {total} imagens têm texto alternativo.", 1,
              evidencia=("exemplos: " + lista_curta([s.split('/')[-1] or s for p_ in pags for s in p_['imagens_sem_alt']], 3) + ".") if sem else "",
              significado="O texto alternativo descreve a imagem para o Google e para pessoas com deficiência visual que usam leitores de tela.",
              correcao="Descrever brevemente cada imagem importante (produtos, equipe, trabalhos).",
              prioridade="baixa" if sit == "atencao" else "media", esforco=ESFORCO_RAPIDO)


def links_quebrados(dados: dict) -> Achado:
    if not dados or not dados.get("verificados"):
        return Achado("seo-links", "seo", "Links internos quebrados", "nao_medido", "na",
                      "Não foi possível medir: nenhum link interno pôde ser verificado.", peso=1.5, confianca="baixa")
    q = dados["quebrados"]
    sit = "ok" if not q else ("atencao" if len(q) <= 2 else "problema")
    return _a("seo-links", "Links internos quebrados", sit,
              f"Verificamos {dados['verificados']} links internos e todos funcionam." if not q else
              f"{plural(len(q), 'link interno', 'links internos')} de {dados['verificados']} verificados {_v(len(q), 'leva', 'levam')} a uma página que não existe (erro 404).", 1.5,
              evidencia=lista_curta([caminho(x["url"]) for x in q], 4) + "." if q else "",
              significado="Links quebrados frustram o visitante e desperdiçam a atenção do Google.",
              correcao="Corrigir ou remover os links listados.", prioridade="media" if sit == "problema" else "baixa",
              esforco=ESFORCO_RAPIDO, nota_interna=(f"{len(dados['falhas'])} links não responderam (timeout/erro 5xx); não contados como quebrados."
                                                    if dados.get("falhas") else ""))


def dados_estruturados(pags: list[dict]) -> list[Achado]:
    tipos = sorted({t for p in pags for t in p["schema_tipos"]})
    out = []
    if tipos:
        out.append(_a("seo-schema", "Dados estruturados (schema.org)", "ok",
                      f"O site usa dados estruturados: {', '.join(tipos[:6])}.", 1,
                      significado="Dados estruturados ajudam o Google a entender informações como empresa, endereço e produtos."))
    else:
        out.append(_a("seo-schema", "Dados estruturados (schema.org)", "problema",
                      "Não encontramos dados estruturados nas páginas analisadas.", 1,
                      significado="Sem eles, o Google e as IAs precisam adivinhar informações como endereço, horário e serviços.",
                      correcao="Adicionar dados estruturados de empresa (Organization ou LocalBusiness) e dos serviços.",
                      prioridade="media", esforco=ESFORCO_MEDIO))

    org = [t for t in tipos if t.lower() in TIPOS_ORGANIZACAO]
    faq = [t for t in tipos if t.lower() in ("faqpage", "qapage")]
    perguntas = [q for p in pags for q in p["perguntas_em_titulos"]]
    out.append(_a("geo-org", "Identificação da empresa para buscas com IA", "ok" if org else "problema",
                  f"A empresa está identificada com dados estruturados do tipo {', '.join(org)}." if org else
                  "Não há dados estruturados que identifiquem a empresa (schema.org Organization ou LocalBusiness).", 1,
                  area="SEO e IA",
                  significado="Assistentes como ChatGPT, Gemini e a busca com IA do Google usam essas informações para citar e recomendar empresas.",
                  correcao="Adicionar o bloco Organization ou LocalBusiness com nome, logo, endereço, telefone e redes sociais.",
                  prioridade="media", esforco=ESFORCO_RAPIDO))

    if faq or len(perguntas) >= 3:
        sit = "ok"
        vimos = ("Há perguntas frequentes marcadas com dados estruturados." if faq else
                 f"Encontramos {len(perguntas)} subtítulos em formato de pergunta, que respondem dúvidas diretas.")
    elif perguntas:
        sit, vimos = "atencao", f"Encontramos {plural(len(perguntas), 'subtítulo')} em formato de pergunta, mas não há seção de perguntas frequentes."
    else:
        sit, vimos = "atencao", "Não encontramos conteúdo em formato de pergunta e resposta."
    out.append(_a("geo-faq", "Conteúdo que responde perguntas diretas", sit, vimos, 0.5, area="SEO e IA",
                  evidencia=("exemplos: " + ", ".join(code(q, 60) for q in perguntas[:2]) + ".") if perguntas else "",
                  significado="Buscas com IA priorizam conteúdo que responde perguntas de forma direta, como \"quanto custa\" ou \"como funciona\".",
                  correcao="Criar uma seção de perguntas frequentes com as dúvidas reais dos clientes.",
                  prioridade="baixa", esforco=ESFORCO_RAPIDO))
    return out


def llms(dados: dict) -> Achado:
    return _a("geo-llms", "Arquivo de orientação para IAs (llms.txt)", "ok" if dados.get("existe") else "atencao",
              "O site tem arquivo llms.txt." if dados.get("existe") else "O site não tem arquivo llms.txt.", 0.25,
              area="SEO e IA", evidencia=f"{code(dados.get('url'))}.",
              significado="O llms.txt é um padrão recente que resume o site para assistentes de IA. Ainda é pouco adotado, por isso tem peso baixo.",
              correcao="Criar um llms.txt com a descrição da empresa, serviços e páginas principais.",
              prioridade="baixa", esforco=ESFORCO_RAPIDO)


def analisar(paginas_html: list[dict], robots_d: dict, sitemap_d: dict, llms_d: dict, https_d: dict,
             cadeia: list, links_d: dict, url_final: str) -> tuple[list[Achado], list[dict]]:
    pags = [extrair_pagina(p["url_final"] or p["url"], p["html"]) for p in paginas_html if p.get("html")]
    if not pags:
        falha = Achado("seo-falha", "seo", "Análise das páginas", "nao_medido", "na",
                       "Não foi possível medir: nenhuma página pôde ser aberta.", peso=0, confianca="baixa")
        return [falha, robots(robots_d), sitemap(sitemap_d), https(url_final, https_d), llms(llms_d)], []
    achados = [
        indexacao(pags), *titulos(pags), descricoes(pags), h1(pags), hierarquia(pags), canonical(pags),
        https(url_final, https_d), redirecionamentos(cadeia), robots(robots_d), sitemap(sitemap_d),
        urls_amigaveis(pags), imagens_alt(pags), links_quebrados(links_d), *dados_estruturados(pags), llms(llms_d),
    ]
    return achados, pags
