import struct
import zlib
import sys

def readpack(fmt, fle):
    return struct.unpack(fmt, fle.read(struct.calcsize(fmt)))

with open(sys.argv[1], "br") as f:
    smth_useless = readpack("4c", f)
    file_size = readpack("I", f)
    smth_useless = readpack("8cI", f)
    data_type = readpack("H", f)
    channels_num = readpack("H", f)
    sample_rate = readpack("I", f)
    smth_useless = readpack("IH", f)
    bits_in_sample = readpack("H", f)
    smth_useless = readpack("4c", f)
    data_size = readpack("I", f)
    print('Size=', file_size[0], ', Type=', data_type[0],
    	  ', Channels=', channels_num[0], ', Rate=', sample_rate[0],
    	  ', Bits=', bits_in_sample[0], ', Data size=', data_size[0], sep='')