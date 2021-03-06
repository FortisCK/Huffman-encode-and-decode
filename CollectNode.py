#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
节点信息的读取和存储
'''
import random, os


class CollectNode:
    def __init__(self):
        root = "password dictionary"
        file_names = []
        for parent, catalog, filename in os.walk(root):
            file_names = filename
        x = random.randint(0, len(file_names) - 1)
        self.fileName1 = file_names[x]
        print("choose a password dictionary: " + self.fileName1)
        self.fr = open("password dictionary/"
                       + self.fileName1, 'r', encoding='utf-8', errors='ignore')

    # 从文件中读取下一个节点的信息
    def __readNextNode(self):
        node = self.fr.readline().strip('\n')
        if node == '':
            self.fr.close()
            return None
        return node.split('=')

    # 返回文件中所有节点信息构成的列表
    def getNodes(self):
        nodes = []
        node = self.__readNextNode()
        while node != None:
            nodes.append(node)
            node = self.__readNextNode()
        return nodes

    # 将所有节点信息构成的列表存入文件
    def saveNodes(self, nodes):
        fw = open(self.fileName, 'w')
        for node in nodes:
            string = node[0] + '=' + node[1] + '\n'
            fw.write(string)
        fw.close()


if __name__ == '__main__':
    io = CollectNode()
    print(io.getNodes())
