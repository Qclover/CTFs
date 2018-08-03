
#字母表/明文/密钥
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

plaintext = ""

keyt = ""

def Scanf():

    global plaintext,keyt

    plaintext = input("请输入明文(全大写):")

    keyt = input("请输入密钥:")


def AlphaMove(alpha,drift):

    return(alphabet[(alphabet.find(alpha)+drift)%26])


def EnCryption():

    for i in range(len(plaintext)):

        print (AlphaMove(plaintext[i],alphabet.find(keyt[i%len(keyt)])),end="")
    
    print("")


def main():

    Scanf()
    
    EnCryption()


if "__main__" == __name__:

    main()




