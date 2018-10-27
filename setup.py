#!/usr/bin/env python3

import setuptools

import os
import sys

if sys.version_info < (3, 3):
    sys.exit('Minimum supported Python version is 3.2')

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Get the current version
exec(open("svg42pdf/version.py").read())

setuptools.setup(
    name='SVG42PDF',
    version=VERSION,
    description='Program for SVG to PDF conversion.',
    long_description=long_description,
    url='https://github.com/karel-brinda/svg42pdf',
    author='Karel Brinda',
    author_email='kbrinda@hsph.harvard.edu',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: Unix',
    ],
    keywords='Graphics, SVG, PDF, Format conversion',
    packages=[
        'svg42pdf',
        'ext.svg2rlg',
    ],
    install_requires=[
        'argparse',
        'cairosvg',
        'reportlab',
    ],
    entry_points={'console_scripts': [
        'svg42pdf = svg42pdf:main',
    ]},
)
