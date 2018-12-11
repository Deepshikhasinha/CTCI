string = 'Hello World!\n'
arrayofchars = list (string)
i=0
j=1
print arrayofchars
size = len(arrayofchars)

while i < size:
    while j < size:
        if(arrayofchars[i] == arrayofchars[j]):
            arrayofchars.pop(j)
            size = len(arrayofchars)
        else:
            j += 1
    i += 1
    j = i+1     
            
print arrayofchars
