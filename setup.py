#!/usr/bin/env python3
from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='xinput-gui',
    version='0.3.1',
    description='A simple GUI for Xorg\'s Xinput tool.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ivan Fonseca',
    author_email='ivanfon@riseup.net',
    url='https://github.com/IvanFon/xinput-gui',
    license='GPLv3+',
    python_requires='>=3.10,<=3.12',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: X11 Applications :: GTK',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Desktop Environment',
        'Topic :: Utilities'
    ],
    keywords='xinput keyboard mouse touchpad',
    packages=[
        'xinput_gui',
        'xinput_gui/gui',
        'xinput_gui/xinput'
    ],
    install_requires=['PyGObject'],
    package_data={'xinput_gui': ['res/*']},
    entry_points={'gui_scripts': ['xinput-gui = xinput_gui.__main__:main']}
)
