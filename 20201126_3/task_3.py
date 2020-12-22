import struct
import zlib
import sys

def readpack(fmt, fle):
    return struct.unpack(fmt, fle.read(struct.calcsize(fmt)))

try:
	with open(sys.argv[1], "br") as f:
		smth_useless = ''
		for i in readpack("4c", f):
			smth_useless += i.decode('utf-8')
		if smth_useless != 'RIFF':
			raise NameError
		file_size = readpack("I", f)
		smth_useless = ''
		for i in readpack("4c", f):
			smth_useless += i.decode('utf-8')
		if smth_useless != 'WAVE':
			raise NameError
		smth_useless = ''
		for i in readpack("3c", f):
			smth_useless += i.decode('utf-8')
		if smth_useless != 'fmt':
			raise NameError
		smth_useless = readpack("c", f)[0].decode('utf-8')
		if smth_useless != chr(32):
			raise NameError
		smth_useless = readpack("I", f)
		data_type = readpack("H", f)
		channels_num = readpack("H", f)
		sample_rate = readpack("I", f)
		smth_useless = readpack("IH", f)
		bits_in_sample = readpack("H", f)
		smth_useless = ''
		for i in readpack("4c", f):
			smth_useless += i.decode('utf-8')
		if smth_useless != 'data': 
			raise NameError
		data_size = readpack("I", f)
		print('Size=', file_size[0], ', Type=', data_type[0],
			  ', Channels=', channels_num[0], ', Rate=', sample_rate[0],
			  ', Bits=', bits_in_sample[0], ', Data size=', data_size[0], sep='')
except (IndexError, NameError) as e:
	print('NO')