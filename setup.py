from setuptools import setup

# NOTE: This is currently duplicated from the gitdb.__init__ module, because
# that's just how you write a setup.py (nobody reads this stuff out of the
# module)

__author__ = "Sebastian Thiel"
__contact__ = "byronimo@gmail.com"
__homepage__ = "https://github.com/gitpython-developers/gitdb"
<<<<<<< .merge_file_1Q4gPL
<<<<<<< .merge_file_ek0Mnj
version_info = (2, 0, 3)
=======
version_info = (2, 0, 2)
>>>>>>> .merge_file_jqxLbk
=======
version_info = (2, 0, 2)
>>>>>>> .merge_file_0WPdQM
__version__ = '.'.join(str(i) for i in version_info)

setup(
    name="gitdb2",
    version=__version__,
    description="Git Object Database",
    author=__author__,
    author_email=__contact__,
    url=__homepage__,
    packages=('gitdb', 'gitdb.db', 'gitdb.utils', 'gitdb.test'),
    license="BSD License",
    zip_safe=False,
    install_requires=['smmap2 >= 2.0.0'],
    long_description="""GitDB is a pure-Python git object database""",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ]
)
