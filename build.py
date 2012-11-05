#!/usr/bin/env python

'''
Generate robmd.net with Wok from build directory
'''

import sys
import os
import subprocess
import glob

print "Building RobMD.net..."

# Settings
# --------

# Location of the required Python modules and Node libraries
BUILDPATH = 'build'
PYPATH = os.path.join(BUILDPATH, 'python')
NODEPATH = os.path.join(BUILDPATH, 'node')

# Python modules
PYMODS = [
    'wok-master',
    os.path.join('PyYAML-3.10', 'lib'),
    'Markdown-2.2.0',
    'Jinja2-2.6',
]

# Python init
# -----------
print "Adding Python modules to the Python path..."
for module in PYMODS:
    mod_dir = os.path.join(os.getcwd(), PYPATH, module)
    sys.path.append(mod_dir)
    print "\tAdded %s"%mod_dir

# Less
# ----
print "Compiling Less stylesheets..."

LESSC = os.path.join(NODEPATH, 'less-1.3.1', 'bin', 'lessc')
LESSFILES = glob.glob(os.path.join('media', 'less', '*.less'))

for lessfile in LESSFILES:
    subprocess.call(['node', LESSC, '--compress', lessfile, lessfile + '.css'])
    print "\tCompiled %s"%lessfile

# Wok
# ---
print "Running Wok..."
from wok.engine import Engine
Engine()
