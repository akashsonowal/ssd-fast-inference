from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name='ssd-fast',
    version='0.1',
    packages=find_packages(),
    install_requires=required,
    description='A simple, fast ssd inference engine',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.dev/akashsonowal/ssd-fast-inference/',
)