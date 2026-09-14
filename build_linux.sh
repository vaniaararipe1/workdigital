#!/bin/bash
# Gera o executavel do Gerador de Propostas Work Digital para Linux.
# Rode no terminal, dentro da pasta do projeto:  bash build_linux.sh
set -e

echo "============================================"
echo " Gerador de Propostas Work Digital - Build (Linux)"
echo "============================================"

if ! command -v python3 >/dev/null 2>&1; then
    echo "[ERRO] Python 3 nao foi encontrado."
    exit 1
fi

echo
echo "Instalando dependencias..."
python3 -m pip install --upgrade pip >/dev/null
python3 -m pip install -r requirements.txt pyinstaller

echo
echo "Gerando o executavel (isso pode levar 1-2 minutos)..."
python3 -m PyInstaller --noconfirm gerador_propostas.spec

echo
echo "============================================"
echo " Pronto! O executavel esta em:"
echo " dist/Gerador de Propostas Work Digital"
echo "============================================"
echo
echo "IMPORTANTE: para gerar o PDF automaticamente, o LibreOffice precisa"
echo "estar instalado (sudo apt install libreoffice-impress)."
