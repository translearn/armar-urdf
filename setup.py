import os
from setuptools import find_packages
from setuptools import setup

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    readme_file = f.read()

setup(name='armar',
      version='1.1.0',
      packages=find_packages(),
      include_package_data=True,
      author='translearn',
      author_email='jonas.kiemel@kit.edu',
      url='https://github.com/translearn/armar-urdf',
      description='URDF Files for Humanoid Robots of the ARMAR Family',
      long_description=readme_file,
      long_description_content_type='text/markdown',
      license='CC BY-NC 4.0',
      classifiers=[
          "Intended Audience :: Developers",
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9'],
      python_requires='>=3.5'
      )
