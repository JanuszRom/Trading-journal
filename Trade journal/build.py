import os
import shutil
import PyInstaller.__main__

def build_app():
    # Clean previous builds
    shutil.rmtree('build', ignore_errors=True)
    shutil.rmtree('dist', ignore_errors=True)

    # Build using ONLY the spec file (no extra options)
    PyInstaller.__main__.run([
        'TradeJournal.spec',  # Only this line is needed
    ])

if __name__ == '__main__':
    build_app()