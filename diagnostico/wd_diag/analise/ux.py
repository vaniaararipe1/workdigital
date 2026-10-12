"""Experiência do usuário e conversão: heurísticas verificáveis no HTML renderizado.

Entradas são os dicionários `medidas` produzidos por coleta/medir.js.
Itens que dependem de julgamento (prova social, proposta de valor) saem como
tipo "avaliacao" e não entram na nota.
"""
from __future__ import annotations

import re

from ..modelos import ESFORCO_RAPIDO, Achado
from .comum import caminho, code, esc, num, pct, plural

GENERICOS = re.compile(r"^(bem[- ]?vindo|bem[- ]?vinda|seja bem[- ]?vindo|home|in[íi]cio|p[áa]gina inicial|welcome|"
                       r"sobre( n[óo]s)?|ol[áa]|quem somos|nossa empresa|menu)\b", re.I)


def _nao_medido(id_, titulo, motivo, peso) -> Achado:
    return Achado(id_, "ux", titulo, "nao_medido", "na", f"Não foi possível medir: {motivo}.", peso=peso, confianca="baixa")


def _descr_ctas(ctas: list) -> str:
    return ", ".join(f"{code(c['texto'] or c['href'], 40)} a {c['topo']} px do topo" for c in ctas[:3])


def cta_dobra(medidas: dict | None, dispositivo: str) -> Achado:
    id_ = f"ux-cta-{dispositivo}"
    nome = "celular" if dispositivo == "mobile" else "computador"
    peso = 3 if dispositivo == "mobile" else 2
    titulo = f"Chamada para ação na primeira tela ({nome})"
    if not medidas:
        return _nao_medido(id_, titulo, f"a página não abriu na simulação de {nome}", peso)
    altura = medidas["viewport"]["altura"]
    fortes = medidas.get("ctas_fortes_dobra") or []
    dobra = medidas.get("ctas_dobra") or []
    primeiro = medidas.get("primeiro_cta")
    if fortes:
        return Achado(id_, "ux", titulo, "medido", "ok",
                      f"Há um botão de ação visível sem precisar rolar a página no {nome}.",
                      evidencia=f"{_descr_ctas(fortes)}; a tela tem {altura} px de altura.",
                      significado="O visitante recebe um convite claro para dar o próximo passo.", peso=peso, area="Conversão")
    if dobra:
        return Achado(id_, "ux", titulo, "medido", "atencao",
                      f"Na primeira tela do {nome} há elementos clicáveis, mas nenhum botão com um convite claro de ação (como \"Fale conosco\" ou \"Peça um orçamento\").",
                      evidencia=f"encontrados: {_descr_ctas(dobra)}.",
                      significado="Sem um convite explícito, o visitante precisa descobrir sozinho como contratar ou comprar.",
                      correcao="Usar um botão com verbo de ação e destaque visual logo abaixo do título principal.",
                      impacto="menos visitantes dão o primeiro passo de contato.",
                      prioridade="alta" if dispositivo == "mobile" else "media", esforco=ESFORCO_RAPIDO, peso=peso, area="Conversão")
    ev = (f"primeiro botão de ação ({code(primeiro['texto'] or primeiro['href'], 40)}) a {primeiro['topo']} px do topo; "
          f"a tela tem {altura} px de altura." if primeiro else "nenhum botão de ação encontrado na página inicial.")
    return Achado(id_, "ux", titulo, "medido", "problema",
                  f"No {nome}, nenhum botão de ação aparece antes de rolar a página.", evidencia=ev,
                  significado="O visitante não recebe um convite claro para agir na primeira impressão.",
                  correcao="Colocar um botão de destaque (por exemplo, \"Falar no WhatsApp\" ou \"Pedir orçamento\") logo abaixo do título.",
                  impacto="quem chega com intenção de compra precisa procurar como falar com você, e parte desiste.",
                  prioridade="alta" if dispositivo == "mobile" else "media", esforco=ESFORCO_RAPIDO, peso=peso, area="Conversão")


def contato_direto(home_mobile: dict | None, paginas: list[dict]) -> Achado:
    titulo = "WhatsApp ou telefone clicável"
    todas = [(p["url"], c) for p in paginas if p.get("medidas") for c in p["medidas"].get("contato_direto", [])]
    if not paginas or not any(p.get("medidas") for p in paginas):
        return _nao_medido("ux-contato", titulo, "as páginas não puderam ser abertas", 3)
    tipos = sorted({c["tipo"] for _, c in todas})
    home = (home_mobile or {}).get("contato_direto", []) if home_mobile else []
    home_vis = [c for c in home if c["visivel"]]
    altura = (home_mobile or {}).get("viewport", {}).get("altura", 0)
    na_dobra = [c for c in home_vis if c["fixo"] or (c["topo"] is not None and c["topo"] < altura)]
    n_pag = len([p for p in paginas if p.get("medidas")])
    if home_vis:
        nomes = " e ".join("WhatsApp" if t == "whatsapp" else "telefone" for t in sorted({c["tipo"] for c in home_vis}))
        extra = " Fica visível já na primeira tela." if na_dobra else " Porém não aparece na primeira tela: é preciso rolar a página."
        return Achado("ux-contato", "ux", titulo, "medido", "ok" if na_dobra else "atencao",
                      f"A página inicial no celular tem link clicável de {nomes}.{extra}",
                      evidencia=f"links {', '.join(code(c['href'], 50) for c in home_vis[:2])}" + (" (botão fixo na tela)" if any(c['fixo'] for c in home_vis) else ""),
                      significado="Um toque abre a conversa, sem precisar copiar número.",
                      correcao="" if na_dobra else "Adicionar um botão de WhatsApp fixo no canto da tela do celular.",
                      prioridade="" if na_dobra else "media", esforco="" if na_dobra else ESFORCO_RAPIDO,
                      impacto="" if na_dobra else "o caminho mais curto até o contato fica escondido para quem não rola a página.",
                      peso=3, area="Conversão")
    if todas:
        onde = sorted({caminho(u) for u, _ in todas})
        return Achado("ux-contato", "ux", titulo, "medido", "atencao",
                      "Há link clicável de contato no site, mas não na página inicial do celular.",
                      evidencia=f"encontrado em {', '.join(code(o, 40) for o in onde[:3])}.",
                      significado="A página inicial é a mais visitada; o contato direto deveria estar nela.",
                      correcao="Adicionar botão de WhatsApp clicável na página inicial, de preferência fixo no canto da tela.",
                      impacto="quem está no celular precisa navegar por outras páginas para encontrar como falar com você.",
                      prioridade="alta", esforco=ESFORCO_RAPIDO, peso=3, area="Conversão")
    return Achado("ux-contato", "ux", titulo, "medido", "problema",
                  "Não encontramos link de WhatsApp nem telefone clicável.",
                  evidencia=f"nenhum link {code('wa.me')}, {code('api.whatsapp.com')} ou {code('tel:')} nas {n_pag} páginas analisadas.",
                  significado="Para quem está no celular, falar com você exige copiar e colar o número.",
                  correcao="Transformar o número em link de WhatsApp e adicionar um botão fixo no canto da tela.",
                  impacto="cada passo extra até a conversa reduz o número de pedidos de contato.",
                  prioridade="alta", esforco=ESFORCO_RAPIDO, peso=3, area="Conversão",
                  nota_interna=f"Tipos encontrados no site: {tipos or 'nenhum'}. Confirme manualmente se há widget de chat que use outro formato de link.")


def formulario(paginas: list[dict], tem_contato_direto: bool) -> Achado:
    titulo = "Formulário de contato"
    abertas = [p for p in paginas if p.get("medidas")]
    if not abertas:
        return _nao_medido("ux-form", titulo, "as páginas não puderam ser abertas", 2)
    forms = [(p["url"], f) for p in abertas for f in p["medidas"].get("formularios", [])]
    contato = [(u, f) for u, f in forms if f["campos"] >= 2]
    externos = [(p["url"], s) for p in abertas for s in p["medidas"].get("formularios_externos", [])]
    if not contato and externos:
        u, src = externos[0]
        return Achado("ux-form", "ux", titulo, "medido", "ok",
                      "Há um formulário de contato de serviço externo incorporado ao site.",
                      evidencia=f"página {code(caminho(u), 40)}: {code(src, 80)}.",
                      significado="O visitante tem uma forma de escrever para a empresa. Os campos não puderam ser medidos porque o formulário vem de outro serviço.",
                      peso=2, area="Conversão", confianca="baixa",
                      nota_interna="Formulário em iframe: abra a página e confira quantidade de campos e rótulos.")
    if not contato:
        return Achado("ux-form", "ux", titulo, "medido", "atencao" if tem_contato_direto else "problema",
                      f"Não encontramos formulário de contato nas {len(abertas)} páginas analisadas.",
                      significado=("Parte dos clientes prefere escrever a ligar ou chamar no WhatsApp, principalmente fora do horário comercial."),
                      correcao="Incluir um formulário curto (nome, contato e mensagem) na página de contato.",
                      prioridade="baixa" if tem_contato_direto else "media", esforco=ESFORCO_RAPIDO, peso=2, area="Conversão",
                      impacto="" if tem_contato_direto else "quem não quer ligar não tem outra forma simples de pedir contato.",
                      nota_interna="Formulários que só aparecem depois de um clique (pop-up) não são detectados, porque a ferramenta não clica em nada. Confira o botão de contato do site.")
    url, f = max(contato, key=lambda x: x[1]["campos"])
    sem_rotulo = f["campos"] - f["com_rotulo"]
    ev = f"página {code(caminho(url), 40)}: {plural(f['campos'], 'campo')}, {f['com_rotulo']} com rótulo identificável."
    if f["campos"] > 9:
        return Achado("ux-form", "ux", titulo, "medido", "problema",
                      f"O formulário principal tem {f['campos']} campos.", evidencia=ev,
                      significado="Formulários longos desanimam. Cada campo extra é um motivo para desistir.",
                      correcao="Reduzir para o essencial (nome, contato e mensagem) e pedir o resto depois, na conversa.",
                      impacto="menos pedidos de contato chegam até você.",
                      prioridade="media", esforco=ESFORCO_RAPIDO, peso=2, area="Conversão")
    if f["campos"] > 6 or sem_rotulo > 0:
        motivo = []
        if f["campos"] > 6:
            motivo.append(f"tem {f['campos']} campos")
        if sem_rotulo > 0:
            motivo.append(f"{plural(sem_rotulo, 'campo')} sem rótulo (só com texto de exemplo dentro do campo, que some ao digitar)")
        return Achado("ux-form", "ux", titulo, "medido", "atencao", "O formulário principal " + " e ".join(motivo) + ".",
                      evidencia=ev,
                      significado="Rótulos claros e poucos campos facilitam o preenchimento, inclusive para leitores de tela.",
                      correcao="Manter até 6 campos e colocar um rótulo visível acima de cada um.",
                      prioridade="baixa", esforco=ESFORCO_RAPIDO, peso=2, area="Conversão")
    return Achado("ux-form", "ux", titulo, "medido", "ok",
                  f"Formulário com {plural(f['campos'], 'campo')}, todos com rótulo.", evidencia=ev,
                  significado="Curto e claro. Bom para quem prefere escrever.", peso=2, area="Conversão")


def viewport(medidas: dict | None) -> Achado:
    titulo = "Site adaptado ao celular"
    if not medidas:
        return _nao_medido("ux-viewport", titulo, "a página não abriu na simulação de celular", 2)
    meta = medidas.get("meta_viewport") or ""
    largura = medidas["viewport"]["largura"]
    doc = medidas.get("largura_documento", largura)
    if "width=device-width" not in meta.replace(" ", ""):
        return Achado("ux-viewport", "ux", titulo, "medido", "problema",
                      "A página não declara que deve se ajustar à largura do celular.",
                      evidencia=f"meta viewport: {code(meta or 'ausente')}.",
                      significado="O celular mostra a versão de computador em miniatura, e o visitante precisa dar zoom.",
                      correcao="Adicionar a configuração de viewport e revisar o layout responsivo.",
                      impacto="a maior parte das visitas vem do celular, e a experiência fica ruim para elas.",
                      prioridade="alta", esforco="médio (dias)", peso=2, area="Experiência")
    if doc > largura + 10:
        return Achado("ux-viewport", "ux", titulo, "medido", "atencao",
                      "O site se ajusta ao celular, mas parte do conteúdo fica mais larga que a tela.",
                      evidencia=f"largura do conteúdo {doc} px em tela de {largura} px.",
                      significado="O visitante consegue arrastar a página para os lados, o que parece erro.",
                      correcao="Encontrar o elemento que ultrapassa a largura e ajustá-lo.",
                      prioridade="media", esforco=ESFORCO_RAPIDO, peso=2, area="Experiência")
    return Achado("ux-viewport", "ux", titulo, "medido", "ok", "A página se ajusta à largura do celular, sem rolagem lateral.",
                  evidencia=f"meta viewport {code(meta)}; conteúdo com {doc} px em tela de {largura} px.", peso=2, area="Experiência")


def alvos_toque(medidas: dict | None) -> Achado:
    titulo = "Botões e links fáceis de tocar"
    if not medidas or not medidas.get("alvos_total"):
        return _nao_medido("ux-toque", titulo, "não havia elementos clicáveis medíveis no celular", 1)
    total, peq = medidas["alvos_total"], medidas["alvos_pequenos_total"]
    p = pct(peq, total)
    ev = f"{peq} de {total} elementos clicáveis com menos de {code('24×24 px')}"
    exemplos = [a["texto"] for a in medidas.get("alvos_pequenos", []) if a["texto"]][:3]
    if exemplos:
        ev += ", por exemplo " + ", ".join(code(e, 30) for e in exemplos)
    situacao = "ok" if p <= 10 else ("atencao" if p <= 30 else "problema")
    return Achado("ux-toque", "ux", titulo, "medido", situacao,
                  f"{p}% dos botões e links da página inicial são pequenos demais para tocar com o dedo." if peq else
                  "Os botões e links têm tamanho adequado para o toque.",
                  evidencia=ev + ".",
                  significado="Alvos pequenos causam toques errados, principalmente para pessoas com mais idade." if situacao != "ok" else "",
                  correcao="Aumentar a área de toque de ícones e links para pelo menos 44 px." if situacao != "ok" else "",
                  prioridade="baixa" if situacao == "atencao" else ("media" if situacao == "problema" else ""),
                  esforco=ESFORCO_RAPIDO if situacao != "ok" else "", peso=1, area="Experiência")


def legibilidade(medidas: dict | None) -> Achado:
    titulo = "Leitura confortável no celular"
    if not medidas or not medidas.get("texto_total_chars"):
        return _nao_medido("ux-leitura", titulo, "não havia texto medível na página inicial", 1)
    p = pct(medidas["texto_pequeno_chars"], medidas["texto_total_chars"])
    situacao = "ok" if p <= 10 else ("atencao" if p <= 40 else "problema")
    return Achado("ux-leitura", "ux", titulo, "medido", situacao,
                  f"{p}% do texto da página inicial no celular está com letra menor que 12 px.",
                  evidencia=f"{num(medidas['texto_pequeno_chars'], 0)} de {num(medidas['texto_total_chars'], 0)} caracteres visíveis abaixo de {code('12px')}.",
                  significado=("Texto pequeno obriga o visitante a dar zoom ou desistir de ler." if situacao != "ok"
                               else "O tamanho do texto é confortável para leitura no celular."),
                  correcao="Usar fonte de pelo menos 16 px no texto corrido do celular." if situacao != "ok" else "",
                  prioridade="media" if situacao == "problema" else ("baixa" if situacao == "atencao" else ""),
                  esforco=ESFORCO_RAPIDO if situacao != "ok" else "", peso=1, area="Experiência")


def prova_social(paginas: list[dict]) -> Achado:
    titulo = "Prova social visível"
    abertas = [p for p in paginas if p.get("medidas")]
    if not abertas:
        return _nao_medido("ux-social", titulo, "as páginas não puderam ser abertas", 0)
    sinais = [(p["url"], s) for p in abertas for s in p["medidas"].get("sinais_prova_social", [])]
    widgets = sum(p["medidas"].get("widgets_prova_social", 0) for p in abertas)
    if sinais or widgets:
        ev = "; ".join(f"{code(caminho(u), 30)}: “{esc(s[:90])}”" for u, s in sinais[:2])
        if widgets:
            ev += (" · " if ev else "") + f"{plural(widgets, 'bloco visual', 'blocos visuais')} de depoimentos ou avaliações"
        return Achado("ux-social", "ux", titulo, "avaliacao", "ok",
                      "Encontramos sinais de prova social, como depoimentos, avaliações ou clientes atendidos.",
                      evidencia=ev,
                      significado="Mostrar quem já confia na empresa ajuda o visitante a decidir. Vale conferir se esses elementos aparecem logo na página inicial.",
                      peso=0, area="Conversão",
                      nota_interna="Sinal detectado por palavras-chave. Confira se é prova social de fato (e não só a palavra 'clientes' num menu).")
    return Achado("ux-social", "ux", titulo, "avaliacao", "atencao",
                  f"Não encontramos depoimentos, avaliações ou clientes em destaque nas {len(abertas)} páginas analisadas.",
                  significado="Avaliações de clientes reduzem a insegurança de quem ainda não conhece a empresa.",
                  correcao="Incluir 3 depoimentos curtos, a nota do Google ou logos de clientes na página inicial.",
                  prioridade="media", esforco=ESFORCO_RAPIDO, peso=0, area="Conversão",
                  nota_interna="Busca por palavras-chave; pode haver prova social em imagem (sem texto). Confira visualmente a captura.")


def proposta_valor(home: dict | None) -> Achado:
    titulo = "Clareza da proposta de valor no título principal"
    if not home:
        return _nao_medido("ux-proposta", titulo, "a página inicial não abriu", 0)
    h1s = [h for h in home.get("h1s", []) if h["texto"]]
    principal = (h1s[0]["texto"] if h1s else (home.get("primeiro_titulo") or {}).get("texto", "")).strip()
    if not principal:
        return Achado("ux-proposta", "ux", titulo, "avaliacao", "atencao",
                      "A página inicial não tem um título principal em texto.",
                      significado="Se o título está só dentro de uma imagem, o Google e quem usa leitor de tela não o leem, e a mensagem pode passar despercebida.",
                      correcao="Escrever um título em texto que diga o que a empresa faz e para quem.",
                      prioridade="media", esforco=ESFORCO_RAPIDO, peso=0, area="Conversão",
                      nota_interna="Verifique na captura se o título está numa imagem ou slider.")
    if GENERICOS.search(principal) or len(principal.split()) <= 2:
        return Achado("ux-proposta", "ux", titulo, "avaliacao", "atencao",
                      f"O título principal é “{principal[:120]}”.",
                      significado="O título não diz o que a empresa oferece nem para quem. Vale um título que responda: o que vocês fazem e por que escolher vocês.",
                      correcao="Reescrever o título principal com o serviço, o público e o diferencial.",
                      prioridade="media", esforco=ESFORCO_RAPIDO, peso=0, area="Conversão",
                      nota_interna="Título curto ou genérico pela regra automática. Sugira uma versão na conversa.")
    return Achado("ux-proposta", "ux", titulo, "avaliacao", "ok",
                  f"O título principal é “{principal[:160]}”.",
                  significado="Parece descrever a oferta. Vale confirmar se deixa claro para quem é e qual o diferencial.",
                  peso=0, area="Conversão",
                  nota_interna="Leia o título e decida se a proposta de valor está clara. Ajuste o texto do relatório se discordar.")


def analisar(home_mobile: dict | None, home_desktop: dict | None, paginas: list[dict]) -> list[Achado]:
    m = (home_mobile or {}).get("medidas")
    d = (home_desktop or {}).get("medidas")
    contato = contato_direto(m, paginas)
    return [
        cta_dobra(m, "mobile"),
        cta_dobra(d, "desktop"),
        contato,
        formulario(paginas, contato.situacao in ("ok", "atencao")),
        viewport(m),
        alvos_toque(m),
        legibilidade(m),
        prova_social(paginas),
        proposta_valor(d or m),
    ]
