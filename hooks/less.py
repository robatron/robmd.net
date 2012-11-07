import os
import subprocess

'''
Wok hook for compiling Less stylesheets -> CSS in the output directory.

Any .less files found in the output directory will be compiled to CSS using
Less <http://lesscss.org/>. The compiled version of the file will be created in
the same directory as the Sass file with the same filename, but extension of
.css. For example, foo.less -> foo.css.

Installation:

    Install this as a 'site.output.post' hook, e.g., your __hooks__.py file
    might look like this:

        import less

        hooks = {
            'site.output.post':[less.compile]
        }

Dependencies:

    - Node 0.8+
'''

# Path to the Node executable 'lessc' Less compiler
LESSC = os.path.join('vendor', 'node', 'less-1.3.1', 'bin', 'lessc')
LESSC_ARGS = '--compress'


def compile(output_dir):
    print '[hook/less.compile] Finding/compiling LESS -> CSS in "%s"...'\
            %output_dir

    for root, dirs, files in os.walk(output_dir):
        for f in files:
            fname, fext = os.path.splitext(f)
            if fext == ".less":
                print "\tCompiling %s -> %s.css..."\
                        %(os.path.join(root, f), fname)

                LESS_SRC = os.path.join(root, f)
                CSS_DEST = os.path.join(root, fname + '.css')

                try:
                    subprocess.call(
                        ['node', LESSC, LESSC_ARGS, LESS_SRC, CSS_DEST]
                    )
                except OSError:
                    print "[hook/less.compile] Compilation FAILED."
