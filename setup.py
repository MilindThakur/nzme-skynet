# coding=utf-8
"""
Setup package to install Skynet - NZME Test Automation Library dependencies
"""

import os

from setuptools import setup

from nzme_skynet import core


def readme(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='nzme-skynet',
    version=core.__version__,
    author=core.__author__,
    author_email=core.__email__,
    maintainer=core.__maintainer__,
    url=core.__url__,
    description="NZME Test Automation Library",
    license=core.__license__,
    long_description=readme('README.md'),

    packages=['nzme_skynet.core'],
    test_suite='nzme_skynet.test',
    install_requires=[
        'behave>=1.2.5',
        'pytest>=2.9.2',
        'pytest-xdist>=1.14',
        'requests>=2.10.0',
        'sauceclient>=0.2.1',
        'selenium==2.53.6',
        'chromedriver_installer>=0.0.4'
    ],
    classifiers=[
        "Development Status :: ",
        "Environment :: Web Environment",
        "Intended Audience :: Developers, Testers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Framework :: Selenium"
    ],
    zip_safe=True
)
