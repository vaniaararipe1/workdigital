"""Revisão humana: rascunho do revisao.json e validação antes de gerar a versão revisada.

Regra de integridade: a ferramenta só escreve RASCUNHOS, todos com status "pendente de revisão".
A versão revisada só é gerada quando a Vania preencheu e marcou como "revisado" cada avaliação de
especialista, a nota pessoal e o plano de ação.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from .modelos import ESFORCO_MEDIO, ESFORCO_PROJETO, ESFORCO_RAPIDO, Achado

PENDENTE = "pendente de revisão"
REVISADO = "revisado"
SITUACOES = ("ok", "atencao", "problema")
PRIORIDADES = ("alta", "media", "baixa", "")
ESFORCOS = (ESFORCO_RAPIDO, ESFORCO_MEDIO, ESFORCO_PROJETO, "")
FASES = ("Fazer primeiro", "Em seguida", "Quando possível")
FASE_POR_PRIORIDADE = {"alta": "Fazer primeiro", "media": "Em seguida", "baixa": "Quando possível"}

INSTRUCOES = (
    "Edite os textos abaixo. Para cada bloco revisado, troque o status para \"revisado\". "
    "A versão revisada só é gerada quando TODOS os blocos estiverem \"revisado\" e com texto. "
    "Campo 'situacao' aceita: ok, atencao, problema. 'prioridade': alta, media, baixa. "
    "Textos marcados com [RASCUNHO] são sugestões da ferramenta: reescreva ou apague a marcação para aceitar. "
    "O campo 'sinais_coletados' é só referência e não aparece no relatório. "
    "Depois rode: python diagnostico.py URL --nome \"Empresa\" --versao revisada. "
    "Na automação (Fase 2), salvar este arquivo já gera a versão revisada; para enviá-la ao lead, "
    "troque 'enviar_ao_lead' para true."
)


class RevisaoIncompleta(ValueError):
    def __init__(self, pendencias: list[str]):
        self.pendencias = pendencias
        super().__init__("revisão incompleta:\n" + "\n".join(f"  - {p}" for p in pendencias))


def _rascunho_nota_pessoal(empresa: str, achados: list[Achado]) -> str:
    principais = [a for a in achados if a.tipo == "medido" and a.situacao == "problema" and a.prioridade == "alta"]
    foco = principais[0].titulo.lower() if principais else "os ajustes de maior impacto"
    return (f"[RASCUNHO] Olá! Analisei o site da {empresa} com atenção. O ponto que eu atacaria primeiro é: {foco}. "
            "É uma melhoria que costuma trazer resultado rápido. Separei abaixo um plano em ordem de impacto. "
            "Se quiser, a gente conversa e eu te mostro como colocar em prática.")


def _r(texto: str) -> str:
    return f"[RASCUNHO] {texto}" if texto else ""


def criar_rascunho(r: dict, plano_fases: list[dict]) -> dict:
    """Monta o revisao.json inicial. Tudo nasce como "pendente de revisão"."""
    achados: list[Achado] = r["achados"]
    avaliacoes = []
    for a in achados:
        if a.tipo != "avaliacao":
            continue
        avaliacoes.append({
            "id": a.id,
            "titulo": a.titulo,
            "status": PENDENTE,
            "situacao": a.situacao if a.situacao in SITUACOES else "atencao",
            "o_que_vimos": _r(a.o_que_vimos),
            "o_que_significa": _r(a.significado),
            "o_que_fazer": _r(a.correcao),
            "prioridade": a.prioridade,
            "esforco": a.esforco,
            "sinais_coletados": re.sub(r"<[^>]+>", "", a.evidencia) or a.nota_interna,
        })
    plano = []
    for f in plano_fases:
        for item in f["itens"]:
            plano.append({"fase": f["nome"], "acao": item["acao"], "area": item["area"], "esforco": item["esforco"]})
    return {
        "_instrucoes": INSTRUCOES,
        "empresa": r["empresa"],
        "url": r["url_final"],
        "data_analise": r["data"],
        "demonstracao": False,
        "enviar_ao_lead": False,
        "nota_pessoal": {"status": PENDENTE, "texto": _rascunho_nota_pessoal(r["empresa"], achados)},
        "avaliacoes": avaliacoes,
        "plano": {"status": PENDENTE, "itens": plano},
    }


def salvar_rascunho(caminho: Path, dados: dict, sobrescrever: bool = False) -> bool:
    """Não sobrescreve o trabalho da Vania: só cria se o arquivo não existir."""
    if caminho.exists() and not sobrescrever:
        return False
    caminho.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")
    return True


def _preenchido(texto) -> bool:
    t = (texto or "").strip()
    return bool(t) and "[RASCUNHO]" not in t.upper()


def validar(rev: dict) -> list[str]:
    """Lista tudo o que falta para gerar a versão revisada (lista vazia = pode gerar)."""
    falta: list[str] = []
    nota = rev.get("nota_pessoal") or {}
    if nota.get("status") != REVISADO:
        falta.append("nota pessoal: status ainda não é \"revisado\"")
    if not _preenchido(nota.get("texto")):
        falta.append("nota pessoal: texto vazio ou ainda marcado como [RASCUNHO]")

    avaliacoes = rev.get("avaliacoes")
    if not avaliacoes:
        falta.append("avaliações de especialista: nenhuma encontrada no arquivo")
    for av in avaliacoes or []:
        nome = av.get("titulo") or av.get("id") or "avaliação sem título"
        if av.get("status") != REVISADO:
            falta.append(f"avaliação \"{nome}\": status ainda não é \"revisado\"")
        if not _preenchido(av.get("o_que_vimos")):
            falta.append(f"avaliação \"{nome}\": campo o_que_vimos vazio ou ainda marcado como [RASCUNHO]")
        if "[RASCUNHO]" in (av.get("o_que_significa") or "").upper():
            falta.append(f"avaliação \"{nome}\": campo o_que_significa ainda marcado como [RASCUNHO]")
        if av.get("situacao") not in SITUACOES:
            falta.append(f"avaliação \"{nome}\": situacao deve ser ok, atencao ou problema")
        if av.get("situacao") in ("atencao", "problema") and not _preenchido(av.get("o_que_fazer")):
            falta.append(f"avaliação \"{nome}\": campo o_que_fazer vazio ou ainda marcado como [RASCUNHO] (obrigatório quando há algo a melhorar)")
        if av.get("prioridade", "") not in PRIORIDADES:
            falta.append(f"avaliação \"{nome}\": prioridade deve ser alta, media ou baixa")

    plano = rev.get("plano") or {}
    if plano.get("status") != REVISADO:
        falta.append("plano \"Por onde começar\": status ainda não é \"revisado\"")
    itens = plano.get("itens") or []
    if not itens:
        falta.append("plano \"Por onde começar\": sem nenhuma ação")
    for i, it in enumerate(itens, 1):
        if it.get("fase") not in FASES:
            falta.append(f"plano, ação {i}: fase deve ser {', '.join(FASES)}")
        if not _preenchido(it.get("acao")):
            falta.append(f"plano, ação {i}: texto vazio")
    return falta


def carregar_validado(caminho: Path) -> dict:
    if not caminho.exists():
        raise RevisaoIncompleta([f"arquivo {caminho.name} não encontrado (gere primeiro a versão automática)"])
    try:
        rev = json.loads(caminho.read_text(encoding="utf-8"))
    except ValueError as e:
        raise RevisaoIncompleta([f"{caminho.name} não é um JSON válido: {e}"]) from e
    pendencias = validar(rev)
    if pendencias:
        raise RevisaoIncompleta(pendencias)
    return rev


def avaliacoes_como_achados(rev: dict) -> list[Achado]:
    """Converte as avaliações revisadas em achados para o relatório (tipo 'avaliacao', fora da nota)."""
    out = []
    categoria = {"ux-social": "ux", "ux-proposta": "ux"}
    for av in rev.get("avaliacoes", []):
        out.append(Achado(
            av["id"], categoria.get(av["id"], "ux"), av["titulo"], "avaliacao", av["situacao"],
            av["o_que_vimos"].strip(), significado=(av.get("o_que_significa") or "").strip(),
            correcao=(av.get("o_que_fazer") or "").strip() if av["situacao"] != "ok" else "",
            prioridade=av.get("prioridade", "") if av["situacao"] != "ok" else "",
            esforco=av.get("esforco", "") if av["situacao"] != "ok" else "", peso=0, area="Conversão"))
    return out


def plano_revisado(rev: dict) -> list[dict]:
    cores = {"Fazer primeiro": "#C00252", "Em seguida": "#6025E1", "Quando possível": "#04CD8F"}
    fases = [{"nome": f, "cor": cores[f], "itens": []} for f in FASES]
    for it in rev["plano"]["itens"]:
        next(f for f in fases if f["nome"] == it["fase"])["itens"].append(
            {"acao": it["acao"].strip(), "area": it.get("area", ""), "esforco": it.get("esforco", ""), "avaliacao": False})
    return fases
