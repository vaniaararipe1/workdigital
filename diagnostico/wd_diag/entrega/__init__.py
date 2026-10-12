"""Entrega dos relatórios (Fase 2, ainda não implementada).

A ferramenta está separada em módulos para que a Fase 2 só precise implementar esta camada:

    coleta/     → render.py, pagespeed.py, site.py (acesso ao site)
    analise/    → achados a partir dos dados coletados (funções puras)
    pontuacao.py→ notas 0 a 100
    relatorio/  → renderização HTML/PDF das duas versões e notas internas
    revisao.py  → rascunho e validação do revisao.json
    entrega/    → (este pacote) receber o lead e entregar os arquivos

Fluxo previsto:
    1. webhook do RD Station chega em `receber_lead()` com nome, e-mail, empresa e site;
    2. o lead entra numa fila; o worker chama `pipeline.executar_diagnostico()` (versão automática);
    3. `enviar_automatica()` manda o relatorio.pdf ao lead e `avisar_revisao()` avisa a Vania
       com o link para o revisao.json e as notas internas;
    4. depois da revisão, `pipeline.gerar_revisada()` e `enviar_revisada()`.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Lead:
    nome: str
    email: str
    empresa: str
    site: str
    origem: str = "rdstation"   # rdstation | landing | prospeccao


def receber_lead(payload: dict) -> Lead:
    """Converte o JSON do webhook de conversão do RD Station em um Lead."""
    raise NotImplementedError("Fase 2")


def enviar_automatica(lead: Lead, pasta: Path) -> None:
    """Envia o relatorio.pdf (versão automática) ao lead por e-mail."""
    raise NotImplementedError("Fase 2")


def avisar_revisao(lead: Lead, pasta: Path) -> None:
    """Avisa a Vania que há um diagnóstico aguardando revisão."""
    raise NotImplementedError("Fase 2")


def enviar_revisada(lead: Lead, pasta: Path) -> None:
    """Envia o relatorio-revisado.pdf ao lead depois da aprovação."""
    raise NotImplementedError("Fase 2")
