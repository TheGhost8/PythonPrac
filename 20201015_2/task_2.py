from random import *
length = (int)(input())
glas = ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']
sogl = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']
password = ""
while len(password) < length:
	slog = ['Г','ГС','СГ'][randint(0,2)]
	for i in slog:
		if i == 'Г':
			password += glas[randint(0,len(glas)-1)]
		elif i == 'С':
			password += sogl[randint(0,len(sogl)-1)]
print(password)