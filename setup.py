import os
from setuptools import setup, find_packages

VERSION = (0, 1, 0)

f = open(os.path.join(os.path.dirname(__file__), 'README'))
readme = f.read()
f.close()

setup(
    name='brzipcode',
    version='.'.join(map(str, VERSION)),
    description='brzipcode is a lightweight app for retrieving brazilian addresses from a zip code',
    long_description='',
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django',
    ],
    keywords='zip code',
    author='Renato Pedigoni',
    author_email='renatopedigoni@gmail.com',
    url='http://github.com/rpedigoni/brzipcode',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['requests'],
)