from heapq import heappop, heappush
from copy import deepcopy
import random

import time
def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst] 
    l = [] # empty list that will store current permutation
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]
       for p in permutation(remLst):
           l.append([m] + p)
    return l

class Fila:
    def __init__(self):
        self.fila= []
    def obtener(self):
        return self.fila.pop()
    def meter(self,e):
        self.fila.insert(0,e)
        return len(self.fila)
    @property
    def longitud(self):
        return len(self.fila)

class Pila:
    def __init__(self):
        self.pila= []
    def obtener(self):
        return self.pila.pop()
    def meter(self,e):
        self.pila.append(e)
        return len(self.pila)
    @property
    def longitud(self):
        return len(self.pila)


def flatten(L):
    while len(L) > 0:
        yield L[0]
        L = L[1]

class Grafo:
 
    def __init__(self):
        self.V = set() # un conjunto
        self.E = dict() # un mapeo de pesos de aristas
        self.vecinos = dict() # un mapeo
 
    def agrega(self, v):
        self.V.add(v)
        if not v in self.vecinos: # vecindad de v
            self.vecinos[v] = set() # inicialmente no tiene nada
 
    def conecta(self, v, u, peso=1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v, u)] = self.E[(u, v)] = peso # en ambos sentidos
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)
 
    def complemento(self):
        comp= Grafo()
        for v in self.V:
            for w in self.V:
                if v != w and (v, w) not in self.E:
                    comp.conecta(v, w, 1)
        return comp

    def BFS(self,ni):
        visitados =[]
        f=Fila()
        f.meter(ni)
        while(f.longitud>0):
            na = f.obtener()
            visitados.append(na)
            ln = self.vecinos[na]
            for nodo in ln:
                if nodo not in visitados:
                    f.meter(nodo)
        return visitados
    
    def DFS(self,ni):
        visitados =[]
        f=Pila()
        f.meter(ni)
        while(f.longitud>0):
            na = f.obtener()
            visitados.append(na)
            ln = self.vecinos[na]
            for nodo in ln:
                if nodo not in visitados:
                    f.meter(nodo)
        return visitados
    
    def shortest(self, v): # Dijkstra's algorithm
        q = [(0, v, ())] # arreglo "q" de las "Tuplas" de lo que se va a almacenar dondo 0 es la distancia, v el nodo y () el "camino" hacia el
        dist = dict() #diccionario de distancias 
        visited = set() #Conjunto de visitados
        while len(q) > 0: #mientras exista un nodo pendiente
            (l, u, p) = heappop(q) # Se toma la tupla con la distancia menor
            if u not in visited: # si no lo hemos visitado
                visited.add(u) #se agrega a visitados
                dist[u] = (l,u,list(flatten(p))[::-1] + [u])  	#agrega al diccionario
            p = (u, p) #Tupla del nodo y el camino
            for n in self.vecinos[u]: #Para cada hijo del nodo actual
                if n not in visited: #si no lo hemos visitado
                    el = self.E[(u,n)] #se toma la distancia del nodo acutal hacia el nodo hijo
                    heappush(q, (l + el, n, p)) #Se agrega al arreglo "q" la distancia actual mas la ditanacia hacia el nodo hijo, el nodo hijo n hacia donde se va, y el camino
        return dist #regresa el diccionario de distancias

    def kruskal(self):
        e = deepcopy(self.E)
        arbol = Grafo()
        peso = 0
        comp = dict()
        t = sorted(e.keys(), key = lambda k: e[k], reverse=True)
        nuevo = set()
        while len(t) > 0 and len(nuevo) < len(self.V):
            #print(len(t)) 
            arista = t.pop()
            w = e[arista]    
            del e[arista]
            (u,v) = arista
            c = comp.get(v, {v})
            if u not in c:
                #print('u ',u, 'v ',v ,'c ', c)
                arbol.conecta(u,v,w)
                peso += w
                nuevo = c.union(comp.get(u,{u}))
                for i in nuevo:
                    comp[i]= nuevo
        print('MST con peso', peso, ':', nuevo, '\n', arbol.E)
        return arbol

    def vecinoMasCercano(self):
        lv = list(self.V)
        random.shuffle(lv)
        ni = lv.pop()
        le = dict()
        while len(lv)>0:
            ln = self.v[ni]
            for nv in ln:
                le[nv]=self.E[(ni,nv)]
            menor = min(le.values())
            lv.append(menor)
            del lv[menor]
        return lv
        
        

g= Grafo()
g.conecta('Mexico','EU', 30)
g.conecta('Mexico','Spain',9045 )
g.conecta('Mexico','Francia', 9100)
g.conecta('Mexico','Canada', 4035)
g.conecta('Mexico','Chec', 9035)
g.conecta('Mexico','Italia', 10135)
g.conecta('Mexico','Egipto', 12000)
g.conecta('Mexico','China', 12095)
g.conecta('Mexico','UK', 8535)
g.conecta('EU','Spain', 8309)
g.conecta('EU','Francia', 8400)
g.conecta('EU','Canada', 2705)
g.conecta('EU','Chec', 9035)
g.conecta('EU','Italia', 9130)
g.conecta('EU','Egipto', 11100)
g.conecta('EU','China', 12805)
g.conecta('EU','UK', 1300)
g.conecta('Spain','Francia', 530)
g.conecta('Spain','Canada', 5505)
g.conecta('Spain','Chec', 1635)
g.conecta('Spain','Italia', 1184)
g.conecta('Spain','Egipto', 3566)
g.conecta('Spain','China', 7800)
g.conecta('Spain','UK', 1028)
g.conecta('Francia','Canada', 1025)
g.conecta('Francia','Chec', 1030)
g.conecta('Francia','Italia', 925)
g.conecta('Francia','Egipto', 3266)
g.conecta('Francia','China', 9500)
g.conecta('Francia','UK', 1300)
g.conecta('Canada','Chec', 6300)
g.conecta('Canada','Italia', 4105)
g.conecta('Canada','Egipto', 9366)
g.conecta('Canada','China', 11700)
g.conecta('Canada','UK', 5300)
g.conecta('Chec','Italia', 815)
g.conecta('Chec','Egipto', 2885)
g.conecta('Chec','China', 6700)
g.conecta('Chec','UK', 1270)
g.conecta('Italia','Egipto', 2385)
g.conecta('Italia','China', 9040)
g.conecta('Italia','UK', 1740)
g.conecta('Egipto','China', 8440)
g.conecta('Egipto','UK', 4060)
g.conecta('China','UK', 9235)

print(g.kruskal())
print(g.shortest('UK'))


print(g)
k = g.kruskal()
print([print(x, k.E[x]) for x in k.E])

for r in range(10):
    ni = random.choice(list(k.V))
    dfs =  k.DFS(ni)
    c = 0
    #print(dfs)
    #print(len(dfs))
    for f in range(len(dfs) -1):
            c += g.E[(dfs[f],dfs[f+1])]
            print(dfs[f], dfs[f+1], g.E[(dfs[f],dfs[f+1])] )
            
    c += g.E[(dfs[-1],dfs[0])]
    print(dfs[-1], dfs[0], g.E[(dfs[-1],dfs[0])])
    print('costo',c)



data = list('abcdefghij')
tim=time.clock()
per = permutation(data)
print(time.clock()-tim)
