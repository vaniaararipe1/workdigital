"""Estruturas de dados compartilhadas pela coleta, análise e relatório."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Literal

Tipo = Literal["medido", "avaliacao", "nao_medido", "nao_confirmado"]
Situacao = Literal["ok", "atencao", "problema", "na"]
Prioridade = Literal["alta", "media", "baixa", ""]

PONTOS_SITUACAO = {"ok": 1.0, "atencao": 0.5, "problema": 0.0}

ESFORCO_RAPIDO = "rápido (horas)"
ESFORCO_MEDIO = "médio (dias)"
ESFORCO_PROJETO = "projeto (semanas)"


@dataclass
class Achado:
    """Um item verificável do relatório.

    tipo:      "medido" (dado coletado), "avaliacao" (julgamento, não entra na nota)
               "nao_medido" (coleta falhou, não entra na nota) ou
               "nao_confirmado" (não achamos, mas houve sinal de que pode existir; não entra na nota).
    situacao:  ok / atencao / problema / na.
    evidencia: trecho em HTML seguro que aponta para o dado coletado.
    peso:      peso do critério na nota da categoria (ver CRITERIOS.md).
    """

    id: str
    categoria: Literal["performance", "ux", "seo"]
    titulo: str
    tipo: Tipo
    situacao: Situacao
    o_que_vimos: str
    evidencia: str = ""
    significado: str = ""
    correcao: str = ""
    impacto: str = ""
    prioridade: Prioridade = ""
    esforco: str = ""
    peso: float = 1.0
    area: str = ""
    confianca: Literal["alta", "baixa"] = "alta"
    nota_interna: str = ""
    secao: bool = True          # False: aparece só no resumo/plano (ex.: já mostrado nos cartões)

    def conta_na_nota(self) -> bool:
        return self.tipo == "medido" and self.situacao in PONTOS_SITUACAO and self.peso > 0

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Metrica:
    id: str
    nome: str
    explicacao: str
    valor: str
    unidade: str
    status: Literal["bom", "medio", "ruim", "na"]
    tipo: Tipo
    referencia: str
    frase: str
    valor_bruto: float | None = None


@dataclass
class Tecnologia:
    nome: str
    categoria: str
    evidencia: str


@dataclass
class Nota:
    categoria: str
    nota: int | None
    criterios_medidos: int
    criterios_total: int
    detalhe: list = field(default_factory=list)

    @property
    def faixa(self) -> str:
        if self.nota is None:
            return "na"
        if self.nota >= 80:
            return "bom"
        if self.nota >= 50:
            return "medio"
        return "ruim"

    @property
    def rotulo(self) -> str:
        return {"bom": "Bom", "medio": "Precisa melhorar", "ruim": "Crítico",
                "na": "Não foi possível medir"}[self.faixa]
