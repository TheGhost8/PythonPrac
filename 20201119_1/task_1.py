def count_calls(f):
	global calls;
	calls = 0
	def increase():
		global calls;
		calls += 1
		print(calls)
		return calls
	return increase

import sys
exec(sys.stdin.read())