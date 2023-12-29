from setuptools import setup

setup(
    name='Ices',
    version='1.0',
    author='Iceland',
    author_email='1185330343@qq.com',
    description='Ices爬虫框架',
    packages=['Ices'],
    install_requires=[
        'asyncio',
        'aiohttp',
    ],
)