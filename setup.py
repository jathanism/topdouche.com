#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Jathan McCollum'
__email__ = 'jathan@gmail.com'
__maintainer__ = 'Jathan McCollum'

from setuptools import setup, find_packages, Command
import glob
import os
import sys
import unittest

# Get version from pkg index
from fwdb import __version__

class CleanCommand(Command):
    description = "cleans up non-package files. (dist, build, etc.)"
    user_options = []
    def initialize_options(self):
        self.files = None
    def finalize_options(self):
        self.files = './build ./dist ./MANIFEST ./*.pyc examples/*.pyc ./*.egg-info'
    def run(self):
        print 'Cleaning: %s' % self.files
        os.system('rm -rf ' + self.files)

long_desc="""
Douche it up.
"""
setup(
    name='topdouche',
    version=__version__,
    author=__author__,
    author_email=__email__,
    maintainer=__maintainer__,
    packages=find_packages(exclude='tests'),
    license='MIT',
    url='http://topdouche.com',
    description='Who will be the Top Douche?',
    long_description=long_desc,
    scripts=[],
    cmdclass = {
        'clean': CleanCommand,
    }
)
