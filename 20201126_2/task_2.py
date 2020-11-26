import sys

text = sys.argv[1]

print(text.decode('latin1').decode('CP1251'))