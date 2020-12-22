import asyncio
src = eval(input())
#print(src)

tmp = src.copy()
features = {}

async def merge(from1, to1, to2):
	features[from1, to2] = asyncio.Future()
	if to1-from1 > 1:
		await features[from1, to1]
	if to2-to1 > 1:
		await  features[to1, to2]
	i1, i2 = from1, to1
	i = from1
	for i in range(from1, to2):
		#await asyncio.sleep(0.2)
		#print(from1, to2)
		if i1 < to1 and i2 < to2:
			if src[i1] < src[i2]:
				tmp[i] = src[i1]
				i1 += 1
			else:
				tmp[i] = src[i2]
				i2 += 1
		elif i1 < to1:
			tmp[i] = src[i1]
			i1 += 1
		else:
			tmp[i] = src[i2]
			i2 += 1
	src[from1:to2] = tmp[from1:to2]
	features[from1, to2].set_result(True)

async def main():
	tasks = []
	for i in range(0,16,2):
		tasks.append(asyncio.create_task(merge(i, i+1, i+2)))
	#await asyncio.gather(*tasks)
	#tasks.clear()

	for i in range(0,16,4):
		tasks.append(asyncio.create_task(merge(i, i+2, i+4)))
	#await asyncio.gather(*tasks)
	#tasks.clear()

	for i in range(0,16,8):
		tasks.append(asyncio.create_task(merge(i, i+4, i+8)))
	#await asyncio.gather(*tasks)
	#tasks.clear()

	tasks.append(asyncio.create_task(merge(0, 8, 16)))

	await asyncio.gather(*tasks)

asyncio.run(main())
print(src)