# Test Pages - using GitHub Pages for interactive tests

Use this project to generate interactive test sequences as static web pages. It is intended to be used as a git submodule in a target repository, which can be configured to use GitHub Pages for rendering.

## Project configuration
To add `test-pages` to a project:

* Add `test-pages` as a git submodule. You might want to add it to the same folder for storing test specifications (see below).
* Run `test-pages/create.py` to initialize the static pages for the project. Pass in the path to the project folder you want to use for hosting the pages, for example `docs/test-pages`. The script will copy files to that folder.
* Create another folder in the project for test specification files, with subfolders for both yml specifications and xml scripts. For example `test/specs/yml` and `test/specs/xml`.
* Your test specification files must be "compiled" to update the web pages. To do that run the `compile_tests.py` script, passing to it the test-spec folder you created in the previous step. If you pass in specs folder, e.g. `test/specs`, the script will process all yaml files in that folder and also check for a `yml` subfolder and process yaml files there too. Note that the `compile_tests.py` script uses the external `pyyaml` library, so using a virtual python enviroment is recommended.
* If you are using GitHub, configure GitHub Pages in your settings to point to, e.g., `docs` folder. (For some reason, GitHub only allows you to use the root folder or `docs/`.)
* If your `test-pages` file is not at the GitHub root folder, you will also need to add an `index.html` with a link to the `test-pages` folder.


## Test specification files (.yml)

Each test specification is a single YAML file with a top level dictionary with a `name` entry (string) and `steps` list. The basic format is

```
name: <test name>

steps:

  - title: <Name of this step>
    action: <Instructions that the user should take>
    expect: <(Optional) response expected from the system under test>

  # etc.
```

## Generating test files
If you have configure your project as described above, running the `compile_tests.py` script will generate the
json test files at `docs/static/data/ ` and `docs/static/test-names`.
