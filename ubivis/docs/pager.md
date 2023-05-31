# Welcome to ubivis. ~ "tuum codice huc atque"
> Ubivis is a simple to use library that supports including shared objects from any language

# Usage
Using ubivis is simple, just import it in your python file and choose the language

```python
from ubivis import ici
from ubivis.languages import Vlang

test = ici(
    Vlang("test/example.v", auto_construct=True)
).new()

print(test.add(1))
```

The first argument for ici is the language you want to use, while autoconstruct is reliable for building your library automatically.
You can then set the returned value to a variable and use it anywhere in your code