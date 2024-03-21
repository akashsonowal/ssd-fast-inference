from setuptools import setup, find_packages

setup(
    name='ssd-fast',
    version='0.1',
    packages=find_packages(),
    install_requires=None,
    description='A simple, fast, pure PyTorch ssd inference engine',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.dev/akashsonowal/ssd-fast-inference/',
)