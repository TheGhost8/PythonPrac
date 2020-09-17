a, n = eval(input())
x, y, z = 1, 1, 1
while x < a:
	while y < a:
		while z < a:
			if x**n + y**n + z**n == a:
				print(x, y, z)
				break
			z += 1
		if x**n + y**n + z**n == a:
			break
		y += 1
	if x**n + y**n + z**n == a:
		break
	x += 1
else:
	print('FAIL')