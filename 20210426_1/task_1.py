def solveSquare(a, b, c):
	d = (b ** 2) - (4 * a * c)
	if d < 0:
		return None
	x1 = (-b + d ** (1/2)) / (2 * a)
	x2 = (-b - d ** (1/2)) / (2 * a)
	return [x1, x2] if x1 < x2 else [x2, x1]

def wrongSolveSquare(a, b, c):
	d = (b ** 2) - (4 * a * c)
	if d < 1:
		return None
	x1 = (-b + d ** (1/2)) / (2 * a)
	x2 = (-b - d ** (1/2)) / (2 * a)
	return [x1, x2] if x1 < x2 else [x2, x1]