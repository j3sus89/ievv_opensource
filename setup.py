from setuptools import setup, find_packages


setup(
    name='ievv_opensource',
    description='The ievv_opensource django project.',
    version='1.0',
    author='ievv_opensource',
    packages=find_packages(exclude=['manage']),
    install_requires=['setuptools'],
    include_package_data=True,
    zip_safe=False,
)
