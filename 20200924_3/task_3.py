s = input()
l = []
while s:
	l.append(s)
	s = input()
for i in enumerate(l):
	unique = True
	for j in enumerate(l):
		if (i != j) and (set(i[1]) & set(j[1])):
			unique = False
	if unique:
		print(i[1])