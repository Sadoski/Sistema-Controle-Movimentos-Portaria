# -*- mode: python -*-

block_cipher = None


a = Analysis(['__main__.py'],
             pathex=['..\\Sistema Controle Movimentos Portaria',
             'C:\\Python34\\libs\\', 'C:\\Python34\\Lib\\site-packages'],
             binaries=None,
             datas=None,
             hiddenimports=['sip', 'cffi'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='SCMP',
          debug=False,
          strip=False,
          upx=True,
	  runtime_tmpdir=None,
          console=False , icon='..\\Sistema Controle Movimentos Portaria\\imagens\\sis.ico')
