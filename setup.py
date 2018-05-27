#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

requirements = []

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Grigory Starinkin",
    author_email='starinkin@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    description="Solutions for HackerRank",
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords='hackerrank',
    name='hackerrank',
    packages=find_packages(include=['hackerrank']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/velimir0xff/hackerrank-py',
    version='0.1.0',
    zip_safe=False,
)
