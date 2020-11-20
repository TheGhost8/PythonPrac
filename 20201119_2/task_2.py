class Dsc:
	def __get__(self, obj, cls):
		return obj._value

	def __set__(self, obj, val):
		try:
			obj._value = len(val)
		except TypeError:
			obj._value = val
		

class C:
	data = Dsc()

	def __init__(self, name):
		self.name = name

	def __str__(self):
		return f"<{self.name}>"

import sys
exec(sys.stdin.read())