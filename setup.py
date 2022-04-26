import re

from setuptools import setup


PACKAGE_NAME = 'simplecolors'


def read_file(path):
    with open(path) as f:
        return f.read()


def get_version():
    content = read_file('simplecolors/__init__.py')
    regex = r'^__version__ = [\'"]([^\'"]+)[\'"]'
    match = re.search(regex, content, re.MULTILINE)
    if match:
        return match.group(1)
    raise RuntimeError('Unable to find __version__')


setup(
    name=PACKAGE_NAME,
    version=get_version(),
    description='Yet another Python library to work with ANSI colors in the terminal',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    author='Alberto Alcolea',
    author_email='albertoalcolea@gmail.com',
    url='https://github.com/albertoalcolea/simplecolors',
    project_urls={
        'Source': 'https://github.com/albertoalcolea/simplecolors'
    },
    license='MIT',
    keywords=[
        'simplecolors',
        'simplecolor',
        'term',
        'terminal',
        'CLI',
        'color',
        'colors',
        'colour',
        'colours',
        'ANSI',
        'ANSI color',
        'ANSI colors',
        'ANSI colour',
        'ANSI colours',
    ],
    packages=[PACKAGE_NAME],
    package_data={
        PACKAGE_NAME: ['py.typed'],
    },
    extras_require={
        'dev': [
            'flake8>=4.0.1',
        ]
    },
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Terminals',
    ],
)
