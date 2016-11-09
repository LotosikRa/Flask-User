"""
Origin
======

`Ling Thio's repository <http://github.com/lingthio/Flask-User>`_
"""

from __future__ import print_function
from setuptools import setup

setup(
    name='Flask-User',
    version='0.6.8m3.1.2',
    url='http://github.com/LotosikRa/Flask-User',
    license='BSD License',
    author='Ling Thio (with Illia Ananich contributions)',
    author_email='213n.lotos5@gmail.com',
    description='Customizable User Account Management for Flask: Register, Confirm email, Login, Change username, Change password, Forgot password and more.',
    long_description=__doc__,
    keywords='Flask User Registration Email Username Confirmation Password Reset',
    packages=['flask_user'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'passlib',
        'bcrypt',
        'pycryptodome',
        'Flask',
        'Flask-Login',
        'Flask-Mail',
        'Flask-SQLAlchemy',
        'Flask-WTF',
    ],
    test_suite="flask_user.tests.run_tests",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Dutch',
        'Natural Language :: English',
        'Natural Language :: French',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
