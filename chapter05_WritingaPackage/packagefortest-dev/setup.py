from setuptools import setup
"""
setup.py should have same parent directory with package-you-want-install.
"""
setup(
    name="packagefortest",
    # wersion tuple should be parsed from __init__ code text.
    version="0.0.2",
    author="Joe",
    keywords="test",
    #packages is a necessary arg which is name of a real package directory.
    packages=["packagefortest"],
    install_requires=['numpy', 'pandas'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
    ]
)