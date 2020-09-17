import random as rd
values = []
values.append(eval(input()))
for i in range(9): values.append(rd.randint(1,100))
print(values)