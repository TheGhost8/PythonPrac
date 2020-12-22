from types import FunctionType
from functools import wraps

def not_decorator(fun, name):
	@wraps(fun)
	def not_new_fun(*args, **kwargs):
		print(name, ": ", args[1:], ", ", kwargs, sep='')
		result = fun(*args, **kwargs)
		return result
	return not_new_fun

class dump(type):
    def __init__(self, *ap, **an):
        for attr, obj in vars(self).items():
        	if isinstance(obj, FunctionType):
        		setattr(self, attr, not_decorator(obj, attr))
        return super().__init__(self, ap, an)

class C(metaclass=dump):
    def __init__(self, val):
        self.val = val

    def add(self, other, another=None):
        return self.val + other + (another or self.val)

import sys
exec(sys.stdin.read())