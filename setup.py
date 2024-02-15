from setuptools import setup, find_packages

setup(
    name="openai_cli",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'click',
        'openai'
    ],
    entry_points={
        'console_scripts': [
            'openai_cli = openai_cli.cli:cli',
        ],
    }
)