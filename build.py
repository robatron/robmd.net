#!/usr/bin/env python

'''
Generate robmd.net with Wok from build directory
'''

import sys
import os

# Location of the Python modules
PYMODS = os.path.join('vendor', 'python')

# Individual module directories
MODULES = [
    'wok-master',
    os.path.join('PyYAML-3.10', 'lib'),
    'Markdown-2.2.0',
    'Jinja2-2.6',
]

# Join each module to the Python path
for module in MODULES:
    mod_dir = os.path.join(os.getcwd(), PYMODS, module)
    sys.path.append(mod_dir)

# Run Wok
from wok.engine import Engine
Engine()
