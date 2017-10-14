Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> cnt=0
>>> def primo(n):
	global cnt
	for i in (2,round((n**(1/2)+1))):
		cnt=cnt+1
		if ((n%i)==0):
			print("No Primo")
			break

		else:
		 print("Primo")
		 break
	return n,cnt

>>> #Si creamos un ciclo estos son los resultados:))

	
Primo
1 (1, 1)
No Primo
2 (2, 1)
Primo
3 (3, 1)
No Primo
4 (4, 1)
Primo
5 (5, 1)
No Primo
6 (6, 1)
Primo
7 (7, 1)
No Primo
8 (8, 1)
Primo
9 (9, 1)
No Primo
10 (10, 1)
Primo
11 (11, 1)
No Primo
12 (12, 1)
Primo
13 (13, 1)
No Primo
14 (14, 1)
Primo
15 (15, 1)
No Primo
16 (16, 1)
Primo
17 (17, 1)
No Primo
18 (18, 1)
Primo
19 (19, 1)
No Primo
20 (20, 1)
Primo
21 (21, 1)
No Primo
22 (22, 1)
Primo
23 (23, 1)
No Primo
24 (24, 1)
Primo
25 (25, 1)
No Primo
26 (26, 1)
Primo
27 (27, 1)
No Primo
28 (28, 1)
Primo
29 (29, 1)
No Primo
30 (30, 1)
Primo
31 (31, 1)
No Primo
32 (32, 1)
Primo
33 (33, 1)
No Primo
34 (34, 1)
Primo
35 (35, 1)
No Primo
36 (36, 1)
Primo
37 (37, 1)
No Primo
38 (38, 1)
Primo
39 (39, 1)
No Primo
40 (40, 1)
Primo
41 (41, 1)
No Primo
42 (42, 1)
Primo
43 (43, 1)
No Primo
44 (44, 1)
Primo
45 (45, 1)
No Primo
46 (46, 1)
Primo
47 (47, 1)
No Primo
48 (48, 1)
Primo
49 (49, 1)
No Primo
50 (50, 1)
>>> 

