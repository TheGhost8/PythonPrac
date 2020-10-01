def Calc(s, t, u):
	def S(x):
		return eval(s)
	def T(x):
		return eval(t)
	def U(x, y):
		return eval(u)
	def Res(x):
		return U(S(x), T(x))
	return Res

Fun = Calc(input(), input(), input())
print(Fun(1), Fun(2))