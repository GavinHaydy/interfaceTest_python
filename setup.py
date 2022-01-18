from distutils.core import setup
from setuptools import find_packages

with open("README.md", 'rb') as f:
    long_description = f.read()

setup(name='interfaceTest',  # 你包的名称
      version='1.0.0',  # 版本号
      description='test',  # 描述
      long_description=long_description,  # 长描述
      long_description_content_type='text/markdown',
      author='The-Ruffian',
      author_email='',
      url='https://github.com/the-ruffian/interfaceTest_python',
      download_url='https://github.com/the-ruffian/interfaceTest_python',
      install_requires=['requests', 'PyMySQL', 'pytest', 'pytest-assume', 'allure-pytest', 'xlrd'],  # 依赖第三方库
      license='MIT License',
      keywords=['bugpz', 'the-ruffian', 'interfaceTest'],
      packages=find_packages(),
      platforms=["all"],  # 平台
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python :: 3.0',
          'Topic :: Software Development :: Libraries'
      ],
      )
