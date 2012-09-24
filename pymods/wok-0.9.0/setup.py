#!/usr/bin/env python2

from distutils.core import setup

from wok import version

setup(
    name='wok',
    version=version.encode("utf8"),
    author='Mike Cooper',
    author_email='mythmon@gmail.com',
    url='http://wok.mythmon.com',
    description='Static site generator',
    long_description=
        "Wok is a static website generator. It turns a pile of templates, "
        "content, and resources (like CSS and images) into a neat stack of "
        "plain HTML. You run it on your local computer, and it generates a "
        "directory of web files that you can upload to your web server, or "
        "serve directly.",
    download_url="http://wok.mythmon.com/download",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],
    requires=['pyyaml', 'jinja2', 'Markdown', 'docutils', 'Pygments'],
    packages=['wok'],
    scripts=['scripts/wok'],
)
