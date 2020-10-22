def fib_pow(m, n, p=1):
	x1, x2 = 1, 1
	i = 2
	while i < m:
		x1, x2 = x2, x2+x1
		i += 1
	while i <= n:
		p = yield x2**p
		x1, x2 = x2, x2+x1
		i += 1

m, n, p = eval(input())
f = fib_pow(m,n,p)
print(next(f))
for i in range(3):
	print(f.send(2))