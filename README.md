# Huffman-encode-and-decode
1.0
# 南邮课程设计大作业
题目B4： 基于哈夫曼算法的加解密问题  
（一）课题内容  
哈夫曼算法不仅可以用于数据压缩编解码，同样也可以用于实现简单的加解密功能。设明文由若干英文单词构成，试利用哈夫曼算法实现如下功能要求：  
（二）课题要求  
1．基本要求  
(1) 构建单词字典库（可以下载一些文档，并进行字符串处理，提取其中的单词，从而构建字典库）。然后为每个单词配置一个随机数作为权重，利用哈夫曼算法为各单词生成对应的密文，从而构造密码字典；   
(2) 利用密码字典实现对输入文件的加解密；   
(3) 界面友好、直观；  
2. 提高要求  
(1) 按照基本要求实现的加解密系统无法抵抗基于单词频度分析的攻击，试设计能够抵御频度分析攻击的基于哈夫曼算法的加解密方法（提示：可以采用多密码字典混合加解密的方法，加密时随机选择某一个密码字典）；  
(2) 当密码字典规模较大时，加解密的性能必然受到影响，试设计好的算法提高加解密的效率。  
3.其他要求  
(1) 变量、函数命名符合规范。  
(2) 注释详细：每个变量都要求有注释说明用途；函数有注释说明功能，对参数、返回值也要以注释的形式说明用途；关键的语句段要求有注释解释。  
(3) 程序的层次清晰，可读性强。  
(4) 界面美观，交互方便。  
