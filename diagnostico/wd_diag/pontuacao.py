"""Notas de 0 a 100 por categoria. Regras documentadas em CRITERIOS.md."""
from __future__ import annotations

from .modelos import PONTOS_SITUACAO, Achado, Nota


def nota_por_criterios(categoria: str, achados: list[Achado]) -> Nota:
    """Média ponderada dos critérios medidos: ok = 100, atenção = 50, problema = 0.

    Avaliações de especialista e itens não medidos ficam fora do cálculo.
    """
    candidatos = [a for a in achados if a.tipo != "avaliacao" and a.peso > 0]
    medidos = [a for a in candidatos if a.conta_na_nota()]
    detalhe = [{"criterio": a.titulo, "situacao": a.situacao, "peso": a.peso,
                "pontos": PONTOS_SITUACAO.get(a.situacao)} for a in candidatos]
    if not medidos:
        return Nota(categoria, None, 0, len(candidatos), detalhe)
    soma_pesos = sum(a.peso for a in medidos)
    valor = round(100 * sum(a.peso * PONTOS_SITUACAO[a.situacao] for a in medidos) / soma_pesos)
    return Nota(categoria, valor, len(medidos), len(candidatos), detalhe)
