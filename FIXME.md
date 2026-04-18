# FIXME

## Group 650e7cab (Bioinformatik & CAD-3D)

- **BKChem**: Fails with `ModuleNotFoundError: No module named 'imp'` on Ubuntu 24.04 (Python 3.12). The `imp` module was removed in Python 3.12.
- **PyMOL**: Fails with `ModuleNotFoundError: No module named 'imp'` when running the main module on Ubuntu 24.04 (Python 3.12).
- **LDView**: Reports `Error setting INI File` and `OSMesa not working!` during headless verification with `xvfb-run`.
- **MCP-FreeCAD**: The installation and test scripts are empty placeholders (comments only).
- **FreeCAD**: Headless verification via `xvfb-run` shows `libEGL warning: DRI3 error: Could not get DRI3 device`, though it seems to start.
