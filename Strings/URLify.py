import sys

name = bytearray("cat ate my food      ",'utf8')
last = len(name) - 1
i = len(name) - 1
while i <= len(name) and i > 0:
  #print(i)
  if name[i] != 32: 
    name[last] = name[i]
    last = last -1
    #i = i-1
  elif name[i] == 32 and name[i-1] != 32 and name[i+1] != 32:
    #print(chr(name[last]))
    name[last] = ord('%')
    name[last - 1] = ord('0')
    name [last -2] = ord('2')
    last = last - 3
    #i = i-2
  i = i-1

print(name)
