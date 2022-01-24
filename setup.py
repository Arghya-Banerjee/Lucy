from gettext import find
from setuptools import find_packages
from setuptools import setup

if __name__ == '__main__':

    setup(
        name='lucy',
        version='0.1.1',
        description='this is my own personal voice command task performer',
        author='Arghya Banerjee',
        author_email='arghya.banerjee.dev@gmail.com',
        url='https://github.com/Arghya-Banerjee/Lucy',
        packages=find_packages(exclude=('tests*','testing*'))
    )

