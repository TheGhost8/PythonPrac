import fractions
val = eval(input())
s = fractions.Fraction(val[0])
w = fractions.Fraction(val[1])
A = 0
for i in range(val[2],-1,-1):
	A += fractions.Fraction(s**i) * fractions.Fraction(val[2+val[2]-i+1])
B = 0
for i in range(val[2+val[2]+2],-1,-1):
	B += fractions.Fraction(s**i) * fractions.Fraction(val[2+val[2]+2+val[2+val[2]+2]-i+1])
print(A == w*B)