lingualeo export
================

## Configuration
Create file config.py from config.py.dist
```
  cp ./config.py.dist config.py
```
Add your settings in config.py

## Launching
Command line:
```
  python qt_export.py some_word
```
Command for hotkey alias in your DE:
```
  xsel -o | xargs /path/to/lingualeo.export/qt_export.py
```
