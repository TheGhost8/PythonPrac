n, m = eval(input())
str_length = len(str(n)) + 3 + len(str(n)) + 3 + len(str(n*n))
table_width = 0
i = 1
print(str_length)
while ((str_length + 2) * i) <= m:
	table_width = (str_length + 2) * i
	i += 1
number_of_columns = (int)(table_width/str_length)

for i in range(1, n+1, number_of_columns):
	print('=' * m)
	for j in range(1, n+1):
		s = ""
		for k in range(number_of_columns):
			if i+k > n:
				break
			s += "{0:{align}{width}}".format(i+k, width=len(str(n)), align='>')
			s += " * "
			s += "{0:{align}{width}}".format(j, width=len(str(n)), align='<')
			s += " = "
			s += "{0:{align}{width}}".format((i+k)*j, width=len(str(n*n)), align='<')
			s += " "
			if k == number_of_columns-1:
				s += " "
			elif (i+k+1) <= n:
				s += "| "
		print(s)
print('=' * m)