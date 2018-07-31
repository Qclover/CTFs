alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def enbase(strlist):

    strflag = ""

    temp = ord(strlist[0]) >> 2

    strflag += alphabet[temp]

    temp = ((ord(strlist[0])&3)<<4)|(ord(strlist[1])>>4)

    strflag += alphabet[temp]

    temp = ((ord(strlist[1])&15)<<2)|(ord(strlist[2])>>6)

    strflag += alphabet[temp]

    temp = (ord(strlist[2])&63)

    strflag += alphabet[temp]
    
    return strflag

def main():

    charString = input ("请输入要转换的字符串:")

    for i in range(len(charString)//3):

       print(enbase(charString[i*3:i*3+3]),end="")

    if len(charString)%3!=0:

        if len(charString)%3 == 1:

            print(enbase(charString[-1:]+chr(0)+chr(0))[:2]+"==")

        if len(charString)%3 == 2:

            print(enbase(charString[-2:]+chr(0))[:3]+'=')
    



if '__main__' == __name__:

    main()


