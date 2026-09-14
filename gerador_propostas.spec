# -*- mode: python ; coding: utf-8 -*-
# Spec do PyInstaller para o Gerador de Propostas Work Digital.
# Rode com os scripts build_windows.bat / build_macos.sh / build_linux.sh
# (eles so chamam `pyinstaller gerador_propostas.spec` no sistema certo).
import sys
from pathlib import Path

ROOT = Path(SPECPATH)

datas = [
    (str(ROOT / "templates"), "templates"),
    (str(ROOT / "fonts"), "fonts"),
    (str(ROOT / "scripts" / "schema_simples.json"), "scripts"),
    (str(ROOT / "scripts" / "schema_completa.json"), "scripts"),
    (str(ROOT / "assets"), "assets"),
]

if sys.platform.startswith("win"):
    icone = str(ROOT / "assets" / "icon.ico")
elif sys.platform == "darwin":
    icone = str(ROOT / "assets" / "icon.icns")
else:
    icone = None

a = Analysis(
    [str(ROOT / "app" / "main.py")],
    pathex=[str(ROOT), str(ROOT / "scripts")],
    binaries=[],
    datas=datas,
    hiddenimports=["gerar_proposta", "PIL._tkinter_finder"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="Gerador de Propostas Work Digital",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icone,
)

if sys.platform == "darwin":
    app = BUNDLE(
        exe,
        name="Gerador de Propostas Work Digital.app",
        icon=icone,
        bundle_identifier="br.art.workdigital.geradordepropostas",
    )
