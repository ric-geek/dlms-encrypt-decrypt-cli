from setuptools import setup


def readme():

      with open('README.md') as f:

            README = f.read()

      return README


setup(name='dlms_cli',
      version='1.0',
      description='DLMS CLI Tool for encrypt and decrypt APDU',
      long_description=readme(),
      long_description_content_type="text/markdown",
      url='https://github.com/ric-geek/dlms-encrypt-decrypt-cli',
      author='Riccardo',
      license='MIT',
      classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX :: Linux",
            "Development Status :: 5 - Production/Stable"
      ],
      packages=['dlms_encrypt_decrypt_tool'],
      include_package_data=True,
      install_requires=['cryptography'],
      zip_safe=False,
      entry_points={
            'console_scripts':['dlms_cli = dlms_encrypt_decrypt_tool.dlms_cli:main',
                               ],
            }
      )