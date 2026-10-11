"""Análise de performance a partir dos dados extraídos do PageSpeed/Lighthouse."""
from __future__ import annotations

from ..modelos import ESFORCO_MEDIO, ESFORCO_RAPIDO, Achado, Metrica
from .comum import code, megabytes, num, segundos

LIMITES = {
    "lcp": (2500, 4000),
    "cls": (0.1, 0.25),
    "inp": (200, 500),
    "bytes": (2 * 1024 * 1024, 4 * 1024 * 1024),
}

FONTES = {
    "pagespeed": "Google PageSpeed Insights",
    "lighthouse_local": "Lighthouse (a mesma ferramenta do PageSpeed) executado pela Work Digital",
}

# Tradução das oportunidades do Lighthouse para linguagem de negócio.
OPORTUNIDADES = {
    "image-delivery-insight": ("Imagens mais pesadas do que o necessário",
                               "As fotos e imagens são a parte mais pesada da página e atrasam a primeira impressão.",
                               "Comprimir as imagens, usar formatos modernos (WebP ou AVIF) e enviar tamanhos menores para o celular.",
                               ESFORCO_RAPIDO),
    "modern-image-formats": ("Imagens em formatos antigos", "Formatos antigos de imagem ocupam mais espaço e demoram mais para baixar.",
                             "Converter as imagens para WebP ou AVIF.", ESFORCO_RAPIDO),
    "uses-optimized-images": ("Imagens sem compressão", "Imagens sem compressão aumentam o tempo de carregamento.",
                              "Comprimir as imagens antes de publicar.", ESFORCO_RAPIDO),
    "uses-responsive-images": ("Imagens maiores que a tela", "O celular baixa imagens no tamanho de computador.",
                               "Gerar versões menores das imagens para telas pequenas.", ESFORCO_RAPIDO),
    "offscreen-images": ("Imagens fora da tela carregadas cedo demais", "O site baixa imagens que o visitante ainda nem viu.",
                         "Ativar o carregamento sob demanda (lazy loading) para imagens abaixo da primeira tela.", ESFORCO_RAPIDO),
    "render-blocking-insight": ("Arquivos que travam o início do carregamento",
                                "A tela fica em branco enquanto o navegador espera alguns arquivos de estilo e código.",
                                "Adiar ou carregar de forma assíncrona os arquivos que não são essenciais para a primeira tela.",
                                ESFORCO_MEDIO),
    "render-blocking-resources": ("Arquivos que travam o início do carregamento",
                                  "A tela fica em branco enquanto o navegador espera alguns arquivos de estilo e código.",
                                  "Adiar os arquivos que não são essenciais para a primeira tela.", ESFORCO_MEDIO),
    "unused-javascript": ("Código que é baixado mas não é usado",
                          "O visitante baixa programação que a página não utiliza, geralmente de plugins e ferramentas externas.",
                          "Remover plugins sem uso e carregar scripts só nas páginas que precisam deles.", ESFORCO_MEDIO),
    "unused-css-rules": ("Estilos que são baixados mas não são usados", "Arquivos de estilo maiores que o necessário atrasam a exibição.",
                         "Remover estilos sem uso, comuns em temas e construtores de página.", ESFORCO_MEDIO),
    "document-latency-insight": ("Servidor demora para responder", "Antes de qualquer coisa aparecer, o servidor leva tempo para entregar a página.",
                                 "Ativar cache de página, revisar a hospedagem ou usar uma CDN.", ESFORCO_MEDIO),
    "server-response-time": ("Servidor demora para responder", "O servidor leva tempo para começar a entregar a página.",
                             "Ativar cache de página ou revisar a hospedagem.", ESFORCO_MEDIO),
    "cache-insight": ("Arquivos sem cache no navegador", "Quem volta ao site precisa baixar tudo de novo.",
                      "Configurar tempo de cache mais longo para imagens, estilos e scripts.", ESFORCO_RAPIDO),
    "uses-long-cache-ttl": ("Arquivos sem cache no navegador", "Quem volta ao site precisa baixar tudo de novo.",
                            "Configurar tempo de cache mais longo para arquivos estáticos.", ESFORCO_RAPIDO),
    "font-display-insight": ("Fontes que atrasam a exibição do texto", "O texto pode ficar invisível enquanto as fontes carregam.",
                             "Configurar as fontes para exibir o texto imediatamente (font-display: swap).", ESFORCO_RAPIDO),
    "lcp-discovery-insight": ("Imagem principal descoberta tarde", "A maior imagem da primeira tela começa a carregar depois do necessário.",
                              "Priorizar o carregamento da imagem principal e não usar carregamento sob demanda nela.", ESFORCO_RAPIDO),
    "third-parties-insight": ("Ferramentas externas pesando no carregamento", "Chats, pixels e widgets de terceiros disputam o carregamento com o conteúdo.",
                              "Revisar quais ferramentas externas são realmente necessárias e adiar as demais.", ESFORCO_MEDIO),
    "uses-text-compression": ("Arquivos de texto sem compressão", "Páginas e scripts trafegam maiores do que precisam.",
                              "Ativar compressão (gzip ou brotli) no servidor.", ESFORCO_RAPIDO),
    "legacy-javascript-insight": ("Código antigo para navegadores antigos", "O site envia código extra que navegadores atuais não precisam.",
                                  "Atualizar a configuração de build ou plugins.", ESFORCO_MEDIO),
    "duplicated-javascript": ("Código duplicado", "O mesmo código é baixado mais de uma vez.", "Remover bibliotecas duplicadas.", ESFORCO_MEDIO),
    "dom-size-insight": ("Página com estrutura muito grande", "Páginas com muitos elementos ficam lentas para desenhar e responder.",
                         "Simplificar seções da página, comum em construtores visuais.", ESFORCO_MEDIO),
    "efficient-animated-content": ("Animações em GIF pesadas", "GIFs animados são muito pesados.", "Trocar GIFs por vídeo curto.", ESFORCO_RAPIDO),
    "unminified-javascript": ("Scripts sem minificação", "Arquivos maiores que o necessário.", "Minificar os scripts.", ESFORCO_RAPIDO),
    "unminified-css": ("Estilos sem minificação", "Arquivos maiores que o necessário.", "Minificar os estilos.", ESFORCO_RAPIDO),
}


def _status(valor, chave) -> str:
    if valor is None:
        return "na"
    bom, ruim = LIMITES[chave]
    return "bom" if valor <= bom else ("medio" if valor <= ruim else "ruim")


def metricas(mobile: dict, desktop: dict) -> list[Metrica]:
    """Cartões de métricas (celular é a referência principal)."""
    base = mobile if mobile.get("ok") else desktop
    disp = "celular" if base is mobile else "computador"
    out: list[Metrica] = []
    if not base.get("ok"):
        for id_, nome in (("lcp", "Tempo até o conteúdo principal aparecer"), ("cls", "Estabilidade da página enquanto carrega"),
                          ("inp", "Resposta ao toque e ao clique"), ("bytes", "Peso da página inicial")):
            out.append(Metrica(id_, nome, "", "—", "", "na", "nao_medido", "",
                               "Não foi possível medir: a ferramenta de performance não respondeu."))
        return out

    lcp = base.get("lcp_ms")
    st = _status(lcp, "lcp")
    frase = {
        "bom": "Rápido: o visitante vê o que procura quase de imediato.",
        "medio": "Aceitável, mas acima do recomendado. Parte dos visitantes começa a perder a paciência.",
        "ruim": "O visitante olha para uma tela incompleta por tempo demais. Muita gente desiste e volta para a busca antes de ver a sua oferta.",
        "na": "Não foi possível medir.",
    }[st]
    out.append(Metrica("lcp", "Tempo até o conteúdo principal aparecer", "Maior elemento visível carregado (LCP)",
                       segundos(lcp) if lcp is not None else "—", "s" if lcp is not None else "", st,
                       "medido" if lcp is not None else "nao_medido", "Bom: até 2,5 s · Ruim: acima de 4 s",
                       f"No {disp}: {frase}", lcp))

    cls = base.get("cls")
    st = _status(cls, "cls")
    frase = {
        "bom": "Os elementos ficam no lugar enquanto a página carrega. Ponto positivo.",
        "medio": "Alguns elementos mudam de lugar durante o carregamento, o que pode causar toques no lugar errado.",
        "ruim": "Botões e textos pulam de lugar enquanto a página carrega. O visitante perde o ponto de leitura ou toca no lugar errado.",
        "na": "Não foi possível medir.",
    }[st]
    out.append(Metrica("cls", "Estabilidade da página enquanto carrega", "Mudança inesperada de layout (CLS)",
                       num(cls, 2) if cls is not None else "—", "", st, "medido" if cls is not None else "nao_medido",
                       "Bom: até 0,1 · Ruim: acima de 0,25", frase, cls))

    inp = base.get("inp_ms_campo")
    st = _status(inp, "inp")
    if inp is None:
        frase = ("Não foi possível medir: este indicador vem de visitas reais registradas pelo Google, "
                 "e o site ainda não tem volume suficiente na base pública.")
    else:
        frase = {"bom": "O site responde rápido quando o visitante toca ou clica.",
                 "medio": "Há um pequeno atraso entre o toque e a resposta da página.",
                 "ruim": "O site demora para reagir ao toque. Parece travado e passa insegurança."}[st]
    out.append(Metrica("inp", "Resposta ao toque e ao clique", "Interação até a próxima pintura (INP), dado de visitantes reais",
                       str(round(inp)) if inp is not None else "—", "ms" if inp is not None else "", st,
                       "medido" if inp is not None else "nao_medido", "Bom: até 200 ms · Ruim: acima de 500 ms", frase, inp))

    b = base.get("bytes_total")
    st = _status(b, "bytes")
    frase = {"bom": "Página leve: carrega bem mesmo em conexão móvel.",
             "medio": "Página um pouco pesada para conexões móveis.",
             "ruim": "Página pesada. Em conexão móvel, isso pesa no tempo de carregamento e no plano de dados do visitante.",
             "na": "Não foi possível medir."}[st]
    out.append(Metrica("bytes", "Peso da página inicial", "Total transferido para abrir a página",
                       megabytes(b) if b is not None else "—", "MB" if b is not None else "", st,
                       "medido" if b is not None else "nao_medido", "Referência: até 2 MB", frase, b))
    return out


def achados(mobile: dict, desktop: dict) -> list[Achado]:
    base = mobile if mobile.get("ok") else desktop
    if not base.get("ok"):
        return [Achado("perf-falha", "performance", "Medição de velocidade", "nao_medido", "na",
                       "Não foi possível medir a velocidade do site nesta data.",
                       evidencia="; ".join(f"{t['fonte']}: {t['erro']}" for t in base.get("tentativas", []) if t.get("erro")),
                       peso=0, confianca="baixa")]
    disp = "celular" if base is mobile else "computador"
    out: list[Achado] = []

    lcp = base.get("lcp_ms")
    if lcp is not None and lcp > LIMITES["lcp"][0]:
        ruim = lcp > LIMITES["lcp"][1]
        out.append(Achado(
            "perf-lcp", "performance", f"O site leva {segundos(lcp)} s para mostrar o conteúdo principal no {disp}",
            "medido", "problema" if ruim else "atencao",
            f"O conteúdo principal da página inicial só fica visível depois de {segundos(lcp)} s. O recomendado pelo Google é até 2,5 s.",
            impacto=("parte dos visitantes que chegam pelo Google ou por anúncios desiste antes de ver o que você oferece."
                     if ruim else "o visitante espera mais que o ideal na primeira impressão."),
            prioridade="alta" if ruim else "media", esforco=ESFORCO_MEDIO, peso=0, area="Performance",
            correcao="Reduzir o peso da primeira tela (imagens, scripts e fontes).", secao=False))

    cls = base.get("cls")
    if cls is not None and cls > LIMITES["cls"][1]:
        out.append(Achado(
            "perf-cls", "performance", "Elementos pulam de lugar enquanto a página carrega", "medido", "problema",
            f"O índice de estabilidade visual ficou em {num(cls, 2)}. O recomendado é até 0,1.",
            impacto="o visitante pode tocar no botão errado ou perder o que estava lendo, o que passa sensação de site mal feito.",
            prioridade="media", esforco=ESFORCO_RAPIDO, peso=0, area="Performance",
            correcao="Reservar espaço fixo para imagens, banners e fontes antes de carregarem.", secao=False))

    for op in base.get("oportunidades", [])[:4]:
        titulo, significado, correcao, esforco = OPORTUNIDADES.get(
            op["id"], (op["titulo"], "Ponto apontado pela ferramenta de medição.", "Revisar este item com um desenvolvedor.", ESFORCO_MEDIO))
        partes = []
        if op["economia_ms"]:
            partes.append(f"economia estimada de {code(segundos(op['economia_ms']) + ' s')}")
        if op["economia_bytes"]:
            partes.append(f"redução estimada de {code(megabytes(op['economia_bytes']) + ' MB')}")
        ms = op["economia_ms"]
        prioridade = "alta" if ms >= 1000 else ("media" if ms >= 300 or op["economia_bytes"] >= 500_000 else "baixa")
        out.append(Achado(
            f"perf-op-{op['id']}", "performance", titulo, "medido", "problema",
            f"A ferramenta de medição apontou este item na versão para {disp}.",
            evidencia=("; ".join(partes) + ".") if partes else "", significado=significado, correcao=correcao,
            prioridade=prioridade, esforco=esforco, peso=0, area="Performance"))
    return out


def nota(mobile: dict, desktop: dict) -> tuple[int | None, int, list]:
    """Nota = 70% celular + 30% computador (nota de performance do Lighthouse)."""
    partes = []
    if mobile.get("ok") and mobile.get("nota") is not None:
        partes.append(("Celular", mobile["nota"], 0.7))
    if desktop.get("ok") and desktop.get("nota") is not None:
        partes.append(("Computador", desktop["nota"], 0.3))
    if not partes:
        return None, 0, []
    total_peso = sum(p for _, _, p in partes)
    valor = round(sum(n * p for _, n, p in partes) / total_peso)
    return valor, len(partes), [{"criterio": f"Nota Lighthouse ({d})", "valor": n, "peso": p} for d, n, p in partes]


def fonte_texto(mobile: dict, desktop: dict, data_br: str) -> str:
    base = mobile if mobile.get("ok") else desktop
    if not base.get("ok"):
        return ""
    fonte = FONTES.get(base.get("fonte"), base.get("fonte"))
    extra = " Condições simuladas: celular com conexão 4G lenta." if base is mobile else ""
    return f"Fonte: {fonte}, em {data_br}.{extra}"
