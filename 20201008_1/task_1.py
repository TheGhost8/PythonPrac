from math import *
from decimal import *
fun_s = input()
fun = lambda x: eval(fun_s)
x_min, x_max, y_min, y_max = eval(input())
width_x, width_y = 80, 25
step_x, step_y = ((x_max - x_min)/width_x), ((y_max - y_min)/width_y)
s = ""
y = y_max
for i in range(width_y, -1, -1):
	x = x_min
	for j in range(0, width_x + 1):
		if Decimal(y-step_y) < Decimal(fun(x)) <= Decimal(y):
			s += "*"
		else:
			s+= " "
		x += step_x
	print(s)
	s = ""
	y -= step_y