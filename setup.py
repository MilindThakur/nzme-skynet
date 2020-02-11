# coding=utf-8
"""
Setup package to install Skynet - NZME Test Automation Library dependencies
"""

import os
import codecs
import re
from os import path

from setuptools import setup, find_packages


def readme(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def long_description():
    this_directory = path.abspath(path.dirname(__file__))
    try:
        with open(path.join(this_directory, 'README.md'), 'rb') as f:
            return f.read().decode('utf-8')
    except IOError:
        return 'NZME Test Automation Library for Browser, Mobile and API automation'



setup(
    name='nzme-skynet',
    version=find_version('nzme_skynet/__init__.py'),
    author='Milind Thakur',
    author_email='milindat28@gmail.com',
    maintainer='milindat28@gmail.com',
    url='https://github.com/MilindThakur/nzme-skynet',
    description="NZME Test Automation Library",
    long_description_content_type='text/markdown',
    license='BSD 3-Clause License',
    long_description=long_description(),
    keywords=[
      'selenium',
      'bdd',
      'appium',
      'browser automation',
      'mobile automation'
    ],
    entry_points={
        'console_scripts': [
            'nzme-behave-parallel = nzme_skynet.scripts.behave_parallel_scenarios:main'
        ]
    },
    packages=find_packages(exclude=["test"]),
    include_package_data=True,
    test_suite='nzme_skynet.test',
    install_requires=[
        'behave',
        'requests',
        'selenium==3.141.0',
        'faker',
        'browsermob-proxy',
        'haralyzer',
        'Appium-Python-Client',
        'typing',
        'allure-behave'
    ],
    tests_require=[
        'pytest',
        'pytest-xdist',
        'httpretty'
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Testing :: Acceptance",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    zip_safe=True
)
