
import os 
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name = 'ajayiezekiel9000scrumy',
    version = '0.1',
    packages = find_packages(),
    include_package_data=True,
    description='A simple Django app created during six-week Django Linuxjobber internship',
    long_description=README,
    author = 'ajayiezekiel9000',
    author_email = 'ade@gmail.com',
    classifier=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: X.Y',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

