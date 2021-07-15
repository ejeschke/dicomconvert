#! /usr/bin/env python
#
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import os

srcdir = os.path.dirname(__file__)

from distutils.command.build_py import build_py

long_description = '''
Convert DICOM medical image files to FITS or PNG.

* Preserves bit depth
* Writes metadata to FITS HDU table and also to image metadata as
  best as possible.
'''

setup(
    name = "dcmcvt",
    version = "0.1.0",
    author = "Eric Jeschke",
    author_email = "eric@naoj.org",
    description = ("Convert medical DICOM images to FITS or PNG."),
    long_description = long_description,
    license = "BSD",
    keywords = "DICOM medical imaging convert FITS PNG",
    url = "http://github.com/ejeschke/dcmcvt",
    packages = ['dcmcvt',
                'dcmcvt.meta', 'dcmcvt.convert',
                # tests
                ],
    package_data = {'dcmcvt.meta': ['*.yml'],},
    scripts = ['scripts/dcmcvt'],
    install_requires = ['pyyaml>=5.3.1', 'pydicom>=2.1.2',
                        'astropy>=3.2.1', 'opencv-python>=4.4.0'],
    #test_suite = "",
    classifiers=[
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: BSD License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: C',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.7',
          'Topic :: Scientific/Engineering :: Astronomy',
          'Topic :: Scientific/Engineering :: Physics',
          ],
    cmdclass={'build_py': build_py}
)
