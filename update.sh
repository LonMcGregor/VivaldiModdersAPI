#!/usr/bin/bash
tar xf "$1" vivaldi-source/VIVALDI_VERSION vivaldi-source/vivapp/src/prefs_definitions.json vivaldi-source/extensions/schema/
source .venv/bin/activate
pushd OfficialApi
python processSource.py ../vivaldi-source

