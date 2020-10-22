s = input()
s = s.lower()
all_pairs = set()
for i in range(1, len(s)):
	if s[i-1].isalpha() and s[i].isalpha():
		all_pairs.add(s[i-1] + s[i])
print(len(all_pairs))