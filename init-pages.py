"""Initializes folder as test-pages root."""

import os
import shutil
import sys

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Initialize folder as test-pages (static) root.')
    parser.add_argument('static_folder', help='path to new static root folder')
    args = parser.parse_args()

    # Target folder must be empty
    if os.path.exists(args.static_folder):
        assert os.path.isdir(args.static_folder)
        reply = input('folder already exists; OK to blow way any existing contents? [y/N] ')
        if reply.lower() not in ['y', 'yes']:
            sys.exit(1)
        shutil.rmtree(args.static_folder)

    # Copy the static content
    source_folder = os.path.abspath(os.path.dirname(__file__))
    from_folder = os.path.join(source_folder, 'static-content')
    shutil.copytree(from_folder, args.static_folder, ignore=shutil.ignore_patterns('.*'))

    print('SUCCESS: the static files have been copied to {}'.format(args.static_folder))
    print('Use the compile-tests.py script to generate content for the pages.')
