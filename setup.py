#!/usr/bin/env python3

from setuptools import setup, find_packages

readme = open('README.rst').read()

long_description = "%s" % readme

setup(
    name='pysparklines',
    version=1.0,
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
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.2',
)
