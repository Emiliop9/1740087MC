Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> cnt=0
>>> def fibonacci(n):
	global cnt
	cnt=cnt+1
	if n==0 or n==1:
		return(1)
	return fibonacci(n-2) + fibonacci(n-1)

>>> #Resultados del ciclo
>>> #1 1
2 3
3 5
5 9
8 15
13 25
21 41
34 67
55 109
89 177
144 287
233 465
377 753
610 1219
987 1973
1597 3193
2584 5167
4181 8361
6765 13529
10946 21891
17711 35421
28657 57313
46368 92735
75025 150049
121393 242785
196418 392835
317811 635621
514229 1028457
832040 1664079
1346269 2692537
2178309 4356617
3524578 7049155
5702887 11405773
9227465 18454929
14930352 29860703
24157817 48315633
39088169 78176337
63245986 126491971
102334155 204668309
165580141 331160281
267914296 535828591
433494437 866988873
701408733 1402817465
1134903170 2269806339
1836311903 3672623805