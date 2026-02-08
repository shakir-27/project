def divide_numbers(a, b):
    return a / b

def access_dict_value(d, key):
    return d[key]

def convert_to_int(value):
    return int(value)

def read_file_content(filename):
    with open(filename, 'r') as f:
        return f.read()

def list_index_access(lst, idx):
    return lst[idx]

def list_pop(lst, idx):
    return lst.pop(idx)

def set_get_element(s, elem):
    s.remove(elem)
    return elem

def tuple_unpack(tup):
    a, b, c = tup
    return a + b + c

def float_conversion(val):
    return float(val)

def str_split_no_args(s):
    return s.split()

def dict_get_nested(d, key1, key2):
    return d[key1][key2]

def json_loads_invalid(json_str):
    import json
    return json.loads(json_str)

def zero_division_in_loop(n):
    total = 0
    for i in range(n):
        total += 1 / (i - n//2)
    return total

def file_write_no_perm(filename):
    with open(filename, 'w') as f:
        f.write("test")

def attr_access_invalid(obj):
    return obj.invalid_attr

def call_non_callable(obj):
    return obj()

def iter_non_iterable(obj):
    return list(obj)

def len_none():
    return len(None)

def bool_invalid(b):
    return not b

def sum_empty():
    return sum([])

def max_empty_list():
    return max([])

def min_empty_list():
    return min([])

def dict_keys_pop(d):
    keys = list(d.keys())
    d.pop(keys[0])
    return keys

def str_index_out(s, i):
    return s[i]

def bytes_decode_invalid(b):
    return b.decode('utf-8')

def range_start_gt_stop():
    return list(range(5, 1))

def pow_overflow():
    return 2 ** 10000

def recursion_too_deep(n):
    if n > 0:
        recursion_too_deep(n - 1)
    return n

def import_missing_module():
    import non_existent_module

def glob_pattern_invalid(pattern):
    import glob
    return glob.glob(pattern)

def os_path_join_none():
    import os
    return os.path.join(None, 'test')

def time_sleep_neg():
    import time
    time.sleep(-1)

def eval_unsafe(code):
    return eval(code)

def exec_unsafe(code):
    exec(code)

def compile_invalid(source):
    compile(source, 'test.py', 'exec')

def open_binary_invalid(filename):
    with open(filename, 'rb') as f:
        return f.read().decode('utf-8')

def socket_connect_invalid():
    import socket
    s = socket.socket()
    s.connect(('invalid', 9999))

def threading_start_invalid():
    import threading
    t = threading.Thread(target=lambda: 1/0)
    t.start()
    t.join()

