import os
import subprocess

def compile_sass(output_dir):
    '''
    Compile Sass files -> CSS in the output directory.

    Any .scss or .sass files found in the output directory will be compiled 
    to CSS using Sass. The compiled version of the file will be created in the 
    same directory as the Sass file with the same name and an extension of 
    .css. For example, foo.scss -> foo.css.

    Hook:

        site.output.post

    Dependencies:

        - Ruby
        - Sass (http://sass-lang.com)
    '''
    for root, dirs, files in os.walk(output_dir):
        for f in files:
            fname, fext = os.path.splitext(f)
            if fext == ".scss" or fext == ".sass":
                abspath = os.path.abspath(root)
                sass_src = "%s/%s"%(abspath, f)
                sass_dest = "%s/%s.css"%(abspath, fname)
                sass_arg = "%s:%s"%(sass_src, sass_dest)
                subprocess.call(['sass', sass_arg])
