
import ctypes
import os
import subprocess

from rich.console import Console
console = Console()
print = console.print

# constants
TARGET_PATH = "built"

def pprint(*args):
    print("[blue][𝓾𝓫𝓲𝓿𝓲𝓼][/blue] - ", end='')
    print(*args)


class Rust:
    def __init__(
        self,
        source,
        auto_construct: bool = False
    ) -> None:
        self.source = source
        if not auto_construct:
            pprint("Adding Rust libary without compilation.")
        else:
            pprint("No im not building it, no current context is available for building")
        
        self.lib = ctypes.CDLL(source)
    
class Vlang:
    def __init__(
        self,
        source,
        auto_construct: bool = False
    ) -> None:
        
        if not auto_construct and not source:
            print("Autoconstruction and library path not specified. Either one need to be present.")
        self.auto_construct = auto_construct
        self.source = source

        if auto_construct:
            lib_path = self._build()
        else:
            if not os.path.exists(source.replace(".v", ".o")):
                raise Exception("No library is present, please build it first")

        self.lib = ctypes.CDLL(lib_path)
    
    def _build(self):
        c_path = self.source.replace(".v", ".c")
        library_path = TARGET_PATH+"/"+self.source.split("/")[-1].replace(".v",".o")

        result = subprocess.run(
            ["v", "-o", c_path, self.source]
        )
        assert result.returncode == 0
        pprint("Built C ->", c_path)

        result = subprocess.run(
            [
                "gcc",
                "-shared",
                "-o",
                library_path,
                "-fPIC",
                c_path,
                "-lgc"
            ]
        )
        assert result.returncode == 0
        pprint("Built library ->",library_path)
        return library_path