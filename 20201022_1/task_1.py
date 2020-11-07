def fib(m, n):
	x1, x2 = 0, 1
	i = 2
	while i < m:
		x1, x2 = x2, x2+x1
		i += 1
	while i <= n+1:
		yield x1
		x1, x2 = x2, x2+x1
		i += 1

m, n = eval(input())
f = fib(m, n)
print(*f)