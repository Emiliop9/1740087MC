Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> funcion={}
>>> cnt=0
>>> def fibonacci(n):
	global funcion,cnt
	cnt+=1
	if n==0 or n==1:
		return(1)
	if n in funcion:
		return funcion[n]
	else:
		val=fibonacci(n-2)+fibonacci(n-1)
		funcion[n]=val
		return val

	
>>> for i in range (1,51):
	print(i,cnt,fibonacci(i))

	
1 0 1
2 1 2
3 4 3
4 7 5
5 10 8
6 13 13
7 16 21
8 19 34
9 22 55
10 25 89
11 28 144
12 31 233
13 34 377
14 37 610
15 40 987
16 43 1597
17 46 2584
18 49 4181
19 52 6765
20 55 10946
21 58 17711
22 61 28657
23 64 46368
24 67 75025
25 70 121393
26 73 196418
27 76 317811
28 79 514229
29 82 832040
30 85 1346269
31 88 2178309
32 91 3524578
33 94 5702887
34 97 9227465
35 100 14930352
36 103 24157817
37 106 39088169
38 109 63245986
39 112 102334155
40 115 165580141
41 118 267914296
42 121 433494437
43 124 701408733
44 127 1134903170
45 130 1836311903
46 133 2971215073
47 136 4807526976
48 139 7778742049
49 142 12586269025
50 145 20365011074
>>> 