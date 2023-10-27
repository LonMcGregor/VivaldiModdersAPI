# Vivaldi Modders API
References to assist in modding vivaldi.

## API Generated from official source
A description of the `vivaldi.*` api namespace, as provided by the official source code. It is incomplete in some places. View [here](OfficialApi/accessKeys.html).
A description of preferences and settings within vivaldi. Details [here](OfficialApi/preferenceDefinitions.html).

## Build
1. Download the latest file from [https://vivaldi.com/source](https://vivaldi.com/source) and save it as `vivaldi-source.tar.xz`.
2. Run this command: `tar xf vivaldi-source.tar.xz vivaldi-source/VIVALDI_VERSION vivaldi-source/vivapp/src/prefs_definitions.json vivaldi-source/extensions/schema/`
3. This will extract to a directory called `vivaldi-source`.
4. This can take a while to complete.
5. Then run `python processSource.py path/to/vivaldi-source`.

Note: Needs [linjackson78/jstyleson](https://github.com/linjackson78/jstyleson) installed because there are comments in the JSON files.
This can be in a python virtual environment.

## TODOs
* each `chrome.Tab` has an `extData` object which vivaldi uses for things like stacks and tiling. this needs a public reference
