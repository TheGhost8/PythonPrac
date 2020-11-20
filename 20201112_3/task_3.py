while True:
	try:
		v1, v2, v3 = eval(input())
		x1, y1, x2, y2, x3, y3 = v1[0], v1[1], v2[0], v2[1], v3[0], v3[1]
		area = abs(x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3)/2
		if area <= 0:
			raise ValueError('WrongTriangle')
		print("{0:.2f}".format(area))
		break
	except (ValueError, NameError, TypeError) as e:
		if str(e) == 'WrongTriangle':
			print('Not a triangle')
		else:
			print('Invalid input')