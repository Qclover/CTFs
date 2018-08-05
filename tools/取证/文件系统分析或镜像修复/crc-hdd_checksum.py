import binascii
file = open('CTF.hdd', 'rb')
content = file.read()
checksum = 0
for i in range(0, 11*512):
if i == 106 or i == 107 or i == 112:
continue
checksum = (((checksum << 31) & int('0xFFFFFFFF', 16)) | (checksum >> 1))+int(binascii.b2a_hex(content[i]),16)
print(hex(checksum))