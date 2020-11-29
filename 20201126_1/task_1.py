import sys

data = sys.stdin.buffer.read()
port_num = int(data[0])
data = data[1:]

chunks = []
for i in range(port_num):
	chunks.append(data[i*len(data)//port_num:(i+1)*len(data)//port_num])

chunks.sort()
chunks.insert(0, bytes([port_num]))

for i in chunks:
	sys.stdout.buffer.write(i)