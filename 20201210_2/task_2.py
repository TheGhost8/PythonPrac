import asyncio
src = eval(input())
length = len(src)

tmp = src.copy()
features = {}
massives = {}

async def merge(from1, to1, to2):
	if to2 - from1 <= 1:
		massives[from1, to2] = [src[from1]]
		return
	features[from1, to2] = asyncio.Future()
	if to1-from1 > 1:
		await features[from1, to1]
	if to2-to1 > 1:
		await  features[to1, to2]
	start_massive = []
	sorted_massive = []
	if to2 - from1 == 2:
		start_massive = src[from1:to2]
	else:
		start_massive = massives[from1, to1] + massives[to1, to2]
	sorted_massive = start_massive.copy()
	i1, i2 = 0, to1-from1
	i = from1
	for i in range(0, to2-from1):
		#print(from1, to2)
		if i1 < (to1-from1) and (i2 < to2-from1):
			if start_massive[i1] < start_massive[i2]:
				sorted_massive[i] = start_massive[i1]
				i1 += 1
			else:
				sorted_massive[i] = start_massive[i2]
				i2 += 1
		elif i1 < (to1-from1):
			sorted_massive[i] = start_massive[i1]
			i1 += 1
		else:
			sorted_massive[i] = start_massive[i2]
			i2 += 1
	massives[from1, to2] = sorted_massive
	features[from1, to2].set_result(True)

async def main():
	tasks = []
	j = 2
	while j <= length:
		for i in range(0, length, j):
			if i+j//2 >= length:
				tasks.append(asyncio.create_task(merge(i, i+(length-i)//2, length)))
			elif i+j >= length:
				tasks.append(asyncio.create_task(merge(i, i+j//2, length)))
			else:
				tasks.append(asyncio.create_task(merge(i, i+j//2, i+j)))
		j *= 2
	if length > 0 and j//2 != length:
		tasks.append(asyncio.create_task(merge(0, j//2, length)))
	elif length == 0 or length == 1:
		return

	await asyncio.gather(*tasks)
	src[0: length] = massives[0, length][0: length]

asyncio.run(main())
print(src)