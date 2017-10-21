from heapq import heappop, heappush

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


g=Grafo()
g.conecta('a','b', 2)
g.conecta('a','c', 2)
g.conecta('a','d', 1)
g.conecta('c','f', 10)
g.conecta('b','f', 1)
g.conecta('b','e',4)
g.conecta('c','f',7)
g.conecta('a','f',20)
g.conecta('c','b',3)
g.conecta('f','g',5)
g.conecta('g','h',3)
g.conecta('g','i',5)
g.conecta('f','k',8)
g.conecta('c','h',5)
g.conecta('c','i',7)
g.conecta('a','h',9)
g.conecta('b','k',16)
g.conecta('d','k',11)
g.conecta('b','k',19)
g.conecta('k','l',13)
g.conecta('k','m',21)
g.conecta('l','n',40)
g.conecta('l','m',14)
g.conecta('m','o',3)
g.conecta('l','o',6)
g.conecta('o','p',3)
g.conecta('c','p',20)
g.conecta('d','p',30)
g.conecta('f','o',60)
g.conecta('a','p',35)
print(g.shortest('a'))
