from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='formation.python',
      version=version,
      description="Formation examples",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='formation example',
      author='JeanMichel FRANCOIS',
      author_email='toutpt@gmail.com',
      url='https://github.com/toutpt/formation.python',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['formation'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      test_suite = "formation.python.tkinter.addressbook.tests",
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
