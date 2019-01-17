

def build_heap(arr):
    for i in range(len(arr)//2):
        small = arr[i]
        s = "none"
        if small > arr[i*2 +1]:
            s = "left"
        if i* 2 + 2 < len(arr) and small > arr[i*2 + 2]:
            s = "right"
        if s == "left":
            arr[i],arr[i*2+1] = arr[i*2+1],arr[i]
        if s == "right":
            arr[i],arr[i*2+2] = arr[i*2+2],arr[i]
        if arr[i] < arr[i//2]:
            arr[i],arr[i//2] = arr[i//2], arr[i]
    return arr
            
  
def heap_insert(arr,element):
    arr.append(element)
    i = len(arr) -1
    while i > 0 :
        print(arr[i])
        print(arr[i//2 -1])
        if arr[i] < arr[i//2 -1]:
            arr[i],arr[i//2 -1] = arr[i//2 -1],arr[i]
            i = i//2
        else:
            break
    return arr
arr = build_heap([3,2,5,1,6,8])
print(arr)
print(heap_insert(arr,4))
