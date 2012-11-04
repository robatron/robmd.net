#!/usr/bin/env python

'''
Generate robmd.net with Wok from build directory
'''

import sys
import os
import subprocess
import fnmatch

print "Building RobMD.net..."

# Location of the required Python modules and Node libraries
BUILDPATH = 'build'
PYPATH = os.path.join(BUILDPATH, 'python')
NODEPATH = os.path.join(BUILDPATH, 'node')

# Python modules and Node packages
PYMODS = [
    'wok-master',
    os.path.join('PyYAML-3.10', 'lib'),
    'Markdown-2.2.0',
    'Jinja2-2.6',
]

print "Adding Python modules to the Python path..."
for module in PYMODS:
    mod_dir = os.path.join(os.getcwd(), PYPATH, module)
    sys.path.append(mod_dir)
    print "\tAdded %s"%mod_dir

# Compile Less stylesheets
LESSC = os.path.join(NODEPATH, 'less-1.3.1', 'bin', 'lessc')
LESSDIR = os.path.join('media', 'less')
LESSFILES = os.listdir(LESSDIR)

print "Compiling Less stylesheets..."
for lessfile in LESSFILES:
    if fnmatch.fnmatch(lessfile, '*.less'):
        subprocess.call(['node', LESSC, '--compress', lessfile, lessfile + '.css'])
        print "Compiled %s"%lessfile

print "Running Wok..."
from wok.engine import Engine
Engine()
