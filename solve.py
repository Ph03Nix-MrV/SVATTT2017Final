from Crypto.Util.number import long_to_bytes
def transform(byte, n):
    return (byte >> n) | ((byte & (((3 * (n * 2 + 1) & 1) << n) - (7 * (n * 2 + 1) & 1))) << (size - n))
def process(FLAG):
    flag = int(FLAG.encode('hex'), 16)
    flag = bin(flag).lstrip('0b')
    FLAG = []
    for i in range(0, len(flag), size):
        FLAG.append(int(flag[i:i + size], 2))
    return FLAG

size = 9
arr=[361, 293, 84, 138, 197, 419, 189, 404, 216, 177, 383, 432, 344, 366, 87, 273, 419, 229, 254, 225, 349, 438, 140, 205, 107, 498, 163, 249, 206, 220, 105, 311, 315, 475, 44, 55, 355, 261, 434, 216, 249, 303, 60, 150, 493, 19, 291, 297, 184, 220, 206, 360, 303, 218, 301, 390, 343, 411, 420, 416, 70, 288, 400, 335]

A=[]
for i in range(64):
  for j in range(512):
    x = transform(j, i % size)
    x = transform(x, (i + 3) % size)
    if x == arr[i]:
      A.append(j)

s=''
for i in A[:-1]:
  tmp = bin(i)[2:]
  if len(tmp) < size:
    tmp = '0'*(size-len(tmp)) + tmp
  s+=tmp

print 'case 1: ',long_to_bytes(int(s+bin(A[-1])[2:],2))
print 'case 2: ',long_to_bytes(int(s+'0'+bin(A[-1])[2:],2))
print 'case 3: ',long_to_bytes(int(s+'00'+bin(A[-1])[2:],2))
