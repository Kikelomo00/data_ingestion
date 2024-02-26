from setuptools import setup, find_packages

setup(
    name='data_ingestion',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy','pandas','sqlalchemy','logging'],
    url='https://github.com/Kikelomo00/data_ingestion',
    author='Kareemat',
    author_email='kkabdurr@gmail.com'
)