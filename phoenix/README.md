###
###    Date:2018-07-29
###   Time:08:00 GMT
###  Author:nianhua
###

````
Function TurnBinary :
  input(num)
  output(binstr)
  annotation:The num between 1 and 128,the binstr is seven bits
  
Function CharacterProcessing :
  input(crystr)
  output(str<bin>)
  annotation:The str<bin> is a multiplier of 7
  
Function BOX :
  input(strA,strB)
  output(strA^strB)
  annotation:According to the shortest traversal


Sample topic<Thank to P1an019横渡大海会断魂>：

ciphertext:0000011000000000101010110111001011000101100000111001100100111100111001

keyt:helloworld


---------------------------------------------------------------------------------
Program output：
---------------------------------------------------------------------------------
请输入明文或密文:0000011000000000101010110111001011000101100000111001100100111100111001
请输入密码:helloworld
解密/加密后的二进制:
----------------------------------------------------------------------
1101011110010111110011011011111100111000011101000110101111100101011101
----------------------------------------------------------------------
尝试转换为ASCII可见字符:
key[yahkr]
````




