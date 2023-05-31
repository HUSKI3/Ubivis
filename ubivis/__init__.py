


import ctypes
import os
import subprocess
from typing import Any

from ubivis.languages import (
    Rust, Vlang,
    TARGET_PATH
)

def pprint(*args):
    print("[𝓾𝓫𝓲𝓿𝓲𝓼] - ", end='')
    print(*args)


def get_default_include_paths():
    try:
        result = subprocess.run(['gcc', '-E', '-Wp,-v', '-'], input='', capture_output=True, text=True)
        output = result.stderr
        include_paths = []

        # Extract include paths from the gcc output
        start_marker = '#include <...> search starts here:'
        end_marker = 'End of search list.'
        start_index = output.find(start_marker)
        end_index = output.find(end_marker)

        if start_index != -1 and end_index != -1:
            include_output = output[start_index + len(start_marker):end_index].strip()
            include_paths = include_output.split('\n')

        return include_paths
    except FileNotFoundError:
        return []

class LangWrapper:
    def __init__(self, lib) -> None:
        self.lib = lib
    def __getattr__(self, __name: str) -> Any:
        try:
            function = getattr(self.lib, __name)
        except AttributeError as e:
            print(e)
            quit()

        def execute(*args):
            return function(*args)

        return execute

class ici:
    """
    Define an import
    """
    def __init__(
        self,
        language
    ) -> None:
        self.language = language

    def new(
        self
    ):
        if not os.path.exists(TARGET_PATH):
            os.mkdir(TARGET_PATH)
        
        return LangWrapper(self.language.lib)
    
    @staticmethod
    def run_prechecks():
        header_file = "gc.h"
        include_paths = get_default_include_paths()
        if include_paths:
            if any(os.path.isfile(os.path.join(path.strip(), header_file)) for path in include_paths):
                pprint("Header file is present.")
            else:
                pprint("Header file is not present.")
        else:
            print("Unable to retrieve default include paths.")

def CFunc(arg_types=None, return_type=None, target_lib_func=None):
    if target_lib_func is None:
        raise Exception("Target library function must be defined")
    
    target_lib_func.restype = return_type
    target_lib_func.argtypes = list(arg_types)

    def __internal__layer_1(func):
        def __internal__layer_2(*args):
            return func(*args)
        return __internal__layer_2
    return __internal__layer_1
    
class Types:
    CharPtr = ctypes.c_char_p