# modulehooks

modulehooks is a Python module used to wrap another
module with various hooks that trigger when a variable
is assigned to (for example, `sys.excepthook`). Currently
there is only one type of hook, `FunctionHook`, which
adds the function to a callback list that all gets called
when the hook is called.

This is particularly useful
with attributes such as `sys.excepthook` that could
be overwritten by any other script, and with a
`FunctionHook` all functions that were assigned to it
will be stored and called when needed.

## Example

```py
import sys
from modulehooks import ModuleWrapper, FunctionHook

class SysWrapper(ModuleWrapper):
    excepthook = FunctionHook(sys.excepthook)
    _names = ["excepthook"]
    _restricted = ["__excepthook__"]

wrapper = SysWrapper.create(sys)
sys.modules["sys"] = wrapper
sys = wrapper
```

`_names` is used to declare all hooks that are defined,
`_restricted` is used to declare attributes that cannot
be modified or deleted and `create` creates a wrapper
around the specified module. Remember to modify
`sys.modules` as well otherwise `import` will load the
default Python module and not your custom wrapper.
