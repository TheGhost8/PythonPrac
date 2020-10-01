def DominatingPair(a, b):
	return (a[0] >= b[0]) and (a[1] >= b[1]) and ((a[0] > b[0]) or (a[1] > b[1]))

def Pareto(l_pair):
	out_p = []
	for p in l_pair:
		if out_p:
			add = True
			for k in out_p:
				if DominatingPair(p, k):
					out_p.remove(k)
				elif DominatingPair(k, p):
					add = False
			if add:
				out_p.append(p)
		else:
			out_p.append(p)
	return out_p
	

l = eval(input())
print(Pareto(l))