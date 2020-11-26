import sys

data = sys.stdin.buffer.read()
print(data)
print(type(data[0]))
port_num = int(data[0])
data = data[1:]
print(port_num)
print(data)

chunks = []
port_size = len(data)//port_num

for i in range(port_num):
	chunks.append(data[i*port_size:(i+1)*port_size])

chunks.sort()

for i in chunks:
	sys.stdout.buffer.write(i)