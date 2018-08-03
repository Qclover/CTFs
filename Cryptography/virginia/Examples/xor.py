twoCipher = []
binstr = {
        '0':'0000',
        '1':'0001',
        '2':'0010',
        '3':'0011',
        '4':'0100',
        '5':'0101',
        '6':'0110',
        '7':'0111',
        '8':'1000',
        '9':'1001',
        'A':'1010',
        'B':'1011',
        'C':'1100',
        'D':'1101',
        'E':'1110',
        'F':'1111',
        }

def returntenum(nowstring):

    nowbin = ""

    nowten = 0

    for i in nowstring:

        nowbin += binstr[i]

    for i in range(8):

        nowten = nowten + int(nowbin[i])*(2**(7-i))

    return(nowten)

def madeToTwo():

    global twoCipher
 
    for  i in range(len(ciphertext)//2):
        
        twoCipher.append(ciphertext[i*2:i*2+2])

    print(twoCipher)


ciphertext = input("请输入密文:")

password = input("请输入密码:")

madeToTwo()

passlist = password.split(',')

print(passlist)

password = ""

for i in passlist:

    password += chr(int(i))


for i in range(len(twoCipher)):

    cc = returntenum(twoCipher[i]) ^ ord(password[i%7])

    print(chr(cc),end="")


print("")

