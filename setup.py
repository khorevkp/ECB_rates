from setuptools import setup


setup(
    name='ECB_rates',                    # package name
    version='1.0',                          # version
    description='ECB Daily Rates History',   # short description
    url='https://github.com/khorevkp/ECB_rates',               # package URL
    install_requires=[],                    # list of packages this package depends
                                            # on.
    packages=['ecbfxrates'],              # List of module names that installing
                                            # this package will provide.
)