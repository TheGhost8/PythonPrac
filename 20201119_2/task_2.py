class Num:
	def __get__(self, obj, cls):
		try:
			return obj._num
		except AttributeError:
			return 0

	def __set__(self, obj, value):
		try:
			obj._num = len(value)
			obj._num = value.real
		except TypeError:
			obj._num = value
		except AttributeError:
			obj._num = len(value)

	def __delete__(self, obj):
		obj._num = None


import sys
exec(sys.stdin.read())