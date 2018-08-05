#--*coding:utf-8--*--
#Author=Qclover-Guangnian
def change(c,i):
    c = c.lower()
    num = ord(c)
    if num >= 97 and num <= 122:
        num = 97 + ((num - 97) + i) % 26
    return chr(num)


def kaisa_jiami(string,i):
    string_new = ''
    for s in string:
        string_new += change(s,i)
    print(string_new)
    return string_new

def kaisa_jiemi(string):
    for i in range(25):
        print('\n', i, '\n')
        i += 1
        kaisa_jiami(string,i)


def main():
    print('请选择需要的操作：')
    print('1：凯撒加密')
    print('2：凯撒解密')
    choice = input()
    if choice == '1':
        string = input('请输入需要加密的字符串：')
        num = int(input('请输入需要偏移的位数：'))
        kaisa_jiami(string,num)
    elif choice == '2':
        string = input('请输入需要解密的字符串：')
        kaisa_jiemi(string)
    else:
        print('输入错误，请重试！')
        main()

if __name__ == '__main__':
    main()
