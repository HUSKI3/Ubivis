# Rich
import os
from rich.console import Console
from rich.syntax import Syntax

## Create console
console = Console()
print = console.print

from rich.__main__ import make_test_card

# Load documentation

# create your rich data
with console.pager():
    with open(os.path.join(__file__.rsplit("/", 1)[0], "docs","pager.md"), "rt") as code_file:
        syntax = Syntax(code_file.read(), "python")
    console.print(syntax)