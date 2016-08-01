"""
Flask-Angular-Injection
-------------

Flask extension to inject Flask data into AngularJS controller through a service.
"""
from setuptools import setup


setup(
    name='Flask-Angular-Injection',
    version='1.0',
    url='http://github.io/flask-angular-injection/',
    license='MIT',
    author='Sujeet Pillai',
    author_email='sujeet.pillai@gmail.com',
    description='Flask extension to inject Flask data into angularjs through a service',
    long_description=__doc__,
    packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)