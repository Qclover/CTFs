#
#    Date:2018-07-29
#   Time:07:50 GMT
#  Author:nianhua
#
#此文件用来计算费纳姆密码，或解密费纳姆密码

def TurnBinary(turNum):
    "将传入的turNum数值类型转化为7位的二进制字符串返回"
    
    if 0 < turNum < 128:
    
        strbin = []

        for i in range(7):

            turNum,remainder = divmod(turNum,2)
        
            strbin.append(str(remainder))
         
        return(''.join(strbin[::-1]))
    
    else:
        #数值超出范围
        
        return "*******"
        
        print("not ok")

def CharacterProcessing(cryStr):

    proceStr = ""

    for i in cryStr:

        proceStr +=  TurnBinary(ord(i))

    return proceStr

def BOX(strA,strB):
    "会判断A和B的长度是否相同，但仅仅会提示一下，随后按照最短的遍历"

    loopNum = 0
    strC = ""

    if len(strA) != len(strB):

        print ("我擦，小伙子这俩个字符串不一样长啊，要不要检查一下!")
    
        if len(strA) < len(strB):

            loopNum = len(strA)

        else:

            loopNum = len(strB)

    else:

        loopNum = len(strA)


    for i in range(loopNum):

        if strA[i] == strB[i]:
            
            strC =  strC + '0'
        
        else:

            strC = strC + '1'


    print("解密/加密后的二进制:")
    
    print('-'*loopNum)

    print (strC)

    print('-'*loopNum)

    print('尝试转换为ASCII可见字符:')

    for i in range(loopNum//7):

        num = 0

        char = strC[i*7:(i+1)*7]

        for j in range(7) : #这里用range而不用char是因为这样处理更方便

            num += int(char[j])*(2**(6-j))
            
        print(chr(num),end='')

    print("")


def main():

    ciphertext = input ("请输入明文或密文:")

    cryptogram = input ("请输入密码:")

    #print(CharacterProcessing(cryptogram))
    
    #BOX(ciphertext,CharacterProcessing(cryptogram))

    #判断是加密还是解密
    #条件是：如果第一个输入的是二进制，则为解密。
    #        如果第一个输入的是字母，则为加密。
    #        判断的有点粗糙。
    #        原则上，费纳姆密码只能加密字母。

    if '1' in ciphertext:

        BOX(ciphertext,CharacterProcessing(cryptogram))

    else:

        BOX(CharacterProcessing(ciphertext),CharacterProcessing(cryptogram))

if '__main__' == __name__ :

    main()





