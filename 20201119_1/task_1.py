from functools import wraps

def deccount(f):
	calls = 1
	@wraps(f)
	def call_number(*args, **kwargs):
		nonlocal calls
		print(calls)
		calls += 1
		result = f(*args, **kwargs)
		return result
	return call_number

import sys
exec(sys.stdin.read())