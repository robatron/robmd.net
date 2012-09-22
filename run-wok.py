#!/usr/bin/env python
import sys
import os

PYMOD_DIR = 'pymods'
MODULES = [
    'wok',
    os.path.join('PyYAML-3.10', 'lib'),
    'Markdown-2.2.0',
    'Jinja2-2.6',

]

for module in MODULES:
	sys.path.append(os.path.join(os.getcwd(), PYMOD_DIR, module))

from wok.engine import Engine
Engine()

