import pyfiglet


def solve(a: float, b: float):
	if a == 0 or b == 0:
		return None
	else:
		return str(-b / a)


def fig(res) -> str:
	f = pyfiglet.Figlet()
	if res is None:
		return f.renderText("NO ROOTS")
	return f.renderText(f"Root: {res}")