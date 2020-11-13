while True:
	try:
		v1, v2, v3 = eval(input())
		print(v1,v2,v3)
		area = (v1[0]*v2[1] + v2[0]*v3[1] + v3[0]*v1[1] - v2[0]*v1[1] - v3[0]*v2[1] - v1[0]*v3[1])/2
		if area <= 0:
			raise Exception()
		print('Area:', area)
		break
	except:
		print('Input normal tops.')