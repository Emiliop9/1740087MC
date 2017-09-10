import random
cnt=0
#no me Corrió el programa

def quicksort(arr):
    global cnt
    if len(arr)<=1:
        return arr
    p=arr.pop(0)
    menores,mayores= [], []
    for e in arr:
        cnt+=1
        if e<=p:
            menores.append(e)
        else:
            mayores.append(a)
    return quicksort(menores) + [p] + quicksort(mayores)

def rndar(long):
    arr=[]
    for i in range (long):
        arr.append(random,randint(0,long))
    return arr

i=10

while i<=10:
    for replica in range(10):
        ori=rndar(1)
        arr=quicksort(ori)
        print(1,cnt,arr,ori)
        cnt=0
