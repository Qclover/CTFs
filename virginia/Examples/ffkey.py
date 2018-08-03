import operator

twoCipher = []

ciphertext = ""

keylen = ""

thiskey = ""

fridnum = {
        'a':0.08167,'b':0.01492,'c':0.02782,'d':0.04253,
        'e':0.12702,'f':0.02228,'g':0.02015,'h':0.06094,
        'i':0.06966,'j':0.00153,'k':0.00772,'l':0.04025,
        'm':0.02406,'n':0.06749,'o':0.07507,'p':0.01929,
        'q':0.00095,'r':0.05987,'s':0.06327,'t':0.09056,
        'u':0.02758,'v':0.00978,'w':0.02360,'x':0.00150,
        'y':0.01974,'z':0.00074,
        }

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
        'a':'1010',
        'b':'1011',
        'c':'1100',
        'd':'1101',
        'e':'1110',
        'f':'1111',
        }



def Scanf():
    
    global ciphertext,keylen

    ciphertext = input("请输入密文:")

    keylen = int(input("请输入密文长度:"))
        
    ciphertext = ciphertext.lower()


def returntenum(nowstring):

    nowbin = ""

    nowten = 0

    for i in nowstring:

        nowbin += binstr[i]

    for i in range(8):

        nowten = nowten + int(nowbin[i])*(2**(7-i))

    return(nowten)



def getkey(nowDic,nowlen):

    print("------------------------------")

    print(nowDic)

    print("------------------------------")
    
    alphdic = {}

    machtmp = []

    for i in fridnum:

        alphdic[i] = round(fridnum[i] * nowlen)

    print(alphdic)

    print("-----------------------------")


    for i in range(3,int(nowlen*fridnum['e'])+1):

        for  j in nowDic:

            if (i-2)<=nowDic[j]<=(i+2):

                for k in alphdic:

                    if (i-2)<=alphdic[k]<=(i+2):

                       machtmp.append(returntenum(j) ^ ord(k))

    newmachdic = {}

    for i in machtmp:

        newmachdic[i] = 0

    for i in machtmp:

        newmachdic[i] += 1 

    newmachdic_t = sorted(newmachdic.items(),key=operator.itemgetter(1),reverse = True)

    print("因子:次数")

    count_dic = 0

    for i,j in newmachdic_t:

        print("%3d:%3d"%(i,j))

        count_dic += 1

        if count_dic >= 5:

            break









def FreqAnaly(nowList): #频率分析
    
    nowDic = {}

    for i in nowList:
        
        nowDic[i] = 0

    for i in nowList:

        nowDic[i] += 1
    
   # print(nowDic)
    
    for i in nowDic:

        print("%s:%s"%(i,nowDic[i]*'█'))

    getkey(nowDic,len(nowList))


def madeToTwo():

    global twoCipher
 
    for  i in range(len(ciphertext)//2):
        
        twoCipher.append(ciphertext[i*2:i*2+2])

    print(twoCipher)

def StrSplit():

    for i in range(keylen):

        FreqAnaly(twoCipher[i::keylen])

        print("----------")


def main():

    Scanf()
    
    madeToTwo()

    StrSplit()





if "__main__" == __name__:

    main()
