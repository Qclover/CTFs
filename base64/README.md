###
###    Date:2018-07-31
###   Time:14:47 GMT
###  Author:nianhua
###

````
File enbase64.py
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
  annotation:The main purpose is to solve the malformed base encryption

File debase64.py
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
  annotation:The main purpose is to solve the malformed base encryption

---------------------------------------------------------------------------------
Program output：
---------------------------------------------------------------------------------

└──╼ $python3 enbase64.py
请输入要转换的字符串:nian-hua  
bmlhbi1odWE=

---------------------------------------------------------------------------------

└──╼ $python3 debase64.py 
请输入base64加密后的数据:bmlhbi1odWE=
nian-hua

Some places to pay attention to：
  alphabet is variable, But it needs to be consistent. 
  Although there are many base64/base32 programs, this program can set the alphabet by itself. I think this is the best place.
````




