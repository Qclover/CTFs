print("传统凯撒加密，需要注意的是\n此处为向前移动，字母表为普通顺序")

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("凯撒密码破解，会显示密钥")

ciphertext = input("请输入要破解的密码:")

for i in range(1,26):

    print (i,end=":")

    for j in ciphertext:

        print (alphabet[alphabet.find(j)-i-1],end="")

    print("")

