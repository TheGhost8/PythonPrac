val = int(input())
print('A+', end='') if (val % 2 == 0) and (val % 25 == 0) else print('A-', end='')
print('B+', end='') if (val % 2 == 1) and (val % 25 == 0) else print('B-', end='')
print('C+') if val % 8 == 0 else print('C-')