alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"

ciphertext = ""


def TenToBin(tenum):

    binstr = ""

    for i in range(4,-1,-1):

        if 1 == (tenum//(2**i)):

            binstr += '1'

            tenum = tenum%(2**i)

        else:

            binstr += '0'

    return binstr

def BinToStr(strbin):
    "Turn the binary string to a ASCII string"

    strten = ""
    
    for i in range(len(strbin)//8):

        num = 0

        test = strbin[i*8:i*8+8]

        for j in range(8):

            num += int(test[j])*(2**(7-j))

        strten += chr(num)

    return strten

def decode(base32string):

    binstr = ""

    for i in base32string:

        binstr += TenToBin(alphabet.find(i))

    print(BinToStr(binstr))


def main():

    global ciphertext

    ciphertext = input("请输入base32加密后的数据:")

    ciphertext = ciphertext.upper()
    
    #自己检查输入有没有问题哈哈
    #长度最好也自己检查一下

    decode(ciphertext)


if "__main__" == __name__:

    main()
