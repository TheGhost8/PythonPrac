def Substraction(a, b):
	if hasattr(a, "__sub__") and hasattr(b, "__sub__") and (type(a) == type(b)):
		return a-b
	else:
		return type(a)([i for i in a if i not in b])

x, y = eval(input())
print(Substraction(x, y))