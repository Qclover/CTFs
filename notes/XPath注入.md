##  0x01 简介 

 XPath注入攻击是指利用XPath 解析器的松散输入和容错特性，能够在 URL、表单或其它信息上附带恶意的XPath  查询代码，以获得权限信息的访问权并更改这些信息。XPath注入发生在当站点使用用户输入的信息来构造请求以获取XML数据。攻击者对站点发送经过特殊构造的信息来探究站点使用的XML是如何构造的，从而进一步获取正常途径下无法获取的数据。当XML数据被用作账户验证时，攻击者还可以提升他的权限。 

##  0x02 原理 

 XPath 注入的原理与sql注入大体类似。主要是通过构建特殊的输入，这些输入往往是XPath语法中的一些组合，这些输入将作为参数传入Web  应用程序，通过执行XPath查询而执行入侵者想要的操作。但是，注入的对象不是数据库users表了，而是一个存储数据的XML文件。因为xpath不存在访问控制，所以我们不会遇到许多在SQL注入中经常遇到的访问限制。  注入出现的位置也就是`cookie`，`headers`，`request parameters/input`等。 例如： 

```
<?xml version="1.0" encoding="UTF-8"?> <users> <user> <firstname>Ben</firstname> <lastname>Elmore</lastname> <loginID>abc</loginID> <password>test123</password> </user> <user> <firstname>Shlomy</firstname> <lastname>Gantz</lastname> <loginID>xyz</loginID> <password>123test</password> </user> <user> <firstname>Jeghis</firstname> <lastname>Katz</lastname> <loginID>mrj</loginID> <password>jk2468</password> </user> <user> <firstname>Darien</firstname> <lastname>Heap</lastname> <loginID>drano</loginID> <password>2mne8s</password> </user> </users>
```

 正常查询`//users/user[loginID/text()='xyz'and password/text()='123test']`,如果黑客在 `loginID` 字段中输入：`' or 1=1 or ''='` 则变成`//users/user[loginID/text()=''or 1=1 or ''='' and password/text()='' or 1=1 or ''='']`，成功获取所有`user`数据，然后攻击者完成登录可以再通过XPath盲入技术获取最高权限帐号和其它重要文档信息。 

##  0x03 利用 

 如果一个网站某应用程序将数据保存在XML中，并且对用户的输入没有做限制，攻击者提交了没有经过处理的输入，就插入到 XPath 查询中，即产生Xpath注入，那么就攻击者就可能通过控制查询，获取数据，或者删除数据之类的操作。 

 Xpath是xml路径语言，用于配置文件的查找。数据库就是xml文件。因此只要是利用XPath语法的Web 应用程序如果未对输入的XPath查询做严格的处理都会存在XPath注入漏洞。比如一些登录地址页面，搜索页面需要与xml交互的位置。 

 判断依据：主要根据错误信息页面判断以及查看源码进行分析。 

 [![xpath0.jpeg](http://www.webbaozi.com/content/uploadfile/201702/31421487145373.jpeg)](http://www.webbaozi.com/content/uploadfile/201702/31421487145373.jpeg) 

###  Example：Bwapp 

 首先这是这个Get方式请求验证，因此对get的参数进行注入测试，发现报错信息，说明是可能通过xml存储于前端交互。 

 [![xpath1.png](http://www.webbaozi.com/content/uploadfile/201702/241a1487145381.png)](http://www.webbaozi.com/content/uploadfile/201702/241a1487145381.png) 

 然后构造xpath查询语句`//users/user[loginID/text()='' and password/text()='']`,因此`'or 1=1 or ''='`或者`' or '1'='1`等使其为真可以。 

 [![xpath2.png](http://www.webbaozi.com/content/uploadfile/201702/c7541487169140.png)](http://www.webbaozi.com/content/uploadfile/201702/c7541487169140.png) 

###  Example:hctf 

 index.html 

```
<?php
$re = array('and','or','count','select','from','union','group','by','limit','insert','where','order','alter','delete','having','max','min','avg','sum','sqrt','rand','concat','sleep'); setcookie('injection','c3FsaSBpcyBub3QgdGhlIG9ubHkgd2F5IGZvciBpbmplY3Rpb24=',time()+100000); if(file_exists('t3stt3st.xml')) { $xml = simplexml_load_file('t3stt3st.xml'); $user=$_GET['user']; $user=str_replace($re, ' ', $user); // $user=str_replace("'", "&apos", $user); $query="user/username[@name='".$user."']"; $ans = $xml->xpath($query); foreach($ans as $x => $x_value) { echo $x.": " . $x_value; echo "<br />"; } } ?>
```

 t3stt3et.xml 

```
<?xml version="1.0" encoding="utf-8"?> <root1> <user> <username name='user1'>user1</username> <key>KEY:1</key> <username name='user2'>user2</username> <key>KEY:2</key> <username name='user3'>user3</username> <key>KEY:3</key> <username name='user4'>user4</username> <key>KEY:4</key> <username name='user5'>user5</username> <key>KEY:5</key> <username name='user6'>user6</username> <key>KEY:6</key> <username name='user7'>user7</username> <key>KEY:7</key> <username name='user8'>user8</username> <key>KEY:8</key> <username name='user9'>user9</username> <key>KEY:9</key> </user> <hctfadmin> <username name='hctf1'>hctf</username> <key>flag:hctf{Dd0g_fac3_t0_k3yboard233}</key> </hctfadmin> </root1>
```

 通过查看源码`$query`，然后构造payload:` `']|//*|['`` 

##  0x04 危害 

1.  在URL及表单中提交恶意XPath代码，可获取到权限限制数据的访问权，并可修改这些数据； 
2.   可通过此类漏洞查询获取到系统内部完整的XML文档内容。 
3.  逻辑以及认证被绕过，它不像数据库那样有各种权限，xml没有各种权限的概念,正因为没有权限概念，因此利用xpath构造查询的时候整个数据库都会被用户读取。 

##  0x05 防御 

1.  数据提交到服务器上端，在服务端正式处理这批数据之前，对提交数据的合法性进行验证。 
2.  检查提交的数据是否包含特殊字符，对特殊字符进行编码转换或替换、删除敏感字符或字符串。 
3.  对于系统出现的错误信息，以IE错误编码信息替换，屏蔽系统本身的出错信息。 
4.  参数化XPath查询，将需要构建的XPath查询表达式，以变量的形式表示，变量不是可以执行的脚本。 
5.  通过MD5、SSL等加密算法，对于数据敏感信息和在数据传输过程中加密，即使某些非法用户通过非法手法获取数据包，看到的也是加密后的信息。 总结下就是：限制提交非法字符，对输入内容严格检查过滤，参数化XPath查询的变量。 