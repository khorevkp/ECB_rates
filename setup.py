from setuptools import setup


setup(
    name='ecbfxrates',                    # package name
    version='3.0',                          # version
    description='ECB Daily Rates History',   # short description
    url='https://github.com/khorevkp/ECB_rates',               # package URL
    install_requires=[],                    # list of packages this package depends
                                            # on.
    packages=setuptools.find_packages(exclude=['tests*']),
)