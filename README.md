# Vivaldi Modders API
References to assist in modding vivaldi.

## API Generated from official source
A description of the `vivaldi.*` api namespace, as provided by the official source code. It is incomplete in some places. View [here](OfficialApi/accessKeys.html).
A description of preferences and settings within vivaldi. Details [here](OfficialApi/preferenceDefinitions.html).

## Build
1. Set up a python .venv and install the requirements
2. Download the latest file from [https://vivaldi.com/source](https://vivaldi.com/source).
3. Run the update script `./update.sh`

Note: Needs [linjackson78/jstyleson](https://github.com/linjackson78/jstyleson) installed because there are comments in the JSON files.
This can be in a python virtual environment.

## TODOs
* each `chrome.Tab` has an `extData` object which vivaldi uses for things like stacks and tiling. this needs a public reference
