"""Entrega dos relatórios (Fase 2).

    email.py   envio pelo Gmail (SMTP com senha de app)
    worker.py  processamento no GitHub Actions do repositório privado de diagnósticos:
               automatico → roda a versão automática, envia ao lead e avisa a Vania
               revisao    → quando a Vania salva o revisao.json, gera a revisada e, se pedido, envia ao lead
               falha      → avisa a Vania quando uma execução falha

A página do diagnóstico e o recebimento dos pedidos ficam no repositório privado (pasta web/, Vercel).
"""
