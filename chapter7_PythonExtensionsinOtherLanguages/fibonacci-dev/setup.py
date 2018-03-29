import os
from setuptools import setup, Extension

try:
    import Cython
    USE_CYTHON = True
    #USE_CYTHON = bool(os.environ.get("USE_CYTHON"))
except ImportError as e:
    USE_CYTHON = False

ext = ".pyx" if USE_CYTHON else ".c"

extensions = [Extension("fibonacci", ["fibonacci" + ext])]

if USE_CYTHON:
    from Cython.Build import cythonize
    extensions = cythonize(extensions)

setup(
    name="fibonacci",
    ext_modules=extensions,
    extras_require={
        'cython': ["cython==0.27.3"]
    }
)