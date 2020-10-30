#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter
from HuffumanTree import *
from NodeDataIO import *
from decode import *
import tkinter.messagebox
from tkinter.filedialog import *
import re, random


class MyDialog:
    def __init__(self):
        root = Tk()
        root.title('芜湖，起飞')
        Label(root, text="明文：").grid(row=1, column=0)
        Label(root, text="密文：").grid(row=5, column=0)
        Label(root, height=2).grid(row=3)
        Label(root, height=2).grid(row=7)
        Frame1 = Frame(root).grid(row=8)
        self.string = Text(root)
        self.encoding = Text(root)
        self.string['width'] = 40
        self.encoding['width'] = 40
        self.string['height'] = 10
        self.encoding['height'] = 10
        self.string.bind('<FocusIn>', self.focusString)
        self.encoding.bind('<FocusIn>', self.focusEncoding)
        self.string.grid(row=0, column=1, rowspan=3)
        self.encoding.grid(row=4, column=1, rowspan=3)
        trans = Button(Frame1, text="加密", command=self.transform)
        dec = Button(Frame1, text="解密", command=self.decode)
        self.__reset = Button(Frame1, text="重置", command=self.__reset)
        dict = Button(Frame1, text="生成加密字典", command=self.dictionary)
        getStr = Button(root, text="从文件导入明文", command=self.getStr)
        getEnc = Button(root, text="从文件导入密文", command=self.getEnc)
        putStr = Button(root, text="将解密结果导出到文件", command=self.putStr)
        putEnc = Button(root, text="将加密结果导出到文件", command=self.putEnc)
        trans.grid(row=8, column=2)
        dec.grid(row=8, column=3)
        dict.grid(row=8, column=0)
        self.__reset.grid(row=8, column=4)
        getStr.grid(row=0, column=2)
        getEnc.grid(row=4, column=2)
        putStr.grid(row=2, column=2)
        putEnc.grid(row=6, column=2)
        root.mainloop()

    def dictionary(self):
        fileName = askopenfilename()
        if fileName == '':
            return
        f = open(fileName)
        try:
            text = f.read()  # 读取整个文件并放入一个字符串变量中
            words = re.findall(r"\b[a-zA-Z]{1,50}\b", text)  # 正则匹配所有英文单词得到一个列表
            if words == '':
                tkinter.messagebox.showwarning("错误", "无法生成密钥")
            results = []
            dictionary = {}
            value = 0
            li = [i for i in range(2000)]
            li1 = random.sample(li, 2000)
            for word in words:
                results.append(word)
            results += [',', '.', '?', '!', ':', ';', '-', '_', '(', ')', '[', ']', "'", '"']
            results = list(set(results))  # 将匹配结果存储在列表里并用set函数去除重复单词
            results.sort()  # 对列表排序
            for result in results:
                dictionary[result] = li1[value]  # 单词为字典的键，随机数为值，作为每个单词的权重
                value += 1
            number = random.randint(100, 999)
            output = open("password dictionary/dictionary%d.txt" % number, "w")
            print(dictionary)
            print("create password dictionary：" + "dictionary%d.txt" % number)
            for key in dictionary:
                output.writelines(key + "=" + str(dictionary[key]) + "\n")  # 字典内容写入文件
            output.close()
        finally:
            f.close()

    # 字符串导出到文件
    def putStr(self):
        string = self.string.get('0.0', END)
        if string.strip('\n') == '':
            tkinter.messagebox.showwarning("警告", "没有可写的字符")
            return
        fileName = asksaveasfilename()
        if fileName == '':
            return
        fw = open(fileName, 'w')
        fw.write(string)
        fw.close()

    # 编码导出到文件
    def putEnc(self):
        encoding = self.encoding.get('0.0', END)
        if encoding.strip('\n') == '':
            tkinter.messagebox.showwarning("警告", "没有可写的字符")
            return
        fileName = asksaveasfilename()
        if fileName == '':
            return
        fw = open(fileName, 'w')
        fw.write(encoding)
        fw.close()

    # 从文件中获取字符串
    def getStr(self):
        fileName = askopenfilename()
        if fileName == '':
            return
        fr = open(fileName, 'r')
        string = ''
        tmp = fr.readline().strip('\n')
        while tmp != '':
            string += tmp
            tmp = fr.readline().strip('\n')
        fr.close()
        self.string.delete('0.0', END)
        self.string.insert('0.0', string)
        self.encoding['state'] = 'disabled'

    # 从文件中获取编码
    def getEnc(self):
        fileName = askopenfilename()
        if fileName == '':
            return
        fr = open(fileName, 'r')
        string = ''
        tmp = fr.readline().strip('\n')
        while tmp != '':
            string += tmp
            tmp = fr.readline().strip('\n')
        fr.close()
        self.encoding.delete('0.0', END)
        self.encoding.insert('0.0', string)
        self.string['state'] = 'disabled'

    # 当字符串文本框获得焦点，将编码框设为不可用
    def focusString(self, event):
        if self.string['state'] == 'normal':
            self.encoding['state'] = 'disabled'

    # 当编码框获得焦点，将字符串框设为不可用
    def focusEncoding(self, event):
        if self.encoding['state'] == 'normal':
            self.string['state'] = 'disabled'

    # 字符和编码之间相互转化
    def transform(self):
        io = NodeDataIO()
        nodeList = io.getNodes()
        tree = HuffumanTree(nodeList)
        encoder = Encoding(tree.encodingList)
        count = io.fileName1[10:13]
        self.count = count
        if (self.encoding['state'] != 'disabled') and (self.string['state'] != 'disabled'):
            return
        elif (self.encoding['state'] == 'disabled') and (self.string['state'] != 'disabled'):
            text = self.string.get('0.0', END).strip('\n')
            if text[-1] != ' ':
                if text[-1] in [',', '.', '?', '!', ':', ';', '-', '_', '(', ')', '[', ']', "'", '"']:
                    text += ' '
                else:
                    tkinter.messagebox.showerror('错误', '您输入的文本不符合规范，请在末尾添加标点')
                    return
            for i in range(len(text)):
                if text[i] in [',', '.', '?', '!', ':', ';', '-', '_', '(', ')', '[', ']', "'", '"'] and text[
                    i + 1] != ' ':
                    tkinter.messagebox.showerror('错误', '您输入的文本不符合规范，请在标点后添加空格')
                    return

            try:
                encoding = bin(int(io.fileName1[10:13]))[2:] + encoder.getStringEncoding(text)
            except:
                tkinter.messagebox.showerror('错误', '您输入的文本中包含未编码的字符，请重新输入！')
                return
            self.encoding['state'] = 'normal'
            self.encoding.delete('0.0', END)
            self.encoding.insert('0.0', encoding)
            self.__reset.focus_set()
        else:
            self.__decode(encoder)

    # 重置所有文本框
    def __reset(self):
        self.string['state'] = 'normal'
        self.encoding['state'] = 'normal'
        self.string.delete('0.0', END)
        self.encoding.delete('0.0', END)

        self.__reset.focus_set()

    def decode(self):
        text = self.encoding.get('0.0', END).strip('\n')
        if text.startswith(bin(int(self.count))[2:]):
            text = text[len(bin(int(self.count))[2:]):]
        global de_fr
        de_fr = open('password dictionary/dictionary'
                     + self.count + '.txt', 'r', encoding='utf-8', errors='ignore')
        new = Decode(de_fr)
        nodeList = new.getNodes()
        tree = HuffumanTree(nodeList)
        encoder = Encoding(tree.encodingList)
        try:
            string = encoder.getStringDecoding(str(text))
        except:
            tkinter.messagebox.showerror('错误', '无法解码，请重新输入!')
            return
        self.string['state'] = 'normal'
        self.string.delete('0.0', END)
        self.string.insert('0.0', string)
        self.__reset.focus_set()


MyDialog()
