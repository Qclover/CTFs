**PDF****文件分析**

**0x1:**PDF文件是一个非常复杂的文档文件格式，[多年来](https://www.sultanik.com/pocorgtfo/)已经出现了多种可以隐藏数据的地方和技巧，因此它在CTF取证题中十分流行。NSA在2008年发表过标题为“Adobe PDF中的隐藏数据和元数据：公开危险和应对措施”。尽管原URL已经无法打开，但你仍可以在[这里](http://www.itsecure.hu/library/file/Biztons%C3%A1gi%20%C3%BAtmutat%C3%B3k/Alkalmaz%C3%A1sok/Hidden%20Data%20and%20Metadata%20in%20Adobe%20PDF%20Files.pdf)打开副本。Ange Albertini也在Github上保留着一份关于[PDF文件格式的隐藏小技巧](https://github.com/corkami/docs/blob/master/PDF/PDF.md)的Wiki。

**0x2:**PDF格式类似HTML一样有着部分的明文，但其中还包括了许多二进制‘对象’。Didier Steven写过关于PDF格式的[具体材料分析](https://blog.didierstevens.com/2008/04/09/quickpost-about-the-physical-and-logical-structure-of-pdf-files/)，这些二进制‘对象’可以是压缩数据，也可以是加密数据，还可以类似Javascript或Flash的脚本语言。你可以通过文本编辑器也可以使用类似Origami的PDF文件编辑器来显示PDF的结构。

[qpdf](https://github.com/qpdf/qpdf)是一个查看pdf文件并整理提取信息时十分有用的工具，另一个是Ruby中的[Origami](https://github.com/mobmewireless/origami-pdf)框架。

在搜索PDF文件中的隐藏数据时，常见的隐藏地方包括：

- 不可见的图层
- Adobe的元数据格式‘XMP’
- Adobe的XMP元数据
- PDF的‘增量生成’功能允许保留用户不可见的前版本信息
- 白色的文字或背景图
- 图片背后的文字信息
- 图层后面被覆盖的另一个图层
- 不显示的注释层。