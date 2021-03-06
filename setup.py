#!/usr/bin/env python3
from distutils.core import setup

setup(
    name='asyncpgsa',
    version='0.1.0',
    requires=[
        'asyncpg',
        'sqlalchemy',
    ],
    packages=['asyncpgsa'],
    url='https://github.com/canopytax/asyncpgsa',
    license='Apache 2.0',
    author='nhumrich',
    author_email='nick.humrich@canopytax.com',
    description='sqlalchemy support for asyncpg'
)
