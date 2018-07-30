###
###    Date:2018-07-30
###   Time:03:33 GMT
###  Author:nianhua
###

````
File enbase32.py
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
  annotation:The main purpose is to solve the malformed base encryption

File debase32.py
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
  annotation:The main purpose is to solve the malformed base encryption

---------------------------------------------------------------------------------
Program output：
---------------------------------------------------------------------------------

└──╼ $python3 enbase32.py 
请输入要转换的字符串:abcdefghijk
MFRGGZDFMZTWQ2LKNM======

---------------------------------------------------------------------------------

└──╼ $python3 debase32.py 
请输入base32加密后的数据:MFRGGZDFMZTWQ2LKNM======
abcdefghijk

Some places to pay attention to：
  alphabet is variable, But it needs to be consistent. 
````




