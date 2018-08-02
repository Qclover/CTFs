
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ciphertext = ""

keyt = ""

def Scanf():

    global ciphertext,keyt

    ciphertext = input("请输入密文:")

    keyt = input("请输入密钥:")

def AlphaMove(alpha,drift):

    return(alphabet[(alphabet.find(alpha)+drift)%26])

def Decryption():

    for i in range(len(ciphertext)):

        print (AlphaMove(ciphertext[i],0-alphabet.find(keyt[i%len(keyt)])),end="")

    print("")


def main():

    Scanf()

    Decryption()

if "__main__" == __name__ :

    main()
