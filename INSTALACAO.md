# Como instalar o Gerador de Propostas no seu computador

Este guia é para quem só quer usar o programa (não precisa entender nada
de código). Existem duas coisas para instalar, uma vez só:

1. **LibreOffice** (gratuito) — é ele quem gera o PDF automaticamente.
2. **O Gerador de Propostas Work Digital** — o programa com a telinha.

## Passo 1 — Instalar o LibreOffice (se ainda não tiver)

Baixe gratuitamente em **https://www.libreoffice.org/download** e instale
normalmente (Avançar, Avançar, Concluir). Se você já usa LibreOffice ou
Microsoft Office no computador, pode pular para o próximo passo — mas o
programa usa especificamente o LibreOffice para criar o PDF, então ele
precisa estar instalado mesmo que você normalmente use o Office.

## Passo 2 — Gerar o programa (uma vez só)

O programa não vem pronto para baixar diretamente porque cada tipo de
computador (Windows, Mac) precisa da sua própria versão — por isso, a
primeira vez que for usar, você vai gerar o programa no seu computador
com um clique. Depois disso, ele fica pronto para sempre, como qualquer
outro programa instalado.

Você vai precisar do **Python** instalado (também gratuito, uma vez só):

- Baixe em **https://www.python.org/downloads/**
- **Importante no Windows:** na tela de instalação, marque a caixinha
  **"Add Python to PATH"** antes de clicar em "Install Now".

Depois de instalar o Python, dentro da pasta do projeto:

### Windows
Dê 2 cliques no arquivo **`build_windows.bat`**. Uma janela preta vai
abrir, instalar tudo sozinha e no final vai avisar onde está o
executável:
```
dist\Gerador de Propostas Work Digital.exe
```
Copie esse arquivo (ou crie um atalho dele) para a Área de Trabalho —
a partir daí é só dar 2 cliques nele para abrir o programa, como
qualquer outro app.

### Mac
Abra o Terminal, entre na pasta do projeto e rode:
```
bash build_macos.sh
```
No final vai aparecer o aplicativo em:
```
dist/Gerador de Propostas Work Digital.app
```
Arraste esse `.app` para a pasta **Aplicativos**. Na primeira vez que
abrir, o macOS pode avisar que é de um "desenvolvedor não identificado" —
clique com o botão direito no app → **Abrir** → **Abrir mesmo assim**.

## Passo 3 — Usar o programa

1. Abra o programa (ícone roxo com o robozinho da Work Digital).
2. Escolha o modelo: **Simples** ou **Completa**.
3. Preencha os campos (os marcados com `*` são obrigatórios).
4. Clique em **Gerar proposta**.
5. Pronto — o PPTX e o PDF são salvos automaticamente em
   `Documentos/Propostas Work Digital` no seu computador. Use os botões
   **Abrir pasta** e **Abrir PDF** para ver o resultado na hora.

Se quiser salvar em outro lugar, use o botão **Alterar pasta…** antes de
gerar.

## Problemas comuns

- **"LibreOffice não foi encontrado"** — instale o LibreOffice (Passo 1)
  e abra o programa de novo. Mesmo sem o LibreOffice, o PPTX é gerado
  normalmente — só o PDF automático que fica indisponível.
- **Windows reclama que o programa "não é reconhecido" (SmartScreen)** —
  isso é normal para programas novos que não foram comprados de uma loja
  oficial. Clique em "Mais informações" → "Executar assim mesmo".
