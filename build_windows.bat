@echo off
REM Gera o executavel do Gerador de Propostas Work Digital para Windows.
REM Rode este arquivo dando 2 cliques nele (com Python 3.10+ instalado).

setlocal

echo ============================================
echo  Gerador de Propostas Work Digital - Build (Windows)
echo ============================================

where python >nul 2>nul
if errorlevel 1 (
    echo [ERRO] Python nao foi encontrado. Instale em https://www.python.org/downloads/
    echo        e marque a opcao "Add Python to PATH" durante a instalacao.
    pause
    exit /b 1
)

echo.
echo Instalando dependencias...
python -m pip install --upgrade pip >nul
python -m pip install -r requirements.txt pyinstaller
if errorlevel 1 (
    echo [ERRO] Falha ao instalar dependencias.
    pause
    exit /b 1
)

echo.
echo Gerando o executavel (isso pode levar 1-2 minutos)...
python -m PyInstaller --noconfirm gerador_propostas.spec
if errorlevel 1 (
    echo [ERRO] Falha ao gerar o executavel.
    pause
    exit /b 1
)

echo.
echo ============================================
echo  Pronto! O executavel esta em:
echo  dist\Gerador de Propostas Work Digital.exe
echo ============================================
echo.
echo Dica: crie um atalho desse arquivo na Area de Trabalho para abrir
echo o programa como qualquer outro app instalado no computador.
echo.
echo IMPORTANTE: para gerar o PDF automaticamente, o LibreOffice precisa
echo estar instalado (gratuito): https://www.libreoffice.org/download
echo.
pause
