import sys

name = bytearray("foood",'utf8')
array = []
for i in range(0,256):
  array.append(0)
flag = 0
for i in range(0,len(name)):
  if array[name[i]] < 1:
    array[name[i]] += 1
  else:
    flag = 1
    break
if(flag == 1):
  print("not unique")
else:
  print("Unique")
