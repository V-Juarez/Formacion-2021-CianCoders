from setuptools import setup
from setuptools.dist import check_entry_points


setup(
  name='pv',
  version='0.1',
  py_modules=['pv'],
  install_requires=[
    'Click',
  ],
  entry_points='''
  [console_script]
  pv=pv:cli
  ''',
)