from setuptools import setup
from setuptools import find_packages
import sys, os

version = '0.1'

setup(name='reconciler-web',
      version=version,
      description="A tornado ui for the cf reconciler",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='juju cloudfoundry tornado',
      author='whit',
      author_email='whit.morriss@canonical.com',
      url='http://juju.ubuntu.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=["tornado",
                        "jujuclient",
                        "path.py"],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
