import sys
from modulehooks import ModuleWrapper, FunctionHook

class SysWrapper(ModuleWrapper):
    excepthook = FunctionHook(sys.excepthook)
    _names = ["excepthook"]
    _restricted = ["__excepthook__"]

wrapper = SysWrapper.create(sys)
sys.modules["sys"] = wrapper
sys = wrapper
del sys, wrapper

import sys

def beforehook(a, b, c):
    print("Before exception")

def afterhook(a, b, c):
    print(f"After exception: {a!r}, {b!r}, {c!r}")

sys.excepthook = beforehook
sys.excepthook = sys.__excepthook__
sys.excepthook = afterhook

raise Exception("Test value")
