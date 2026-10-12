#!/usr/bin/env python3
"""Diagnóstico Gratuito de Site · Work Digital

Uso:
    python diagnostico.py https://site-do-lead.com.br --nome "Empresa X" --versao automatica
    python diagnostico.py https://site-do-lead.com.br --nome "Empresa X" --versao revisada

A versão automática coleta os dados e gera relatorio.html/pdf, dados.json, notas-internas.html e o
rascunho revisao.json. A versão revisada NÃO acessa o site: usa os dados já coletados e o
revisao.json preenchido pela Vania, e recusa gerar se faltar algo.
"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from wd_diag.config import Config
from wd_diag.pipeline import executar_diagnostico, gerar_revisada, localizar_pasta, regerar
from wd_diag.revisao import RevisaoIncompleta
from wd_diag.seguranca import UrlInvalida


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Gera o Diagnóstico Gratuito de Site da Work Digital.")
    p.add_argument("url", nargs="?", help="endereço do site do lead (http ou https)")
    p.add_argument("--nome", help="nome da empresa, como vai aparecer na capa")
    p.add_argument("--versao", choices=("automatica", "revisada"), default="automatica",
                   help="automatica: coleta e gera o resultado técnico; revisada: gera a versão final a partir do revisao.json")
    p.add_argument("--saida", type=Path, help="pasta do relatório (padrão: relatorios/<dominio>-<data>/)")
    p.add_argument("--regerar", type=Path, metavar="PASTA",
                   help="gera de novo a versão automática e as notas a partir do dados.json, sem acessar o site")
    p.add_argument("--sem-pdf", action="store_true", help="gera só HTML e JSON")
    p.add_argument("--sem-lighthouse-local", action="store_true",
                   help="não usar o Lighthouse local quando o PageSpeed falhar")
    p.add_argument("-v", "--verboso", action="store_true")
    args = p.parse_args(argv)

    logging.basicConfig(level=logging.INFO if args.verboso else logging.WARNING, format="%(message)s")
    logging.getLogger("diagnostico").setLevel(logging.INFO)
    config = Config.do_ambiente()

    if args.regerar:
        r = regerar(args.regerar, config, gerar_pdf=not args.sem_pdf)
        print(f"Versão automática gerada de novo em: {r['pasta']}")
        return 0

    if args.versao == "revisada":
        pasta = args.saida or (localizar_pasta(args.url, config) if args.url else None)
        if not pasta or not (pasta / "dados.json").exists():
            print("Não encontrei a pasta do diagnóstico. Rode primeiro a versão automática ou informe --saida PASTA.",
                  file=sys.stderr)
            return 2
        try:
            gerar_revisada(pasta, config, gerar_pdf=not args.sem_pdf)
        except RevisaoIncompleta as e:
            print(f"Versão revisada NÃO gerada. Falta completar o {pasta / 'revisao.json'}:", file=sys.stderr)
            for item in e.pendencias:
                print(f"  - {item}", file=sys.stderr)
            return 3
        print(f"Versão revisada gerada em: {pasta / 'relatorio-revisado.pdf'}")
        return 0

    if not args.url or not args.nome:
        p.error('informe a URL e --nome "Empresa"')
    if args.sem_lighthouse_local:
        config.usar_lighthouse_local = False
    if not config.pagespeed_api_key:
        print("Aviso: PAGESPEED_API_KEY não configurada. A velocidade será medida pelo Lighthouse local.", file=sys.stderr)
    try:
        r = executar_diagnostico(args.url, args.nome, config, args.saida, gerar_pdf=not args.sem_pdf)
    except UrlInvalida as e:
        print(f"URL recusada: {e}", file=sys.stderr)
        return 2

    print(f"\nVersão automática gerada em: {r['pasta']}")
    for n in r["notas"].values():
        print(f"  {n.categoria}: {n.nota if n.nota is not None else 'sem medição'}")
    print("Próximo passo: revise o revisao.json (veja notas-internas.html) e rode com --versao revisada.")
    if r["avisos"]:
        print("\nAvisos (veja também notas-internas.html):")
        for a in r["avisos"]:
            print(f"  - {a}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
