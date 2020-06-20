from setuptools import setup

def readme():

      with open('README.md') as f:

            README = f.read()

      return README


setup(name='dlms_cli',
      version='0.1',
      description='DLMS CLI Tool for encrypt and decrypt APDU',
      long_description = readme(),
      long_description_content_type="text/markdown",
      url='https://github.com/ric-geek/dlms-encrypt-decrypt-cli',
      author='Riccardo',
      author_email='solidkind@gmail.com',
      license='MIT',
      classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7"
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