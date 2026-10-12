"""Gera um relatório de EXEMPLO com dados fictícios, só para aprovar o visual.

Uso: python exemplo/gerar_exemplo.py
"""
from __future__ import annotations

import base64
import glob
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))

from wd_diag.relatorio.gerar import data_extenso, html_para_pdf, renderizar_html  # noqa: E402

SAIDA = RAIZ / "exemplo" / "saida"

SITE_FICTICIO = """<!doctype html><html><head><meta name=viewport content="width=device-width">
<style>body{margin:0;font-family:Georgia,serif;background:#f4efe7;color:#333}
nav{background:#5b3a29;color:#fff;padding:14px 16px;font-size:15px}
.hero{height:330px;background:linear-gradient(#a98467,#6c584c);color:#fff;padding:24px 16px}
.hero h1{font-size:26px;margin:120px 0 8px}.hero p{font-size:13px;opacity:.8}
.cards{padding:16px}.c{background:#fff;height:90px;margin-bottom:12px;border-radius:6px}</style></head>
<body><nav>&#9776; Padaria Exemplo</nav><div class=hero><h1>Bem-vindo ao nosso site</h1>
<p>Tradição desde 1998</p></div><div class=cards><div class=c></div><div class=c></div></div></body></html>"""


def captura_ficticia(exe: str | None) -> str:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
        pg = b.new_page(viewport={"width": 390, "height": 760}, device_scale_factor=2)
        pg.set_content(SITE_FICTICIO)
        png = pg.screenshot()
        b.close()
    return "data:image/png;base64," + base64.b64encode(png).decode()


def contexto(captura: str) -> dict:
    hoje = date(2026, 10, 11)
    return {
        "exemplo": True,
        "versao": "revisada",
        "rodape_texto": "Análise técnica automatizada com revisão especializada.",
        "prazo_dias": 2,
        "nota_pessoal": "Olá! Este é um exemplo de nota pessoal da especialista.",
        "paginas": [],
        "empresa": "Padaria Exemplo Ltda.",
        "url": "https://www.padariaexemplo.com.br",
        "data_extenso": data_extenso(hoje),
        "captura_mobile": captura,
        "notas": [
            {"categoria": "Performance", "nota": 38, "faixa": "ruim", "rotulo": "Crítico",
             "cobertura": "Medido no celular e no computador"},
            {"categoria": "Experiência e conversão", "nota": 55, "faixa": "medio", "rotulo": "Precisa melhorar",
             "cobertura": "7 de 8 critérios medidos"},
            {"categoria": "SEO e visibilidade", "nota": 72, "faixa": "medio", "rotulo": "Precisa melhorar",
             "cobertura": "14 de 14 critérios medidos"},
        ],
        "top3": [
            {"prioridade": "alta", "titulo": "O site demora 6,4 segundos para aparecer no celular",
             "o_que_vimos": "O conteúdo principal da página inicial só fica visível depois de 6,4 s. O recomendado pelo Google é até 2,5 s.",
             "impacto": "parte relevante dos visitantes de anúncios e do Google desiste antes de ver o que você oferece."},
            {"prioridade": "alta", "titulo": "Não há botão de WhatsApp na primeira tela do celular",
             "o_que_vimos": "O número de WhatsApp aparece só no rodapé, como texto que não abre a conversa ao tocar.",
             "impacto": "quem quer encomendar precisa copiar o número à mão. Cada passo extra reduz pedidos."},
            {"prioridade": "media", "titulo": "Cinco páginas usam o mesmo título no Google",
             "o_que_vimos": "Home, Cardápio, Encomendas, Sobre e Contato têm o título \"Padaria Exemplo\".",
             "impacto": "o Google tem dificuldade de mostrar a página certa para quem busca, por exemplo, \"bolo de aniversário sob encomenda\"."},
        ],
        "secoes": [
            {
                "id": "performance", "kicker": "Performance", "titulo": "Velocidade do site",
                "intro": "Quanto tempo o visitante espera até ver e usar a página. Sites lentos perdem visitas e ficam atrás no Google.",
                "dispositivos": [{"nome": "Celular", "nota": 38}, {"nome": "Computador", "nota": 71}],
                "fonte": "Fonte: Google PageSpeed Insights, medição no celular com conexão 4G simulada, em 11/10/2026.",
                "metricas": [
                    {"nome": "Tempo até o conteúdo principal aparecer", "explicacao": "Maior elemento visível carregado (LCP)",
                     "valor": "6,4", "unidade": "s", "status": "ruim", "tipo": "medido",
                     "referencia": "Bom: até 2,5 s · Ruim: acima de 4 s",
                     "frase": "O visitante olha para uma tela incompleta por mais de 6 segundos. Muita gente fecha antes disso."},
                    {"nome": "Estabilidade da página enquanto carrega", "explicacao": "Mudança inesperada de layout (CLS)",
                     "valor": "0,02", "unidade": "", "status": "bom", "tipo": "medido",
                     "referencia": "Bom: até 0,1 · Ruim: acima de 0,25",
                     "frase": "Os elementos não pulam de lugar durante o carregamento. Ponto positivo."},
                    {"nome": "Resposta ao toque e ao clique", "explicacao": "Interação até a próxima pintura (INP)",
                     "valor": "—", "unidade": "", "status": "na", "tipo": "nao_medido",
                     "referencia": "Bom: até 200 ms",
                     "frase": "Não foi possível medir: o Google ainda não tem visitas reais suficientes deste site para calcular."},
                    {"nome": "Peso da página inicial", "explicacao": "Total transferido para abrir a página",
                     "valor": "4,8", "unidade": "MB", "status": "ruim", "tipo": "medido",
                     "referencia": "Referência: até 2 MB",
                     "frase": "Equivale a baixar um álbum de fotos inteiro para abrir uma página. No 4G, isso consome tempo e o plano de dados do cliente."},
                ],
                "titulo_itens": "Principais oportunidades",
                "itens": [
                    {"titulo": "Imagens muito pesadas", "situacao": "problema", "tipo": "medido",
                     "o_que_vimos": "As fotos da página inicial somam 3,9 MB e estão em formato JPG sem compressão.",
                     "evidencia": "PageSpeed estima economia de <code>3,1 MB</code> com formatos modernos (WebP/AVIF).",
                     "significado": "É a principal causa da lentidão no celular.",
                     "correcao": "Converter as imagens para WebP e servir tamanhos menores para o celular.",
                     "prioridade": "alta", "esforco": "rápido (horas)"},
                    {"titulo": "Scripts que travam o início do carregamento", "situacao": "problema", "tipo": "medido",
                     "o_que_vimos": "6 arquivos de código precisam terminar de baixar antes de a página aparecer.",
                     "evidencia": "Economia estimada de <code>1,2 s</code> segundo o PageSpeed.",
                     "significado": "A tela fica em branco enquanto esses arquivos chegam.",
                     "correcao": "Adiar o carregamento de plugins e scripts que não são essenciais na primeira tela.",
                     "prioridade": "media", "esforco": "médio (dias)"},
                ],
            },
            {
                "id": "ux", "kicker": "Experiência e conversão", "titulo": "O site ajuda o visitante a virar cliente?",
                "intro": "Verificamos se quem chega entende o que você oferece e consegue falar com você sem esforço, no celular e no computador.",
                "itens": [
                    {"titulo": "Chamada para ação na primeira tela", "situacao": "problema", "tipo": "medido",
                     "o_que_vimos": "No celular, nenhum botão aparece antes de rolar a página. No computador, há o botão \"Faça seu pedido\".",
                     "evidencia": "primeiro botão no celular a <code>1.240 px</code> do topo; a tela tem 760 px.",
                     "significado": "No celular, o visitante não recebe um convite claro para agir.",
                     "correcao": "Colocar um botão \"Encomendar pelo WhatsApp\" logo abaixo do título.",
                     "prioridade": "alta", "esforco": "rápido (horas)"},
                    {"titulo": "WhatsApp ou telefone clicável", "situacao": "problema", "tipo": "medido",
                     "o_que_vimos": "O número aparece só no rodapé e não é um link.",
                     "evidencia": "nenhum link <code>wa.me</code>, <code>api.whatsapp.com</code> ou <code>tel:</code> nas 5 páginas analisadas.",
                     "significado": "Para quem está no celular, falar com você exige copiar e colar o número.",
                     "correcao": "Transformar o número em link de WhatsApp e adicionar um botão fixo no canto da tela.",
                     "prioridade": "alta", "esforco": "rápido (horas)"},
                    {"titulo": "Formulário de contato", "situacao": "ok", "tipo": "medido",
                     "o_que_vimos": "Formulário com 4 campos (nome, e-mail, telefone, mensagem), todos com rótulo.",
                     "evidencia": "página <code>/contato</code>.",
                     "significado": "Curto e claro. Bom para quem prefere escrever.",
                     "correcao": "", "prioridade": "", "esforco": ""},
                    {"titulo": "Leitura confortável no celular", "situacao": "atencao", "tipo": "medido",
                     "o_que_vimos": "O site se adapta ao celular, mas 38% dos textos estão com letra menor que 14 px e 9 botões ou links são menores que o recomendado para o dedo.",
                     "evidencia": "viewport configurado; alvos de toque abaixo de <code>48×48 px</code>: 9.",
                     "significado": "Ler e tocar exige esforço, principalmente para pessoas com mais idade.",
                     "correcao": "Aumentar a fonte base para 16 px e o tamanho dos botões do menu.",
                     "prioridade": "media", "esforco": "rápido (horas)"},
                    {"titulo": "Clareza da proposta de valor", "situacao": "atencao", "tipo": "avaliacao",
                     "o_que_vimos": "O título principal é \"Bem-vindo ao nosso site\".",
                     "significado": "O título não diz o que a empresa faz nem para quem. Vale avaliar um título que responda: o que vocês vendem e por que escolher vocês.",
                     "correcao": "Sugestão: \"Pães, bolos e encomendas para festas em Pinheiros, feitos no dia\".",
                     "prioridade": "media", "esforco": "rápido (horas)"},
                    {"titulo": "Prova social visível", "situacao": "atencao", "tipo": "avaliacao",
                     "o_que_vimos": "Não encontramos depoimentos, avaliações ou logos de clientes nas páginas analisadas.",
                     "significado": "Avaliações de clientes ajudam quem está decidindo. Se vocês têm boas notas no Google, vale mostrá-las.",
                     "correcao": "Incluir 3 depoimentos curtos ou a nota do Google na página inicial.",
                     "prioridade": "baixa", "esforco": "rápido (horas)"},
                ],
            },
            {
                "id": "seo", "kicker": "SEO e visibilidade", "titulo": "Como o Google e as IAs encontram você",
                "intro": "Itens técnicos que ajudam o site a aparecer nas buscas do Google e nas respostas de assistentes como ChatGPT e Gemini.",
                "itens": [
                    {"titulo": "Títulos das páginas no Google", "situacao": "problema", "tipo": "medido",
                     "o_que_vimos": "5 páginas usam exatamente o mesmo título.",
                     "evidencia": "<code>&lt;title&gt;Padaria Exemplo&lt;/title&gt;</code> em /, /cardapio, /encomendas, /sobre, /contato.",
                     "significado": "Cada página deveria ter um título próprio, que é o texto azul que aparece no Google.",
                     "correcao": "Escrever um título único para cada página, com o serviço e o bairro.",
                     "prioridade": "media", "esforco": "rápido (horas)"},
                    {"titulo": "Descrição das páginas (meta description)", "situacao": "problema", "tipo": "medido",
                     "o_que_vimos": "3 de 5 páginas não têm descrição.",
                     "significado": "Sem ela, o Google escolhe um trecho qualquer do texto para mostrar abaixo do título.",
                     "correcao": "Escrever uma frase de até 155 caracteres para cada página.",
                     "prioridade": "baixa", "esforco": "rápido (horas)"},
                    {"titulo": "Endereço seguro (HTTPS)", "situacao": "ok", "tipo": "medido",
                     "o_que_vimos": "O site usa HTTPS e redireciona corretamente a versão sem \"www\".",
                     "significado": "O navegador mostra o cadeado e não exibe alerta de site inseguro.", "correcao": "",
                     "prioridade": "", "esforco": ""},
                    {"titulo": "Mapa do site e robots.txt", "situacao": "ok", "tipo": "medido",
                     "o_que_vimos": "Os arquivos sitemap.xml e robots.txt existem e estão acessíveis.",
                     "significado": "Ajudam o Google a encontrar todas as páginas.", "correcao": "",
                     "prioridade": "", "esforco": ""},
                    {"titulo": "Imagens sem descrição (texto alternativo)", "situacao": "problema", "tipo": "medido",
                     "o_que_vimos": "21 de 34 imagens não têm texto alternativo.",
                     "significado": "O Google não entende o que a foto mostra, e leitores de tela para pessoas com deficiência visual também não.",
                     "correcao": "Descrever brevemente cada foto de produto.",
                     "prioridade": "baixa", "esforco": "rápido (horas)"},
                    {"titulo": "Preparo para buscas com inteligência artificial (AEO/GEO)", "situacao": "problema", "tipo": "medido",
                     "o_que_vimos": "Não há dados estruturados de empresa (schema.org Organization ou LocalBusiness), nem perguntas frequentes marcadas, nem arquivo llms.txt.",
                     "significado": "Assistentes de IA têm menos informação confiável sobre endereço, horário e serviços para recomendar a padaria.",
                     "correcao": "Adicionar dados estruturados de LocalBusiness e uma seção de perguntas frequentes.",
                     "prioridade": "media", "esforco": "médio (dias)"},
                ],
            },
        ],
        "tecnologias": [
            {"categoria": "Gerenciador de conteúdo", "nome": "WordPress"},
            {"categoria": "Construtor de páginas", "nome": "Elementor"},
            {"categoria": "Análise de visitas", "nome": "Google Analytics 4"},
            {"categoria": "Gerenciador de tags", "nome": "Google Tag Manager"},
            {"categoria": "Anúncios", "nome": "Meta Pixel"},
        ],
        "plano": [
            {"nome": "Fazer primeiro", "cor": "#C00252", "itens": [
                {"acao": "Botão de WhatsApp clicável na primeira tela e fixo no celular", "area": "Conversão", "esforco": "rápido (horas)"},
                {"acao": "Comprimir e converter as imagens da página inicial", "area": "Performance", "esforco": "rápido (horas)"},
            ]},
            {"nome": "Em seguida", "cor": "#6025E1", "itens": [
                {"acao": "Reescrever o título principal com a proposta de valor", "area": "Conversão", "esforco": "rápido (horas)"},
                {"acao": "Títulos únicos para cada página", "area": "SEO", "esforco": "rápido (horas)"},
                {"acao": "Adiar scripts não essenciais", "area": "Performance", "esforco": "médio (dias)"},
                {"acao": "Dados estruturados de empresa local e perguntas frequentes", "area": "SEO e IA", "esforco": "médio (dias)"},
            ]},
            {"nome": "Quando possível", "cor": "#04CD8F", "itens": [
                {"acao": "Fonte maior e botões maiores no celular", "area": "Experiência", "esforco": "rápido (horas)"},
                {"acao": "Depoimentos ou nota do Google na página inicial", "area": "Conversão", "esforco": "rápido (horas)"},
                {"acao": "Descrições das páginas e textos alternativos das imagens", "area": "SEO", "esforco": "rápido (horas)"},
            ]},
        ],
    }


def main() -> None:
    exe = None
    achados = glob.glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome")
    if achados:
        exe = achados[0]
    SAIDA.mkdir(parents=True, exist_ok=True)
    html = renderizar_html(contexto(captura_ficticia(exe)))
    caminho_html = SAIDA / "relatorio-exemplo.html"
    caminho_html.write_text(html, encoding="utf-8")
    html_para_pdf(caminho_html, SAIDA / "relatorio-exemplo.pdf", exe)
    print("Gerado em", SAIDA)


if __name__ == "__main__":
    main()
