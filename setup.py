import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def publish():
    os.system("python setup.py sdist upload")

if sys.argv[-1] == 'publish':
    publish()
    sys.exit()


setup(
    name='loading',
    version='0.0.1',
    description='simple loading bar in python',
    url='http://www.github.com/myusuf3/loading',
    author='Mahdi Yusuf',
    author_email='yusuf.mahdi@gmail.com',
    py_modules=['loading'],
    license='MIT License',
)
