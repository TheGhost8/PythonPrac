s1 = input()
B = False
for p in enumerate(s1):
	if p[1] in ('A', 'B', 'C'):
		if B:
			print(p)
		if p[1] == 'B':
			B = True
		else:
			B = False
	elif B and (p[0] == len(s1) - 1):
		print(p)