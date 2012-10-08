#!/usr/bin/env python

'''
Run Wok from the pymods directory for portability purposes
'''

import sys
import os

PYMOD_DIR = 'pymods'
MODULES = [
    'wok-master',
    os.path.join('PyYAML-3.10', 'lib'),
    'Markdown-2.2.0',
    'Jinja2-2.6',
]

for module in MODULES:
    mod_dir = os.path.join(os.getcwd(), PYMOD_DIR, module)
    sys.path.append(mod_dir)

from wok.engine import Engine
Engine()
