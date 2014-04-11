#!python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np
import os

os.environ["OPT"] = "-DDYNAMIC_ANNOTATIONS_ENABLED=1 -DNDEBUG -g -fwrapv -O3"
os.environ["CFLAGS"] = "-march=x86-64 -mtune=generic -O2 -pipe -fstack-protector --param=ssp-buffer-size=4"

if __name__=="__main__":
    setup(
            name="StellarSpectra",
            version="0.1",
            author="Ian Czekala",
            author_email="iancze",
            packages=["StellarSpectra"],
            #url="my_website", TBD
            #download_url="my_website", TBD
            license="BSD",
            description="Covariance tools for spectra",
            classifiers=[
                "Intended Audience :: Science/Research",
                "Programming Language :: Python",
            ],
            install_requires = ['numpy'],
            maintainer = "Ian Czekala",
            maintainer_email = "iancze@gmail.com",
            cmdclass = {'build_ext' :build_ext},
            ext_modules = [Extension("StellarSpectra.covariance",
                ["StellarSpectra/covariance.pyx"],
                libraries=['m', 'cholmod', 'amd', 'colamd', 'blas', 'lapack', 'suitesparseconfig'],
                include_dirs=[np.get_include()])]
    )

#By looking at /usr/lib/python3.4/distutils, we are able to dig deeper into the problem at get_config_vars around line 188
#It seems as though any command line option does not override the flags used by distutils.

#Now I compile with
#OPT="-DDYNAMIC_ANNOTATIONS_ENABLED=1 -DNDEBUG -g -fwrapv -O3" CFLAGS="-march=x86-64 -mtune=generic -O2 -pipe -fstack-protector --param=ssp-buffer-size=4" python setup.py build_ext --inplace