#打开密钥文件，读取密钥

f = open('keyt.txt','r+')

keyt = f.read()

print(keyt)

f.close()

#打开密文文件，读取密文
f = open('ciphertext.txt','r+')

ciphertext = f.read()

print(ciphertext)

f.close()

#对密文和密钥进行按位异或
for i in range(len(ciphertext)):

    print(chr(ord(ciphertext[i])^ord(keyt[i])),end="")

