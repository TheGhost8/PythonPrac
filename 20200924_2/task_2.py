l = eval(input())
sorted = False
while not sorted:
	sorted = True
	for i in range(len(l)-1):
		if (l[i]**2 % 100) > (l[i+1]**2 % 100):
			l[i], l[i+1] = l[i+1], l[i]
			sorted = False
print(l)