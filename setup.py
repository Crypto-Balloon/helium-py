"""helium_py setup.py."""

from setuptools import setup

setup(
    name='helium-py',
    version='0.0.1',
    description='',
    long_description='',
    url='',
    author='Crypto Balloon LLC',
    author_email='joshua@cryptoballoon.net',
    packages=['helium_py'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Classifier: Intended Audience :: Developers',
        'Classifier: Operating System :: POSIX :: Linux',
        'Classifier: Programming Language :: Python :: 3.7',
        'Classifier: Programming Language :: Python :: 3.8',
        'Classifier: Programming Language :: Python :: 3.9',
        'Classifier: Programming Language :: Python :: 3.10',
        'Classifier: License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'requests>=2.26.0,<3',
        'betterproto[compiler]>=2.0.0b4,<3',
        'pynacl>=1.5.0',
        'base58==2.1.1',
    ],
)
