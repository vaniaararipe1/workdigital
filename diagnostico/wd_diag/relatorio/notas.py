"""Notas internas: o que revisar antes de enviar e sugestões de abordagem comercial.

As sugestões são regras simples sobre dados coletados; cada uma cita o dado que a originou.
"""
from __future__ import annotations

from ..modelos import Achado


def _por_id(achados: list[Achado]) -> dict[str, Achado]:
    return {a.id: a for a in achados}


def abordagens(r: dict) -> list[dict]:
    a = _por_id(r["achados"])
    notas = r["notas"]
    techs = {t.nome for t in r["tecnologias"]}
    perf_m = r["performance"]["mobile"]
    out = []

    def add(titulo, texto, base):
        out.append({"titulo": titulo, "texto": texto, "base": base})

    if notas["performance"].nota is not None and notas["performance"].nota < 50:
        nota_cel = perf_m.get("nota") if perf_m.get("ok") else None
        add("Velocidade é o argumento mais forte",
            "Abra a conversa pela lentidão no celular. É fácil de mostrar ao vivo no PageSpeed e o dono do negócio sente na pele.",
            f"nota de performance {notas['performance'].nota}" + (f"; celular {nota_cel}" if nota_cel is not None else ""))
    construtor = techs & {"Wix", "Squarespace", "Wix Studio / Editor X"}
    if construtor and (notas["performance"].nota or 100) < 70:
        add("Site em construtor com limite de performance",
            "Construtores prontos limitam otimizações. Bom gancho para apresentar um site próprio de alta performance.",
            f"detectado: {', '.join(sorted(construtor))}")
    if {"WordPress", "Elementor"} <= techs and (notas["performance"].nota or 100) < 60:
        add("WordPress com Elementor pesado",
            "Combinação comum de sites lentos por excesso de plugins e estrutura. Ofereça otimização ou reconstrução enxuta.",
            "detectado: WordPress + Elementor")
    if a.get("ux-whatsapp") and a["ux-whatsapp"].situacao in ("problema", "atencao"):
        add("Ganho rápido: botão de WhatsApp",
            "Correção de poucas horas e efeito visível. Pode ser oferecida como primeira entrega para gerar confiança.",
            a["ux-whatsapp"].o_que_vimos)
    if a.get("ux-cta-mobile") and a["ux-cta-mobile"].situacao == "problema":
        add("Home sem convite para ação no celular",
            "Proposta de reestruturação da página inicial focada em conversão, com antes e depois.",
            a["ux-cta-mobile"].o_que_vimos)
    if (a.get("geo-org") and a["geo-org"].situacao == "problema") or (a.get("seo-schema") and a["seo-schema"].situacao == "problema"):
        add("Preparo para buscas com IA",
            "Tema novo e de interesse. Pacote de SEO técnico com dados estruturados e perguntas frequentes.",
            "sem dados estruturados de empresa")
    if not techs & {"Google Analytics 4", "Google Tag Manager"}:
        add("Sem medição de visitas detectada",
            "Pergunte quantos contatos o site gera por mês. Provavelmente não sabem. Ofereça configurar a medição junto com o projeto.",
            "nenhum Google Analytics 4 ou Tag Manager encontrado no código das páginas analisadas")
    anuncios = techs & {"Meta Pixel", "Google Ads (conversões)", "TikTok Pixel", "LinkedIn Insight"}
    if anuncios:
        add("Investe em anúncios",
            "Cada segundo de lentidão e cada falta de botão de contato desperdiça verba de mídia. Argumento de retorno sobre investimento.",
            f"detectado: {', '.join(sorted(anuncios))}")
    notas_validas = [n.nota for n in notas.values() if n.nota is not None]
    if notas_validas and min(notas_validas) >= 80:
        add("Site em bom estado",
            "Evite proposta de refação. Abordagem de evolução: conteúdo, SEO, preparo para IA e testes de conversão.",
            "todas as notas acima de 80")
    add("Referência de preço",
        "Projetos a partir de R$ 3.000. Ajuste o escopo ao tamanho dos problemas encontrados.", "política comercial")
    return out


def montar(r: dict, rascunho: dict | None = None) -> dict:
    from .contexto import top3
    achados: list[Achado] = r["achados"]
    julgamento = [a for a in achados if a.tipo == "avaliacao"]
    baixa = [a for a in achados if a.tipo in ("nao_medido", "nao_confirmado") or a.confianca == "baixa"
             or a.nota_interna and a.tipo != "avaliacao"]
    medidos = [a for a in achados if a.tipo == "medido"]
    rascunho = rascunho or {}
    avisos = list(r.get("avisos", []))
    return {
        "empresa": r["empresa"],
        "url": r["url_final"],
        "data_extenso": r["data_extenso"],
        "pasta": r.get("pasta", ""),
        "julgamento": [x.to_dict() for x in julgamento],
        "medidos": [x.to_dict() for x in medidos],
        "mais_fortes": top3(achados),
        "rascunho": rascunho,
        "baixa_confianca": [x.to_dict() for x in baixa],
        "avisos": avisos,
        "abordagens": abordagens(r),
        "paginas": r["paginas_resumo"],
        "notas": [{"categoria": n.categoria, "nota": n.nota, "medidos": n.criterios_medidos, "total": n.criterios_total,
                   "detalhe": n.detalhe} for n in r["notas"].values()],
        "performance": r["performance"],
        "tecnologias": r["tecnologias"],
    }
