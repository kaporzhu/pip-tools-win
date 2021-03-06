"""
pip-tools keeps your pinned dependencies fresh.
"""
import sys
from setuptools import setup


def get_dependencies():
    deps = []
    if sys.version_info < (2, 7):
        deps += ['argparse']
    return deps


setup(
    name='pip-tools-win',
    version='0.0.4',
    url='https://github.com/smokingkapor/pip-tools-win',
    license='BSD',
    author='Kapor Zhu',
    author_email='smokingkapor@gmail.com',
    description=__doc__.strip('\n'),
    #packages=[],
    scripts=['bin/pip-review.py', 'bin/pip-dump.py', 'bin/pip-review.bat', 'bin/pip-dump.bat'],
    #include_package_data=True,
    zip_safe=False,
    platforms='windows',
    install_requires=get_dependencies(),
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        #'Development Status :: 1 - Planning',
        #'Development Status :: 2 - Pre-Alpha',
        #'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        #'Development Status :: 5 - Production/Stable',
        #'Development Status :: 6 - Mature',
        #'Development Status :: 7 - Inactive',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        #'Programming Language :: Python :: 2.3',
        #'Programming Language :: Python :: 2.4',
        #'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.0',
        #'Programming Language :: Python :: 3.1',
        #'Programming Language :: Python :: 3.2',
        #'Programming Language :: Python :: 3.3',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: System :: Systems Administration',
    ]
)
