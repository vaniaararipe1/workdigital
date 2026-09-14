#!/bin/bash
# Gera o app do Gerador de Propostas Work Digital para macOS.
# Rode no Terminal, dentro da pasta do projeto:  bash build_macos.sh
set -e

echo "============================================"
echo " Gerador de Propostas Work Digital - Build (macOS)"
echo "============================================"

if ! command -v python3 >/dev/null 2>&1; then
    echo "[ERRO] Python 3 nao foi encontrado. Instale em https://www.python.org/downloads/"
    exit 1
fi

echo
echo "Instalando dependencias..."
python3 -m pip install --upgrade pip >/dev/null
python3 -m pip install -r requirements.txt pyinstaller

echo
echo "Gerando o app (isso pode levar 1-2 minutos)..."
python3 -m PyInstaller --noconfirm gerador_propostas.spec

echo
echo "============================================"
echo " Pronto! O app esta em:"
echo " dist/Gerador de Propostas Work Digital.app"
echo "============================================"
echo
echo "Arraste esse .app para a pasta Aplicativos para 'instalar' no computador."
echo
echo "IMPORTANTE: para gerar o PDF automaticamente, o LibreOffice precisa"
echo "estar instalado (gratuito): https://www.libreoffice.org/download"
echo
echo "Na primeira vez que abrir, o macOS pode avisar que o app é de um"
echo "desenvolvedor nao identificado. Clique com o botao direito no app >"
echo "Abrir > Abrir mesmo assim."
