import importlib.util
import sys
import os

def load_source(name, pathname):
    spec = importlib.util.spec_from_file_location(name, pathname)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

def find_module(name, path=None):
    spec = importlib.util.find_spec(name, path)
    if spec:
        return (None, spec.origin, (None, None, None))
    raise ImportError(f"No module named {name}")

def load_module(name, file, filename, details):
    return load_source(name, filename)

def get_suffixes():
    return [('.py', 'U', 1)]

# This is a partial implementation of the removed 'imp' module for Python 3.12 compatibility.
# It provides enough functionality for BKChem and PyMOL to start.
