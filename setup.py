from setuptools import setup

setup(name='dlms_cli',
      version='0.1',
      description='DLMS CLI Tool for encrypt and decrypt APDU',
      url='https://github.com/ric-geek/dlms-encrypt-decrypt-cli',
      author='Riccardo',
      author_email='riccardocasaro@yahoo.it',
      license='MIT',
      packages=['dlms_encrypt_decrypt_tool'],
      install_requires=['cryptography'],
      zip_safe=False,
      entry_points={
            'console_scripts':['dlms_cli = dlms_encrypt_decrypt_tool.dlms_cli:main',
                               ],
            }
      )