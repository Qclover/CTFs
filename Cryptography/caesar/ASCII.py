print("注意：此程序为使用ASCII码为母表对密文进行移动\n适合于含有字符的密文")
print("因为密文可能有特殊含义的字符，所以需要修改一下源码，在cip里面放入密文!")


ciphertext = '''EOBD.7igq4;741R;1ikR51ibOO0'''


for i in range(0,128):

    print("%3d"%(i),end=":")
    
    for j in ciphertext:

        print(chr((ord(j)+i)%128),end="")

        if ((ord(j)+i)%128)<37:

            break

    print()

