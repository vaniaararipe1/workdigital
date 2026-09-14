# Gerador de Propostas Comerciais — Work Digital

Sistema para gerar propostas comerciais (modelo **simples** ou **completo**)
em **PPTX e PDF** prontos para envio, sem precisar duplicar e editar o
Google Slides manualmente. O design original dos templates **não é
alterado** — o gerador só substitui o texto dos campos que variam de
cliente para cliente (nome, escopo, prazo, valor etc.), preservando
fontes, cores, imagens e layout.

## Estrutura do repositório

```
app/
  main.py                    Interface gráfica (Tkinter) com a identidade Work Digital
templates/                   Templates originais (fonte da verdade do design)
  proposta_simples.pptx      Modelo simples (4 slides)
  proposta_completa.pptx     Modelo completo (21 slides)
fonts/                       Fontes usadas nos templates (Nunito, Space Grotesk Medium)
assets/                      Logo e ícones (extraídos do template) usados no app e no executável
scripts/
  gerar_proposta.py          Gerador (motor comum usado pela GUI e pela linha de comando)
  schema_simples.json        Mapeamento dos campos editáveis do modelo simples
  schema_completa.json       Mapeamento dos campos editáveis do modelo completo
exemplos/
  dados_simples.exemplo.json
  dados_completa.exemplo.json
propostas/                   Onde os arquivos gerados são salvos ao rodar direto do repositório
gerador_propostas.spec       Receita do PyInstaller (usada pelos scripts build_*)
build_windows.bat / build_macos.sh / build_linux.sh   Geram o executável/app nativo
.claude/skills/gerar-proposta/SKILL.md   Skill do Claude Code para gerar via chat
.claude/hooks/session-start.sh           Prepara o ambiente (fontes, LibreOffice) a cada sessão
```

## Como usar

### Opção 1 — App com interface gráfica (recomendado para o dia a dia)

Veja **[INSTALACAO.md](INSTALACAO.md)** para o passo a passo completo de
instalação no Windows/Mac. Resumo: rode `build_windows.bat` (Windows) ou
`build_macos.sh` (Mac) uma vez para gerar o executável nativo, depois é só
abrir como qualquer programa instalado — escolher o modelo, preencher os
campos e clicar em **Gerar proposta**.

Para rodar a interface direto do código (sem gerar o executável), com as
dependências instaladas:
```bash
python3 app/main.py
```

### Opção 2 — Pelo chat do Claude Code

Basta pedir, por exemplo: *"gera uma proposta simples para o cliente
Alfaq"*. O Claude vai perguntar os dados que faltam, montar o arquivo de
dados e rodar o gerador automaticamente (skill `gerar-proposta`), te
entregando o PPTX e o PDF no final.

### Opção 3 — Linha de comando

1. Copie um dos exemplos em `exemplos/` e preencha com os dados do
   cliente (veja a lista de campos de cada modelo em
   `scripts/schema_simples.json` / `scripts/schema_completa.json`).

2. Rode:
   ```bash
   python3 scripts/gerar_proposta.py --tipo simples --dados meus_dados.json
   # ou
   python3 scripts/gerar_proposta.py --tipo completa --dados meus_dados.json
   ```

3. Os arquivos aparecem em `propostas/`, com o nome:
   ```
   <Cliente> Modelo de proposta comercial <simples|completa> (dd-mm-yyyy).pptx
   <Cliente> Modelo de proposta comercial <simples|completa> (dd-mm-yyyy).pdf
   ```
   > O padrão pedido foi `(dd/mm/yyyy)`, mas `/` não é um caractere válido
   > em nome de arquivo — por isso o gerador usa `dd-mm-yyyy` (traço) no
   > lugar da barra. Se quiser subir o PPTX pro Google Drive com o nome
   > exatamente com barra, é só renomear por lá (o Drive aceita `/` no
   > título, o sistema de arquivos local não).

Ambos os arquivos saem bem abaixo do limite de 5 MB (o modelo completo,
o maior caso, fica em torno de 1,5 MB).

## Dependências

- Python 3 + [`python-pptx`](https://pypi.org/project/python-pptx/) (`tkinter` também, para a GUI — já vem com a instalação padrão do Python no Windows/Mac; no Linux, pacote `python3-tk`)
- `soffice` (LibreOffice) com o componente **`libreoffice-impress`**
  instalado — é ele quem faz a conversão PPTX → PDF. O app detecta
  automaticamente se não está instalado e avisa na tela (ainda assim gera
  o PPTX normalmente).
- `poppler-utils` (opcional, só para gerar PNGs de conferência visual).

Em sessões do Claude Code na web, o hook `.claude/hooks/session-start.sh`
cuida de instalar tudo isso automaticamente a cada início de sessão. Se
for rodar localmente/fora do Claude Code, instale manualmente:

```bash
pip install python-pptx
sudo apt-get install -y libreoffice-impress poppler-utils python3-tk
```

## Gerando o executável (.exe / .app)

O app é empacotado com [PyInstaller](https://pyinstaller.org/), que
**precisa rodar no mesmo sistema operacional do executável final** (não
dá pra gerar um `.exe` a partir de Linux/Mac, por exemplo). Por isso, em
vez de um binário pronto no repositório, existe um script de build por
plataforma — rode o do seu sistema (uma vez só; veja o passo a passo
completo em [INSTALACAO.md](INSTALACAO.md)):

```bash
# Windows: dar 2 cliques em build_windows.bat
# Mac:
bash build_macos.sh
# Linux:
bash build_linux.sh
```

O executável final sai em `dist/`, já com os templates, fontes, ícone e
logo da Work Digital embutidos — não depende da pasta do projeto para
rodar (só do LibreOffice instalado à parte, para o PDF). Os arquivos
gerados pelo app ficam salvos em `Documentos/Propostas Work Digital`.

## Como adicionar ou ajustar campos

Cada campo editável é mapeado em `scripts/schema_simples.json` /
`scripts/schema_completa.json` por **slide** e **shape_id** (o id interno
do objeto no PowerPoint, estável mesmo depois de reabrir o arquivo).
Existem 4 tipos de campo:

| `tipo_campo`            | Uso                                                                 |
|--------------------------|----------------------------------------------------------------------|
| `single`                 | Um texto simples (ex: nome do cliente, valor, prazo)                |
| `suffix`                 | Mantém um rótulo em negrito e substitui só o texto depois dele (ex: "**Importante:** ...") |
| `multiline`              | Lista de linhas/bullets (ex: escopo, módulos inclusos)               |
| `multiline_com_titulo`   | Como `multiline`, mas preserva um título fixo no primeiro parágrafo (ex: "Observações:") |

Para adicionar um novo campo:

1. Abra o `.pptx` do template (`templates/proposta_*.pptx`) e identifique
   o texto que você quer tornar editável.
2. Descubra o `shape_id` dele com python-pptx:
   ```python
   from pptx import Presentation
   prs = Presentation("templates/proposta_simples.pptx")
   for i, slide in enumerate(prs.slides, start=1):
       for shape in slide.shapes:
           if shape.has_text_frame and shape.text_frame.text.strip():
               print(i, shape.shape_id, shape.text_frame.text[:60])
   ```
3. Adicione uma entrada no schema correspondente com `chave`, `slide`,
   `shape_id` e `tipo_campo`.
4. Use a nova `chave` no seu JSON de dados.

## Atualizando o design (Google Slides)

O design em si (cores, imagens, fontes, layout) vive nos Google Slides
originais, não no script. Se o design mudar lá:

1. Exporte o Google Slides como `.pptx`
   (Arquivo → Fazer download → Microsoft PowerPoint).
2. Substitua o arquivo correspondente em `templates/`.
3. Confira se os `shape_id` dos campos variáveis continuam os mesmos
   (eles mudam se os objetos de texto forem apagados e recriados do
   zero — nesse caso, atualize o schema conforme o passo acima). Editar
   o *conteúdo* de um shape existente no Slides não muda o `shape_id`.
4. Rode `python3 scripts/gerar_proposta.py ...` com um exemplo para
   conferir visualmente (gere o PDF e confira as páginas).

## Licença das fontes

`Nunito` e `Space Grotesk` são fontes do Google Fonts sob
[SIL Open Font License](https://openfontlicense.org/), livres para uso e
redistribuição — por isso estão incluídas em `fonts/` para garantir que a
conversão para PDF renderize com a tipografia correta em qualquer
ambiente.
