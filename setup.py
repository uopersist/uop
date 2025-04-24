__author__ = 'samantha'

from setuptools import setup, find_packages

packages = find_packages(exclude=['tests'])
setup(name='uop',
      version='0.1',
      description='all in one python UOP package',
      author='Samantha Atkins',
      author_email='samantha@conceptwareinc.com',
      license='internal',
      packages=packages,
      install_requires=['pymongo', 'motor', 'pytest-asyncio',
                        'sjautils@git+https://github.com/Conceptware/sjautils.git',
                        'cryptography', 'pyyaml', 'requests', 'pytest', 'uopmeta'],
      zip_safe=False)
