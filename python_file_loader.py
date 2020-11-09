import importlib
import os
import re
import sys
from importlib.util import spec_from_loader, module_from_spec

def get_module_name_from_file(file):
    file_name = os.path.basename(file)
    module_name = os.path.splitext(file_name)[0]
    return module_name

def file_loader(file):
    code = open(file, "r")
    file_content = code.readlines()
    my_code = "".join(x for x in file_content)

    module_name = get_module_name_from_file(file)
    my_spec = spec_from_loader(module_name, loader=None)
    my_module = module_from_spec(my_spec)

    exec(my_code, my_module.__dict__)
    sys.modules[module_name] = my_module


def call_method_on_module(module, method, method_args={}):
    my_module = sys.modules[module]

    method = getattr(my_module, method)
    method_res = method(**method_args)

    return  method_res