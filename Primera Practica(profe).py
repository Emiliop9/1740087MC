Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:07:06) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> cnt=0
>>> def minimo(arr):
	aux = arr
	global cnt
	result= -1
	for i in range (0, len(arr)):
		#del aux[i]
		esminimo = True
		for j in range (0, len(aux)):
			cnt+=1
			if arr[i] > arr[j]:
				esminimo=False
				break
		#print(es minimo,i,j,arr[i],arr[j])
        if es minimo:
    		result=i
 		break
	else:
		aux=arr
	return result
def ordenaminetobruto(arr):
	aux=arr
	result[]
	for i in range (0, len(arr)):
		m=minimo(aux)
		result.append(aux[m])
		del aux [m]
	return result


import random
p=random. sample(range(2,102), 100)
cnt=0
print(p)
print(p[minimo(p)])
print((min(p))
print(ordenar(p))
print(cnt)
