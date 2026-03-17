import pathlib
import re
import setuptools

from Cython.Build import cythonize

init = (pathlib.Path('tree_sitter_languages') / '__init__.py').read_text()
match = re.search(r"^__version__ = '(.+)'$", init, re.MULTILINE)
version = match.group(1)

with open('README.rst') as reader:
    readme = reader.read()

setuptools.setup(
    name='tree_sitter_languages_win_arm64',
    version=version,
    description='Binary Python wheels for all tree sitter languages, with Windows ARM64 support.',
    long_description=readme,
    author='Grant Jenks',
    author_email='contact@grantjenks.com',
    url='https://github.com/mubbie/py-tree-sitter-languages-win-arm64',
    license='Apache 2.0',
    ext_modules=cythonize('tree_sitter_languages/core.pyx', language_level='3'),
    packages=['tree_sitter_languages'],
    package_data={'tree_sitter_languages': ['languages.so', 'languages.dll']},
    install_requires=['tree-sitter==0.21.3'],
    project_urls={
        'Documentation': 'https://github.com/mubbie/py-tree-sitter-languages-win-arm64',
        'Source': 'https://github.com/mubbie/py-tree-sitter-languages-win-arm64',
        'Tracker': 'https://github.com/mubbie/py-tree-sitter-languages-win-arm64/issues',
        'Upstream': 'https://github.com/grantjenks/py-tree-sitter-languages',
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
