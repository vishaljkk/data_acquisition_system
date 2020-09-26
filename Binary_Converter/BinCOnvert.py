
import struct

def bin2float(b):
    h = int(b, 2).to_bytes(8, byteorder="big")
    #print(h)
    return struct.unpack('>d', h)[0]


def float2bin(f):
    [d] = struct.unpack(">Q", struct.pack(">d", f))
    #print(f'{d:064b}')
    return f'{d:064b}'

f=open("binfile.bin","wb")
num=float2bin(4.507560559501571e-19)
k=' '
f.write(num.encode())
f.write(k.encode())
f.write(num.encode())
f.write(k.encode())
f.write(num.encode())
f.write(k.encode())
f.close()

f=open("binfile.bin","r")
num=f.read().split(' ')
#print(num.split(' '))
print(bin2float(num[0]))
print(bin2float(num[1]))
print(bin2float(num[2]))
f.close()

