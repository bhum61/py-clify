import sys
from functools import reduce

this = sys.modules[__name__]

this.__command_list = {}
this.__option_flags = ""

def command(**dc_kwargs):
    # print(dc_kwargs)
    def Inner(func):
        def wrapper(*args, **kwargs):
            func(*args)

        this.__command_list[func.__name__] = wrapper
        return wrapper
    return Inner

def option_filter(a,b):
    if a[0] != "-":
        return b
    if b[0] == "-":
        return a + b[1:]
    
    return a

def gen_args(args):
    for arg in args:
        if len(arg) > 1 and arg[0] != "-":
            yield arg 

def is_option_set(flag):
    return flag in this.__option_flags

def dispatch(args):
    args_generator = gen_args(args[3:])
    cl_args = tuple(arg for arg in args_generator)

    this.__option_flags = reduce(option_filter, args)

    cmd_func = this.__command_list[args[1]]   
    if cmd_func is not None:
        cmd_func(*cl_args)

    # print(option_flags)
