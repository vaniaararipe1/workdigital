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


def _links(paginas: list[dict], tipos: tuple) -> list[tuple[str, dict]]:
    return [(p["url"], c) for p in paginas if p.get("medidas")
            for c in p["medidas"].get("contato_direto", []) if c["tipo"] in tipos]


def whatsapp(home_mobile: dict | None, paginas: list[dict]) -> Achado:
    """Link de WhatsApp na home (celular) e nas demais páginas analisadas."""
    titulo = "Link de WhatsApp"
    abertas = [p for p in paginas if p.get("medidas")]
    if not abertas:
        return _nao_medido("ux-whatsapp", titulo, "as páginas não puderam ser abertas", 3)
    todas = _links(abertas, ("whatsapp",))
    home = [c for c in (home_mobile or {}).get("contato_direto", []) if c["tipo"] == "whatsapp" and c["visivel"]]
    altura = (home_mobile or {}).get("viewport", {}).get("altura", 0)
    na_dobra = [c for c in home if c["fixo"] or (c["topo"] is not None and c["topo"] < altura)]
    outras = sorted({caminho(u) for u, _ in todas})
    if home:
        ev = f"{code(home[0]['href'], 50)}" + (" (botão fixo na tela)" if any(c["fixo"] for c in home) else
                                               f" a {home[0]['topo']} px do topo; a tela tem {altura} px")
        ev += f"; presente em {plural(len(outras), 'página')} das {len(abertas)} analisadas."
        if na_dobra:
            return Achado("ux-whatsapp", "ux", titulo, "medido", "ok",
                          "A página inicial no celular tem link de WhatsApp visível já na primeira tela.", evidencia=ev,
                          significado="Um toque abre a conversa, sem precisar copiar o número.", peso=3, area="Conversão")
        return Achado("ux-whatsapp", "ux", titulo, "medido", "atencao",
                      "A página inicial no celular tem link de WhatsApp, mas ele só aparece depois de rolar a página.",
                      evidencia=ev, significado="O caminho mais curto até a conversa fica escondido para quem não rola a página.",
                      correcao="Adicionar um botão de WhatsApp fixo no canto da tela do celular.",
                      impacto="parte dos visitantes não encontra o jeito mais rápido de falar com você.",
                      prioridade="media", esforco=ESFORCO_RAPIDO, peso=3, area="Conversão")
    if todas:
        return Achado("ux-whatsapp", "ux", titulo, "medido", "atencao",
                      "Há link de WhatsApp no site, mas não na página inicial do celular.",
                      evidencia=f"encontrado em {', '.join(code(o, 40) for o in outras[:3])}.",
                      significado="A página inicial é a mais visitada; o contato direto deveria estar nela.",
                      correcao="Adicionar botão de WhatsApp na página inicial, de preferência fixo no canto da tela.",
                      impacto="quem está no celular precisa navegar por outras páginas para encontrar como falar com você.",
                      prioridade="alta", esforco=ESFORCO_RAPIDO, peso=3, area="Conversão")
    return Achado("ux-whatsapp", "ux", titulo, "medido", "problema",
                  "Não encontramos link de WhatsApp.",
                  evidencia=f"nenhum link {code('wa.me')} ou {code('api.whatsapp.com')} nas {len(abertas)} páginas analisadas.",
                  significado="Para quem está no celular, falar com você exige copiar e colar o número.",
                  correcao="Transformar o número em link de WhatsApp e adicionar um botão fixo no canto da tela.",
                  impacto="cada passo extra até a conversa reduz o número de pedidos de contato.",
                  prioridade="alta", esforco=ESFORCO_RAPIDO, peso=3, area="Conversão",
                  nota_interna="Confira se há widget de chat que abre o WhatsApp sem link direto (a ferramenta não clica).")


def telefone_email(paginas: list[dict]) -> Achado:
    titulo = "Telefone e e-mail clicáveis"
    abertas = [p for p in paginas if p.get("medidas")]
    if not abertas:
        return _nao_medido("ux-tel-email", titulo, "as páginas não puderam ser abertas", 1)
    tel = _links(abertas, ("telefone",))
    mail = _links(abertas, ("email",))
    partes = []
    if tel:
        partes.append(f"telefone {code(tel[0][1]['href'], 30)}")
    if mail:
        partes.append(f"e-mail {code(mail[0][1]['href'], 50)}")
    ev = ("encontrados: " + "; ".join(partes) + ".") if partes else f"nenhum link {code('tel:')} ou {code('mailto:')} nas {len(abertas)} páginas analisadas."
    if tel and mail:
        return Achado("ux-tel-email", "ux", titulo, "medido", "ok", "O site tem telefone e e-mail clicáveis.", evidencia=ev,
                      significado="Um toque liga ou abre o e-mail, sem copiar nada.", peso=1, area="Conversão")
    if tel or mail:
        falta = "e-mail" if tel else "telefone"
        return Achado("ux-tel-email", "ux", titulo, "medido", "atencao",
                      f"O site tem {'telefone' if tel else 'e-mail'} clicável, mas não encontramos {falta} clicável.", evidencia=ev,
                      significado="Oferecer mais de um canal clicável facilita o contato para quem prefere ligar ou escrever.",
                      correcao=f"Transformar o {falta} em link clicável no rodapé e na página de contato.",
                      prioridade="baixa", esforco=ESFORCO_RAPIDO, peso=1, area="Conversão")
    return Achado("ux-tel-email", "ux", titulo, "medido", "problema", "Não encontramos telefone nem e-mail clicáveis.", evidencia=ev,
                  significado="Quem quer ligar ou mandar e-mail precisa copiar os dados à mão.",
                  correcao="Transformar telefone e e-mail em links clicáveis no rodapé e na página de contato.",
                  prioridade="baixa", esforco=ESFORCO_RAPIDO, peso=1, area="Conversão")


# Assinaturas de formulários carregados por script ou embutidos (busca no HTML renderizado).
SINAIS_FORMULARIO = [
    ("RD Station", r"rdstation|rd-form|bricks-form|RDStationForms|d335luupugsy2\.cloudfront\.net"),
    ("HubSpot", r"hsforms|hbspt\.forms|hs-form"),
    ("Typeform", r"typeform\.com|data-tf-(?:widget|popup|live)"),
    ("Google Forms", r"docs\.google\.com/forms|forms\.gle"),
    ("Elementor", r"elementor-form"),
    ("Contact Form 7", r"wpcf7"),
    ("WPForms", r"wpforms"),
    ("Gravity Forms", r"gform_wrapper|gravityforms"),
    ("Calendly", r"calendly\.com"),
    ("Jotform", r"jotform"),
]


def sinais_formulario(html: str) -> list[str]:
    """Ferramentas de formulário presentes no código da página (mesmo que o formulário não esteja visível)."""
    return [nome for nome, padrao in SINAIS_FORMULARIO if re.search(padrao, html or "", re.I)]


def formulario(paginas: list[dict], tem_contato_direto: bool, busca_contato: dict | None = None) -> Achado:
    """Classifica o formulário de contato.

    Só afirma "não há formulário" (MEDIDO) quando: todas as páginas abriram, a página de contato foi
    procurada (menu, /contato, /fale-conosco) e não há nenhum sinal de formulário carregado por script,
    embutido ou aberto por botão. Havendo qualquer sinal ou página de contato inacessível, o resultado é
    "Não foi possível confirmar".
    """
    titulo = "Formulário de contato"
    busca_contato = busca_contato or {}
    abertas = [p for p in paginas if p.get("medidas")]
    if not abertas:
        return _nao_medido("ux-form", titulo, "as páginas não puderam ser abertas", 2)
    forms = [(p["url"], f) for p in abertas for f in p["medidas"].get("formularios", [])]
    contato = [(u, f) for u, f in forms if f["campos"] >= 2]

    if contato:
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

    externos = [(p["url"], s) for p in abertas for s in p["medidas"].get("formularios_externos", [])]
    if externos:
        u, src = externos[0]
        return Achado("ux-form", "ux", titulo, "medido", "ok",
                      "Há um formulário de contato de serviço externo incorporado ao site.",
                      evidencia=f"página {code(caminho(u), 40)}: {code(src, 80)}.",
                      significado="O visitante tem uma forma de escrever para a empresa. Os campos não puderam ser medidos porque o formulário vem de outro serviço.",
                      peso=2, area="Conversão", confianca="baixa",
                      nota_interna="Formulário em iframe: abra a página e confira quantidade de campos e rótulos.")

    sinais = sorted({n for p in abertas for n in sinais_formulario(p.get("html", ""))})
    modais = [b for p in abertas for b in p["medidas"].get("botoes_modal", [])]
    falhas = [p["url"] for p in paginas if p.get("erro")]
    motivos = []
    if sinais:
        motivos.append("código de formulário de " + ", ".join(sinais))
    if modais:
        motivos.append("botão que parece abrir um formulário em janela (" + ", ".join(code(m, 40) for m in modais[:2]) + ")")
    if busca_contato.get("erro"):
        motivos.append(f"a página de contato não pôde ser aberta ({busca_contato['erro']})")
    if falhas:
        motivos.append(f"{plural(len(falhas), 'página')} não abriu")
    if motivos:
        return Achado("ux-form", "ux", titulo, "nao_confirmado", "na",
                      "Não encontramos um formulário visível sem interação, mas há sinais de que ele existe.",
                      evidencia="sinais encontrados: " + "; ".join(motivos) + ".",
                      significado="O formulário pode aparecer só depois de um clique ou carregar de forma que a análise automática não alcança.",
                      peso=2, area="Conversão", confianca="baixa",
                      nota_interna="Abra o site, clique no botão de contato e confira o formulário (campos, rótulos, se funciona no celular).")

    pagina_contato = busca_contato.get("url")
    ev = (f"analisamos {plural(len(abertas), 'página')}" +
          (f", incluindo a página de contato {code(caminho(pagina_contato), 40)}" if pagina_contato else
           f"; procuramos também {', '.join(code(t, 30) for t in busca_contato.get('tentativas', [])[:3]) or 'a página de contato'}, sem sucesso") +
          ", e não há sinal de formulário carregado por script, embutido ou aberto por botão.")
    return Achado("ux-form", "ux", titulo, "medido", "atencao" if tem_contato_direto else "problema",
                  f"Não há formulário de contato nas {len(abertas)} páginas analisadas.", evidencia=ev,
                  significado="Parte dos clientes prefere escrever a ligar ou chamar no WhatsApp, principalmente fora do horário comercial.",
                  correcao="Incluir um formulário curto (nome, contato e mensagem) na página de contato.",
                  prioridade="baixa" if tem_contato_direto else "media", esforco=ESFORCO_RAPIDO, peso=2, area="Conversão",
                  impacto="" if tem_contato_direto else "quem não quer ligar não tem outra forma simples de pedir contato.")


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


def analisar(home_mobile: dict | None, home_desktop: dict | None, paginas: list[dict],
             busca_contato: dict | None = None) -> list[Achado]:
    m = (home_mobile or {}).get("medidas")
    d = (home_desktop or {}).get("medidas")
    wa = whatsapp(m, paginas)
    tel = telefone_email(paginas)
    return [
        cta_dobra(m, "mobile"),
        cta_dobra(d, "desktop"),
        wa,
        tel,
        formulario(paginas, wa.situacao in ("ok", "atencao") or tel.situacao in ("ok", "atencao"), busca_contato),
        viewport(m),
        alvos_toque(m),
        legibilidade(m),
        prova_social(paginas),
        proposta_valor(d or m),
    ]
