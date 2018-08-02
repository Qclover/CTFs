import devirginia
import operator
import re

ciphertext = "" # 密文字符串

kasNum = "" #相同字母的大小，这个可以设置，其实就是明文中可能出现相同单词的长度

kasialp = {} #这个是用来记录相同的单词，并记录下间距

kasfac = {} #根据间距计算出了 所有可能的公因子

passnum = {} #对共因子进行处理 统计 ，最终显示的就是这个字典

def Scanf():

    global ciphertext,kasNum

    ciphertext = input("请输入密文:")

    kasNum = input("请输入最短相似长度（一般为3或4或更长）")

    print("如果没有找到相似字符串，请降低最短相似长度\n如果没有找到相同公因子，请增加最短相似长度")


def FindStr():

    for i in range(len(ciphertext)-int(kasNum)):

        a = [first.start() for first in re.finditer(ciphertext[i:i+int(kasNum)], ciphertext)]
        
        if len(a) > 1 :
            
            for j in kasialp:

                if j == ciphertext[i:i+int(kasNum)]:

                    continue

            kasialp[ciphertext[i:i+int(kasNum)]] = a[1] - a[0]
    
    print(kasialp)

def SeekFac(name,num):

    #没有写1 是因为1是不可能出现，密钥长度为1说明是凯撒


    kasfac[name] = set()

    for i in range(num):

        for j in range(num):

            if i*j == num :

                kasfac[name].add(i)

                kasfac[name].add(j)
   
def Handle():

    for i in kasialp:

        SeekFac(i,kasialp[i])

        print("%s:%s"%(i,kasfac[i]))

        for j in kasfac[i]:

            passnum[j] = 0
    
    print("----------------------------------------")

    print("统计密钥长度可能性:")

    for i in kasialp:

        for j in kasfac[i]:

            passnum[j] += 1

    passnum_t = sorted(passnum.items(),key=operator.itemgetter(1),reverse = True)

    print("因子:次数")
    for i,j in passnum_t:

        print("%3d:%3d"%(i,j))

def main():

    Scanf()
    
    FindStr()

    Handle()    

if "__main__" == __name__:

    main()
