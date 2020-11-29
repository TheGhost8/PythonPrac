import sys

data = sys.stdin.buffer.read()
port_num = int(data[0])

chunks = []
for i in range(port_num):
	chunks.append(data[i*len(data)//port_num:(i+1)*len(data)//port_num])

chunks.sort()

for i in chunks:
	sys.stdout.buffer.write(i)