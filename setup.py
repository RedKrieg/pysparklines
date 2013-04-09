#!/usr/bin/env python

from setuptools import setup, find_packages

readme = open('README.rst').read()

long_description = "%s" % readme

setup(
    name='pysparklines',
    version=0.2,
    description="pysparklines is a unicode sparkline generation library.",
    long_description=long_description,
    author="Brandon Whaley",
    author_email="redkrieg@gmail.com",
    url="https://github.com/RedKrieg/pysparklines",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sparkline = sparkline:main',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
