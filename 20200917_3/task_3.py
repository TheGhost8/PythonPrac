i = 3
while i <= 6:
	j = 3
	while j <= 6:
		print(i, ' * ', j, ' = ', i*j, '    ', end='') if i * j != 6 else print(i, ' * ', j, ' = :3=', '    ', end='')
		j += 1
	print()
	i += 1