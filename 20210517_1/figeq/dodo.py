def task_png():
	'''Create png file'''
	return{
			"file_dep": ['test.dia'],
			"actions": ['dia test.dia -e test.png'],
			"targets": ['test.png'],
	}

def task_icon():
	'''Create icon file'''
	return{
			"file_dep": ['test.png'],
			"actions": ['convert test.png -resize 64 test-icon.png'],
			"targets": ['test-icon.png'],
	}

def task_icon():
	'''Remove all trash'''
	return{
			"actions": ['rm -f *.png *~'],
	}