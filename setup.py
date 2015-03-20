# Copyright (c) 2015, Warren Weckesser.  All rights reserved.
# This software is licensed according to the "BSD 2-clause" license.

from __future__ import print_function

import os
import sys
import numpy

from distutils.core import setup
from distutils.extension import Extension
try:
    from Cython.Distutils import build_ext
except ImportError:
    print("*** cython must be installed to build the eyediagram package. ***")
    print("setup aborted.")
    sys.exit(-1)


def get_eyediagram_version():
    """
    Find the value assigned to __version__ in eyediagram/__init__.py.

    This function assumes that there is a line of the form

        __version__ = "version-string"

    in __init__.py.  It returns the string version-string, or None if such a
    line is not found.
    """
    with open("eyediagram/__init__.py", "r") as f:
        for line in f:
            s = [w.strip() for w in line.split("=", 1)]
            if len(s) == 2 and s[0] == "__version__":
                return s[1][1:-1]


ext = Extension("eyediagram._brescount",
                [os.path.join("eyediagram", "brescount.pyx")],
                include_dirs=[numpy.get_include()])

setup(name='eyediagram',
      version=get_eyediagram_version(),
      author="Warren Weckesser",
      description="Tools for plotting an eye diagram.",
      license="BSD",
      classifiers=[
          "License :: OSI Approved :: BSD License",
          "Intended Audience :: Developers",
          "Operating System :: OS Independent",
          "Programming Language :: Python, Cython",
      ],
      ext_modules=[ext],
      packages=['eyediagram'],
      cmdclass={'build_ext': build_ext},
      install_requires=[
          'numpy >= 1.6.0',
          'scipy',
      ])
