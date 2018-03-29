from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='caryatid',
    version='0.1.0',
    description='Mesh node tender and automation base',
    author='Adam A.G. Shamblin',
    author_email='signal9@zeroecks.com',
    license='MIT',
    url='https://github.com/coyote240/caryatid',
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'caryatid = caryatid.server:main'
        ]
    },
    install_requires=[
        'construct~=2.9.32',
        'netifaces~=0.10.6'
    ],
    tests_require=['nose'],
    test_suite='caryatid.tests')
