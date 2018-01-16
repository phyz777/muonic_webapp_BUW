"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='muonic_webapp',

    version='1.0.0',

    description='A muonic consumer for MySQL',
    long_description=long_description,

    url='https://github.com/phyz777/muonic_webapp_BUW',

    author='Jonathan Debus, Nicolas Lang',
    author_email='jdphysik@gmail.com',

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Physicists',
        'Topic :: Science :: Astro-particle-phyics',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.5',
    ],

    packages=['muonic_webapp', 'controller', 'controller.migrations',
              'dashboard', 'dashboard.migrations', 'webapp_setup'],

    package_data={'dashboard': ['static/**/*',
                                'static/**/**/*',
                                'static/**/**/**/*',
                                'static/**/**/**/**/*',
                                'static/**/**/**/**/**/*',
                                'static/**/**/**/**/**/**/*',
                                'static/**/**/**/**/**/**/**/*',
                                'static/**/**/**/**/**/**/**/**/*',
                                'static/**/**/**/**/**/**/**/**/**/*',
                                'static/**/**/**/**/**/**/**/**/**/**/*',
                                'static/**/**/**/**/**/**/**/**/**/**/**/*',
                                'static/**/**/**/**/**/**/**/**/**/**/**/**/*',
                                'static/**/**/**/**/**/**/**/**/**/**/**/**/**/*',
                                'static/**/**/**/**/**/**/**/**/**/**/**/**/**/**/*',
                                'static/**/**/**/**/**/**/**/**/**/**/**/**/**/**/**/*',
                                'static/**/**/**/**/**/**/**/**/**/**/**/**/**/**/**/**/*',
                                'static/**/**/**/**/**/**/**/**/**/**/**/**/**/**/**/**/**/*',
                                'static/**/**/**/**/**/**/**/**/**/**/**/**/**/**/**/**/**/**/*',
                                'static/**/**/**/**/**/**/**/**/**/**/**/**/**/**/**/**/**/**/**/*',
                                'static/**/**/**/**/**/**/**/**/**/**/**/**/**/**/**/**/**/**/**/**/*',
                                'templates/app/*.html']},

    entry_points={
        'console_scripts': ['muonic_webapp=webapp_setup.webapp_setup:main']
    }
)
