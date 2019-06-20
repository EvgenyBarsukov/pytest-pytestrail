from m2r import parse_from_file
from setuptools import setup

import pytest_pytestrail

setup(
    name='pytest-pytestrail',
    description='pytest plugin for interaction with TestRail',
    long_description=parse_from_file('README.md'),
    version=pytest_pytestrail.__version__,
    author='tolstislon',
    author_email='tolstislon@gmail.com',
    url='https://github.com/tolstislon/pytest-pytestrail',
    packages=['pytest_pytestrail'],
    install_requires=['pytest>=3.8.0', 'testrail-api>=1.0.1'],
    include_package_data=True,
    python_requires='>=3.6',
    license='MIT License',
    entry_points={'pytest11': ['pytest_pytestrail = pytest_pytestrail.conftest']},
    keywords=['testrail', 'pytest', 'pytest-testrail', 'pytest-pytestrail', 'testrail_api'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Pytest',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Testing'
    ]
)
