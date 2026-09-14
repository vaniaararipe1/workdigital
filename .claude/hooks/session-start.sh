#!/bin/bash
# Prepara o ambiente para rodar scripts/gerar_proposta.py:
# - garante a lib python-pptx
# - garante o componente libreoffice-impress (necessario para exportar PDF)
# - instala poppler-utils (opcional, so para previews PNG)
# - instala as fontes do template (Nunito / Space Grotesk Medium)
# Tudo best-effort: nada aqui deve travar o inicio da sessao.
set -uo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"

# 1. python-pptx
if ! python3 -c "import pptx" >/dev/null 2>&1; then
  pip install --quiet --disable-pip-version-check python-pptx >/dev/null 2>&1 || true
fi

# 2. libreoffice-impress (necessario para soffice --convert-to pdf funcionar
#    com apresentacoes; sem ele o soffice sai com exit code 81 sem mensagem clara)
if command -v soffice >/dev/null 2>&1 && command -v dpkg >/dev/null 2>&1; then
  if ! dpkg -s libreoffice-impress >/dev/null 2>&1; then
    if command -v apt-get >/dev/null 2>&1 && [ "$(id -u)" = "0" ]; then
      apt-get update -qq >/dev/null 2>&1 || true
      apt-get install -y -qq libreoffice-impress >/dev/null 2>&1 || true
    fi
  fi
fi

# 3. poppler-utils (opcional, apenas para gerar previews PNG de verificacao)
if ! command -v pdftoppm >/dev/null 2>&1; then
  if command -v apt-get >/dev/null 2>&1 && [ "$(id -u)" = "0" ]; then
    apt-get install -y -qq poppler-utils >/dev/null 2>&1 || true
  fi
fi

# 4. Fontes do template (Nunito / Space Grotesk Medium), para o PDF sair
#    com a tipografia identica ao Google Slides original
FONTS_SRC="$PROJECT_DIR/fonts"
if [ -d "$FONTS_SRC" ]; then
  FONTS_DEST="$HOME/.fonts"
  mkdir -p "$FONTS_DEST" 2>/dev/null || true
  cp -n "$FONTS_SRC"/*.ttf "$FONTS_DEST"/ 2>/dev/null || true
  command -v fc-cache >/dev/null 2>&1 && fc-cache -f "$FONTS_DEST" >/dev/null 2>&1 || true
fi

exit 0
