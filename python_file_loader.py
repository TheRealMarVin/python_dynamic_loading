import importlib
import os
import re
import sys
import traceback
from importlib.util import spec_from_loader, module_from_spec


def file_loader(base_path, equip, file, test_method, method_args, method_analyzer=None):
    path = os.path.join(base_path, equip, file)

    try:
        print(equip)
        code = open(path, "r")
        a = code.readlines()
        my_code = "".join(b for b in a)

        module_name = equip.replace(" ", "")
        my_spec = spec_from_loader(module_name, loader=None)

        my_module = module_from_spec(my_spec)

        exec(my_code, my_module.__dict__)
        sys.modules['my_module'] = my_module

        #mymodule = imp.new_module("{}_module".format(equip.replace(" ", "")))
        #exec(my_code, mymodule.__dict__)
        method = getattr(my_module, test_method)
        method_res = method(method_args[0][0].encode('utf-8').decode('utf-8'))
        if method_analyzer is not None:
            res = method_analyzer(method_res)
        else:
            res = "OK"

    except Exception:
        traceback.print_exc()
        res = "FAIL"

    print(res)
    return res
