#!/usr/bin/env python

'''
Generate robmd.net with Wok from vendor directory
'''

import sys
import os

print "Building RobMD.net with Wok..."

# Location of the required Python modules for Wok
PYPATH = os.path.join('vendor', 'python')

# Python module locations within PYPATH
PYMODS = [
    'wok-master',
    os.path.join('PyYAML-3.10', 'lib'),
    'Markdown-2.2.0',
    'Jinja2-2.6',
]

print "Adding Python modules to the Python path..."
for module in PYMODS:
    print "\tAdding %s..."%os.path.join(PYPATH, module)
    mod_dir = os.path.join(os.getcwd(), PYPATH, module)
    sys.path.append(mod_dir)

print "Running Wok..."
from wok.engine import Engine
Engine()
