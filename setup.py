from setuptools import setup, find_packages

import sys

if sys.version_info < (3, 0):
    sys.exit(
        ("This doesn't support python 2,"
         " it doesn't support {0}").format(sys.version))

setup(name='bowling',
      version='2021.11.20',
      description=("Bowling For Data."),
      author="cloistered monkey",
      platforms=['linux'],
      url='https://github.com/necromuralist/Bowling-For-Data',
      author_email="cloisteredmonkey.jmark@slmail.me",
      packages=find_packages(),
      )
