from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='onkyo-ri',
      version=version,
      description="Command line tool to control ONKYO devices connected to Raspberry Pi via Remote Interactive protocol.",
      long_description="""\
Command line tool to control ONKYO devices connected to Raspberry Pi via Remote Interactive protocol.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='ONKYO',
      author='Andreas Haack',
      author_email='ahaack@protonmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
