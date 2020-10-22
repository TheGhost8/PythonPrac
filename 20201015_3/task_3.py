from random import *

#a = {'a':1,'b':2}
#print(a[list(a.keys())[1]])

n = (int)(input())
s = input()
all_pairs = {}
while s:
	s = s.lower()
	for i in range(1, len(s)):
		if s[i-1].isalpha() and s[i].isalpha():
			slog = s[i-1] + s[i]
			if slog in all_pairs.keys():
				all_pairs[slog] += 1
			else:
				all_pairs[slog] = 1
	s = input()

password = ""
while len(password) < n:
	password += list(all_pairs.keys())[choices(range(len(all_pairs.keys())), [all_pairs[i] for i in all_pairs])[0]]
	#password += choices(all_pairs.keys(), [all_pairs[i] for i in all_pairs])
print(password)