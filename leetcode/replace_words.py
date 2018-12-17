# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 16:04:20 2018

@author: dsinha1
"""
diction = ["a", "aa", "aaa", "aaaa"]

sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
dic = {}
sen = sentence.split(" ")
final = []
for root in diction:
    #print(dic)
    for word in sen:
        if len(word) >= len(root):
            if word[0:len(root)] == root:
                if word in dic:
                    if len(dic[word]) > len(root):
                        dic[word] = root
                else:
                    dic[word] = root
for i in range(len(sen)):
    if sen[i] in dic:
        sen[i] = dic[sen[i]]
res = ' '.join(sen)                 
print(res)