#!/usr/bin/env python3

import setuptools

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name='pysparklines',
    version=1.2,
    description="pysparklines is a unicode sparkline generation library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Brandon Whaley",
    author_email="redkrieg@gmail.com",
    url="https://github.com/RedKrieg/pysparklines",
    packages=setuptools.find_packages(),
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
