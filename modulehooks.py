import types

class FunctionHook:
    def __init__(self, defaultfunc=None):
        self._defaultfunc = defaultfunc
        self._funcs = []
    
    def __call__(self, *args):
        if len(self._funcs) == 0 and callable(self._defaultfunc):
            self._defaultfunc(*args)
        else:
            for func in self._funcs:
                func(*args)

class ModuleWrapper(types.ModuleType):
    _defaultnames = ["_names", "_restricted", "_module"]
    _names = []
    _restricted = []
    _module = None

    @classmethod
    def create(cls, module):
        if cls is ModuleWrapper:
            raise Exception("Cannot use 'ModuleWrapper' class to wrap module")
        if isinstance(module, ModuleWrapper):
            raise Exception(f"Module has already been wrapped")
        wrapper = cls(module.__name__, module.__doc__)
        wrapper._module = module
        for name in wrapper._names:
            setattr(module, name, getattr(wrapper, name))
        return wrapper

    def __getattribute__(self, name):
        if name in ModuleWrapper._defaultnames or name in type(self)._names:
            return super().__getattribute__(name)
        return self._module.__getattribute__(name)
    
    def __setattr__(self, name, value):
        if name in ModuleWrapper._defaultnames:
            super().__setattr__(name, value)
        elif name in type(self)._names:
            getattr(self, name)._funcs.append(value)
        elif name in type(self)._restricted:
            raise Exception(f"Cannot override restricted function {name!r}")
        else:
            return self._module.__setattr__(name, value)
    
    def __delattr__(self, name):
        if name in type(self)._names:
            getattr(self, name)._funcs.clear()
        elif name in type(self)._restricted:
            raise Exception(f"Cannot delete restricted function {name!r}")
        else:
            self._module.__delattr__(name)
    
    def __repr__(self):
        return super().__repr__().replace("module", type(self).__name__, 1)
    __str__ = __repr__
