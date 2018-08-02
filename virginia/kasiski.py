#转载请注明出处哦~~~~
#https://github.com/nian-hua/
import devirginia
import operator
import re

ciphertext = "" # 密文字符串

kasNum = "" #相同字母的大小，这个可以设置，其实就是明文中可能出现相同单词的长度

kasialp = {} #这个是用来记录相同的单词，并记录下间距

kasfac = {} #根据间距计算出了 所有可能的公因子

passnum = {} #对共因子进行处理 统计 ，最终显示的就是这个字典

#用来输入的函数····这个看看就好。
def Scanf():

    global ciphertext,kasNum

    ciphertext = input("请输入密文:")

    kasNum = input("请输入最短相似长度（一般为3或4或更长）")

    print("如果没有找到相似字符串，请降低最短相似长度\n如果没有找到相同公因子，请增加最短相似长度")

#FindStr函数是用来检索相同字符串的
def FindStr():

    for i in range(len(ciphertext)-int(kasNum)):        #kasNum是相同字母大小，也就是循环(总密文-相同字母大小)次

        a = [first.start() for first in re.finditer(ciphertext[i:i+int(kasNum)], ciphertext)]   #从当前选取kasNum个字符，使用re模块检索，返回一个数组(数组包含每个检索到的字符串下表)
        
        if len(a) > 1 :         #如果检索到大于一个相同的字符串
            
            for j in kasialp:       #遍历kasialp集合

                if j == ciphertext[i:i+int(kasNum)]:    #如果集合中已经有了这个字符串，那么就跳过(其实我觉得如果在re之前先判断一下，程序的复杂度会更低)

                    continue

            kasialp[ciphertext[i:i+int(kasNum)]] = a[1] - a[0]      #集合中没有这个字符串，将其存入集合
    
    print(kasialp)      #打印出来看一看哈哈哈哈

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
