from struct import *
from random import uniform, randint

f = open("o",)

for i in range(10):
	f.write(pack(uniform(0.,1.), randint(0,10)))