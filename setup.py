import os
import pusheen
from setuptools import find_packages
from distutils.core import setup

EXCLUDE_FROM_PACKAGES = (
    'tests',
)

def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()

setup(
    name='Pusheen',
    version=pusheen.__version__,
    description='Easily display puseens.',
    long_description=read('README.md'),
    author='Kazuki Yoshida',
    url='https://github.com/hufififi/pusheen',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    python_requires='>=3.7',
    include_package_data=True,
    install_requires=[
        'tqdm',
    ],
    entry_points={
        'console_scripts': [
            'pusheen = pusheen.pusheen:main',
        ]
    },
)
