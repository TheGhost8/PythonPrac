def BinarySearch(x, seq):
	if seq[round(len(seq)/2)-1] == x:
		return True
	elif len(seq) == 1:
		return False
	elif seq[round(len(seq)/2)-1] > x:
		return BinarySearch(x, seq[0:round(len(seq)/2)])
	else:
		return BinarySearch(x, seq[round(len(seq)/2):len(seq)])

a, b = eval(input())
print(BinarySearch(a, b))