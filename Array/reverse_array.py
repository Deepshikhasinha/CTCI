
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:48:31 2018

@author: dsinha1
"""

def reverse_words(arr):
  words = [[]]
  rev = []
  i = 0
  print(len(arr))
  while i <= len(arr)-1:
      print(i)
      temp = []
      while arr[i] != '  ' :
          temp.append(arr[i])
          i += 1
      print(temp)
      words.append(temp)
  #print(words)
  #x = len(words) - 1
  #while x >= 0:
   # word = words[x]
    #for k in word:
     # rev.append(k)
    #rev.append(' ')
    #x -= 1
  return words

print(reverse_words(['p', 'e', 'r', 'f', 'e', 'c', 't', '  ','m', 'a', 'k', 'e', 's', '  ','p', 'r', 'a', 'c', 't', 'i', 'c', 'e']))
