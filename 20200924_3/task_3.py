s = input()
l = []
while s:
	l.append(s)
	s = input()
for i in range(len(l)):
	unique = True
	for j in range(len(l)):
		if (i != j) and (set(l[i]) & set(l[j])):
			unique = False
	if unique:
		print(l[i])