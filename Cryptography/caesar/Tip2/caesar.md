## 概念及原理

根据百度百科上的解释，凯撒密码是一种古老的加密算法。

密码的使用最早可以追溯到古罗马时期，《高卢战记》有描述恺撒曾经使用密码来传递信息，即所谓的“恺撒密码”，它是一种替代密码，通过将字母按顺序推后起3位起到加密作用，如将字母A换作字母D，将字母B换作字母E。因据说恺撒是率先使用加密函的古代将领之一，因此这种加密方法被称为恺撒密码。这是一种简单的加密方法，这种密码的密度是很低的，只需简单地统计字频就可以破译。 现今又叫“移位密码”，只不过移动的为数不一定是3位而已。

密码术可以大致别分为两种，即易位和替换，当然也有两者结合的更复杂的方法。在易位中字母不变，位置改变；替换中字母改变，位置不变。

将替换密码用于军事用途的第一个文件记载是恺撒著的《高卢记》。恺撒描述了他如何将密信送到正处在被围困、濒临投降的西塞罗。其中罗马字母被替换成希腊字母使得敌人根本无法看懂信息。

苏托尼厄斯在公元二世纪写的《恺撒传》中对恺撒用过的其中一种替换密码作了详细的描写。恺撒只是简单地把信息中的每一个字母用字母表中的该字母后的第三个字母代替。这种密码替换通常叫做恺撒移位密码，或简单的说，恺撒密码。

在密码学中，凯撒密码（或称恺撒加密、恺撒变换、变换加密）是一种最简单且最广为人知的加密技术。它是一种替换加密的技术。这个加密方法是以恺撒的名字命名的，当年恺撒曾用此方法与其将军们进行联系。恺撒密码通常被作为其他更复杂的加密方法中的一个步骤，例如维吉尼亚密码。恺撒密码还在现代的ROT13系统中被应用。但是和所有的利用字母表进行替换的加密技术一样，恺撒密码非常容易被破解，而且在实际应用中也无法保证通信安全。

说了这么多，相信大家可能也有点晕了，下面这张图加密方法就是错三个位来实现加密功能

​              ![img](https://images2015.cnblogs.com/blog/1026866/201610/1026866-20161028113544203-1413480347.png)

（1）  设计思想：

1. 由于输入的是一串英文字符，所以我们用String类来编写，况且String类有许多方法可以调用
2. 错位需要对每个字符进行操作，可以把字符串转换为字符数组，调用的是string类的toCharArray方法
3. 由于string类也是采用Unicode字符集，所以我们进行错位操作时只需读取一个字符，然后与数字3相加，再转换为char类型，就实现了错3位加密操作，解密则减3.
4. 在加密操作中，如果加密的是字母表最后三个，则必须实现循环操作，即X加密后是A,Y加密后是B，Z加密后是C,实现这个就要用到ASCII码，当读到XYZ时，加密则是减去23后转换为char类型，当然，解密时读到ABC加上23即可

（2）  程序流程图：

​                            

 

![img](https://images2015.cnblogs.com/blog/1026866/201610/1026866-20161028113613437-1857661744.jpg)

[Return Top](https://www.cnblogs.com/ECJTUACM-873284962/p/8639300.html#_labelTop)

## 实现过程

我们定义个key=13，此时我们对字符串This is my secret message进行加密

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import pyperclip

message = 'This is my secret message'#保存加密或解密的字符串
key = 13#保存加密密钥的整数

mode = 'encrypt'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

translated = ''

message = message.upper()

for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        translated = translated + LETTERS[num]

    else:
        translated = translated + symbol

print(translated)

pyperclip.copy(translated)
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

打印结果如下：

```
GUVF VF ZL FRPERG ZRFFNTR
[Finished in 0.8s]
```

我们来对上面这部分代码进行分析

我们可以看到，第一行调用了一个pyperclip的模块，我们需要下载这个模块，很简单，安装一个pip，直接输入pip install pyperclip即可完成安装

```
message = 'This is my secret message'#保存加密或解密的字符串
key = 13#保存加密密钥的整数
```

message指定了用来保存加解密的字符串

而key用来保存加密密钥

```
message = message.upper()
```

调用了一个upper函数，将加解密字符串全部变成大写字母

后面的实现过程很简单，判断mode值是否为encrpy，然后对字符进行移位

[Return Top](https://www.cnblogs.com/ECJTUACM-873284962/p/8639300.html#_labelTop)

## 破解原理及实现

我们将加密后的字符串进行破解，实现原理如下：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import pyperclip

message = 'GUVF VF ZL FRPERG ZRFFNTR'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):

    translated = ''

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key

            if num < 0:
                num = num + len(LETTERS)

            translated = translated + LETTERS[num]

        else:
            translated = translated + symbol

    print('Key #%s:%s'%(key,translated))
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

打印结果如下：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
Key #0:GUVF VF ZL FRPERG ZRFFNTR
Key #1:FTUE UE YK EQODQF YQEEMSQ
Key #2:ESTD TD XJ DPNCPE XPDDLRP
Key #3:DRSC SC WI COMBOD WOCCKQO
Key #4:CQRB RB VH BNLANC VNBBJPN
Key #5:BPQA QA UG AMKZMB UMAAIOM
Key #6:AOPZ PZ TF ZLJYLA TLZZHNL
Key #7:ZNOY OY SE YKIXKZ SKYYGMK
Key #8:YMNX NX RD XJHWJY RJXXFLJ
Key #9:XLMW MW QC WIGVIX QIWWEKI
Key #10:WKLV LV PB VHFUHW PHVVDJH
Key #11:VJKU KU OA UGETGV OGUUCIG
Key #12:UIJT JT NZ TFDSFU NFTTBHF
Key #13:THIS IS MY SECRET MESSAGE
Key #14:SGHR HR LX RDBQDS LDRRZFD
Key #15:RFGQ GQ KW QCAPCR KCQQYEC
Key #16:QEFP FP JV PBZOBQ JBPPXDB
Key #17:PDEO EO IU OAYNAP IAOOWCA
Key #18:OCDN DN HT NZXMZO HZNNVBZ
Key #19:NBCM CM GS MYWLYN GYMMUAY
Key #20:MABL BL FR LXVKXM FXLLTZX
Key #21:LZAK AK EQ KWUJWL EWKKSYW
Key #22:KYZJ ZJ DP JVTIVK DVJJRXV
Key #23:JXYI YI CO IUSHUJ CUIIQWU
Key #24:IWXH XH BN HTRGTI BTHHPVT
Key #25:HVWG WG AM GSQFSH ASGGOUS
[Finished in 0.2s]
```