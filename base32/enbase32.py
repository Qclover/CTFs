alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"

def enbase(strlist):

    strflag = ""

    temp = ord(strlist[0])>>3

    strflag += alphabet[temp]

    temp = ((ord(strlist[0])&7)<<2)|(ord(strlist[1])>>6)

    strflag += alphabet[temp]

    temp = ((ord(strlist[1])&62)>>1)

    strflag += alphabet[temp]

    temp = ((ord(strlist[1])&1)<<4)|(ord(strlist[2])>>4)

    strflag += alphabet[temp]

    temp = ((ord(strlist[2])&15)<<1)|(ord(strlist[3])>>7)

    strflag += alphabet[temp]

    temp = (ord(strlist[3])&124)>>2
    
    strflag += alphabet[temp]

    temp = ((ord(strlist[3])&3)<<3)|((ord(strlist[4])&224)>>5)

    strflag += alphabet[temp]

    temp = ord(strlist[4])&31

    strflag += alphabet[temp]
    
    return strflag

def main():

    charString = input ("请输入要转换的字符串:")

    for i in range(len(charString)//5):

       print(enbase(charString[i*5:i*5+5]),end="")

 
    if len(charString)%5!=0:

        if len(charString)%5 == 1:

            print(enbase(charString[-1:]+chr(0)+chr(0)+chr(0)+chr(0))[:2]+"======")

        if len(charString)%5 == 2:

            print(enbase(charString[-2:]+chr(0)+chr(0)+chr(0))[:4]+"====")
    
        if len(charString)%5 == 3:

            print(enbase(charString[-3:]+chr(0)+chr(0))[:5]+"===")

        if len(charString)%5 == 4:

            print(enbase(charString[-4:]+chr(0))[:7]+'=')
        
    print("")


if '__main__' == __name__:

    main()


