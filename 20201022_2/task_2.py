def even(seq):
	for i in seq:
		if i % 2 == 0:
			yield i

def slide(seq):
	seq = iter(seq)
	while True:
		s, seq = tee(seq, 2)
		win = list(islice(s,3))
		if len(win) < 3:
			return
		yield from even(win)
		next(seq)

s = eval(input())
for i, k in enumerate(slide(s)):
	print(k)