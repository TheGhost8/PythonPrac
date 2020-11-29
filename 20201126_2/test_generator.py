import sys

text = sys.stdin.read()

print(text.encode('CP1251').decode('latin1'))