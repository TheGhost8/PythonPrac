a = eval(input())
sum = 0
while a > 0:
	sum += a
	if sum > 21:
		print(sum)
		break
	a = eval(input())
else:
	print(a)