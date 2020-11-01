"""Test spec compiler.

Updates static folder with test files:
* Loads all .yml files from input directory and writes equivalent
  json files to the data directory in the static folder.
* Copies all .xml files to the data directory in static folder.
* Generates test-names.js file.
"""

import argparse
import glob
import json
import os

import yaml

def compile_tests(specs_folder, static_folder):
    """"""
    data_folder = os.path.join(static_folder, 'data')
    test_names = list()

    # Make list of yml folders
    yml_folders = [specs_folder]
    subfolder = os.path.join(specs_folder, 'yml')
    if os.path.exists(subfolder):
        yml_folders.append(subfolder)

    # Read all yml spec files and render json equivalent
    for ext in ['*.yaml', '*.yml']:
        pattern = '{}/**/{}'.format(specs_folder, ext)
        for yml_path in glob.iglob(pattern, recursive=True):
            # print(path)
            js = None
            with open(yml_path) as fyml:
                print('Reading {}'.format(yml_path))
                yml = yaml.safe_load(fyml)
                js = json.dumps(yml, indent=2, sort_keys=True)
            if not js:
                continue

            yml_filename = os.path.basename(yml_path)
            base, ext = os.path.splitext(yml_filename)
            json_file = '{}.json'.format(base)
            json_path = os.path.join(data_folder, json_file)
            with open(json_path, 'w') as fjs:
                print('Writing {}'.format(json_path))
                fjs.write(js)
                fjs.write('\n')
                test_names.append(base)

    # Copy xml files to data folder
    pattern = '{}/**/*.xml'.format(specs_folder)
    for xml_path in glob.iglob(pattern, recursive=True):
        shutil.copy(xml_path, data_folder)

    # Generate specfiles.js with list of json files
    test_names.sort()
    js_text = 'let testNames = ' + json.dumps(test_names, indent=2)
    #print(js_text)
    js_file = 'test-names.js'
    js_path = os.path.join(static_folder, js_file)
    with open(js_path, 'w') as fjs:
        print('Writing', js_path)
        fjs.write(js_text)
        fjs.write('\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate test files from yml specifications.')
    parser.add_argument('input_folder', help='path to test-specs folder (e.g., .../test-specs')
    parser.add_argument('output_folder', help='path to static folder (e.g., .../docs/test-pages)')
    args = parser.parse_args()

    compile_tests(args.input_folder, args.output_folder)
