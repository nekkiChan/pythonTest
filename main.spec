# -*- mode: python ; coding: utf-8 -*-

mydata = [
    ('./views/image/asset/icon.ico', '.'),
    ('./postgresql-16.2-1-windows-x64-binaries*', '.')
]

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=mydata,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='アプリ',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='./views/image/asset/icon.ico',
)
