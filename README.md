# Vivaldi Modders API
References to assist in modding vivaldi.

## apiGen.js
Run this in the vivaldi console and it will output an HTML file of the current internal API.

**WARNING!** This executes methods and could end up being destructive, so run in a clean profile / user directory.

## api.html
A description of the `vivaldi.*` api namespace. View at [api.html](api.html)

## TODOs

`vivaldi.*` API:
* Some functions do not have correctly annotated arguments
* some functions crash vivaldi when you call them (notably `exit()`), so the script has special cases to avoid them
* Callbacks have specific arguments but I don't yet know of a way to easily get at them
* Need descriptions for each api method

Other APIs:
* each `chrome.Tab` has an `extData` object which vivaldi uses for things like stacks and tiling. this needs a public reference
