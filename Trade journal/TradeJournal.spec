# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['src/journal_app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('icons/journal_icon.ico', 'icons'),
        ('icons/journal_icon.png', 'icons'),
        ('icons/journal_icon.icns', 'icons')
    ],
    hiddenimports=[ 'openpyxl',
        'openpyxl.styles',
        'openpyxl.worksheet',
        'pandas',
        'PIL',
        'Pillow',
        'PIL.Image',
        'PIL.ImageTk',
        'pandas._libs.tslibs.timedeltas',
        'pandas._libs.tslibs.nattype',
        'pandas._libs.skiplist',
        'openpyxl',
        'numpy',
	'io',
	'os',
	'shutil'],
    hookspath=['hooks/'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='TradeJournal',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon='icons/journal_icon.ico',
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
