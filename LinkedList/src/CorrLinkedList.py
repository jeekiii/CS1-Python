#!/usr/bin/python3
# -*- coding: utf-8 -*-
class Node:
    def __init__(self, next, value):
        self.next = next
        self.value = value
    def getNext(self):
        return self.next
    def getValue(self):
        return self.value

class LinkedList:


    def __init__(self):
        self.root = None
    def add(self, value):
        if(self.root == None):
            self.root = Node(None, value)
        else:
            self.root = Node(self.root, value)

    def get_reverse(self):
        res = ""
        node = self.root
        while(node != None):
            res += str(node.getValue())
            node = node.getNext()
        return res
