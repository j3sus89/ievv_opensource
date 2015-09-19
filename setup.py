from setuptools import setup, find_packages


setup(
    name='ievv_opensource',
    description='The opensource modules from the commercial IEVV Django framework.',
    version='1.0',
    author='Espen Angell Kristiansen, Tor Johansen, Magne Westlie',
    author_email='post@appresso.no',
    license='BSD',
    packages=find_packages(exclude=['manage', 'tasks']),
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
