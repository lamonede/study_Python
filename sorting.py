import random

def swap(arr, st, nd):
    tmp = arr[st]
    arr[st] = arr[nd]
    arr[nd] = tmp
    
def nodeswap(arr, min, mid, max):
    if(max - min > 1):
        if(arr[min] > arr[mid]):
            swap(arr, min, mid)
        if(arr[mid] > arr[max]):
            swap(arr, mid, max)
            if(arr[min] > arr[mid]):
                swap(arr, min, mid)

def elementswap(arr, min, mid, max):
    i = 1
    if(max - min > 2):
        for i in range((max-min)//2):
            if(arr[min+i] > arr[max-i]):
                swap(arr, min+i, max-i)

def sorting(arr, min, mid, max):
    if(max-min <= 1):
        return 0
    nodeswap(arr, min, mid, max)
    elementswap(arr, min, mid, max)
    sorting(arr, min, (min+mid)//2, mid)
    sorting(arr, mid, (mid+max)//2, max)
    return arr

i = list(range(9))

random.shuffle(i)
print("---------")
print("100010001")
for j in i:
    print(j, end="")

min = 0
mid = len(i)//2
max = len(i)-1
print()
for i in sorting(i, min, mid, max):
    print(i, end="")
