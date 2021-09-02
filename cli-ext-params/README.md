# How to pass parameters to extensions using Inkscape CLI

Currently (September 2021, Inkscape v1.1) is not possible to pass parameters
to extensions running Inkscape in headless mode for batch processing using the
CLI, but there is a workaround.

I've used this trick in [braille-l18n Inkscape extension][braille-l18n] tests.

## `preferences.xml`

Exist a file in your user's Inkscape profile configuration named
`preferences.xml`. You can see the path of this file executing (Linux):

```bash
profile_prefs="$(inkscape --user-data-directory)/preferences.xml"
echo "$profile_prefs"
```

This script stores the latest values of parameters used in extensions
in a `group` node with `"extensions"` id. Check (maybe part) of the content
of this group (100 lines in the next example) with:

```bash
start="$(< "$profile_prefs" grep -n 'id="extensions"' | cut -d: -f1)"
tail -n "+$start" "$profile_prefs" | head -n 100
```

Each attribute in this group represents a parameter in a extension. The
extension is defined by his id, and concatenated with the parameter by a dot
character (`.`). If you change a value and open Inkscape, you'll see that the
extension will have that default value.

## "Pass values" to extensions using batch processing

If you change the value of one attribute in this group and run the extension
using a verb with the  `--actions` option of `inkscape` CLI (see
`inkscape --verb-list`, `inkscape --help-all` and `inkscape --action-list`),
appending `.noprefs` to the name of the extension, this will be executed using
such default value specified in `preferences.xml`.

> See a real example about this technique in
 [braille-l18n tests script][braille-l18n-tests].

[braille-l18n]: https://github.com/mondeja/inkscape-braille-l18n-ext
[braille-l18n-tests]: https://github.com/mondeja/inkscape-braille-l18n-ext/blob/master/tests/run.sh
