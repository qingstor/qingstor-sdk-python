#!/usr/bin/env python

import os

from setuptools import setup, find_packages
from qingstor.sdk import __version__

ROOT = os.path.dirname(__file__)

requires = ['requests', 'PyYAML']

setup(
    name='qingstor-sdk',
    version=__version__,
    description='The official QingStor SDK for the Python programming language.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Yunify SDK Group',
    url='https://github.com/yunify/qingstor-sdk-python',
    author_email='sdk_group@yunify.com',
    scripts=[],
    packages=find_packages('.', exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    namespace_packages=['qingstor'],
    package_dir={'sdk': 'qingstor'},
    include_package_data=True,
    install_requires=requires,
    license="Apache License 2.0",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ], )
