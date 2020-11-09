from python_file_loader import file_loader, call_method_on_module

if __name__ == '__main__':
    file_loader("remote_code.py")
    call_method_on_module("remote_code", "test1")
    call_method_on_module("remote_code", "test2", {"arg": "some var"})
