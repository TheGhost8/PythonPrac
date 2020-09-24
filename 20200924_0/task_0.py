for i in range(3, 7):
	for j in range(3, 7):
		print(i, ' * ', j, ' = ', i*j, '    ', end='') if i * j != 6 else print(i, ' * ', j, ' = :3=', '    ', end='')
		if i*j < 10:
			print(' ', end='')
	print() 