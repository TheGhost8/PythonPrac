class nestr(str):
	def __pos__(self):
		return nestr(self)

	def __neg__(self):
		return nestr(self[::-1])

	def __add__(self, other):
		return nestr(str(self) + str(other))

	def __mul__(self, coef):
		return nestr(str(self) * coef)

print(eval(input()))