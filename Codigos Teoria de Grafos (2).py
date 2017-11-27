class Fila(object):
    def __init__(self):
        self.fl=[]
    def obtener(self):
        return self.fl.pop(0)
    def meter(self,e):
        self.fl.append(e)
        return len(self.fl)
    @property
    def longitud(self):
        return len(self.fl)
class Pila(object):
    def __init__(self):
        self.pl=[]
    def obtener(self):
        return self.pl.pop()
    def meter(self,e):
        self.pl.append(e)
        return len(self.pl)
    @property
    def longitud(self):
        return len(self.pl)
class Grafo:
 
    def __init__(self):
        self.CTO = set() # un conjunto
        self.MARI = dict() # un mapeo de pesos de aristas
        self.vec = dict() # un mapeo
 
    def agrega(self, v):
        self.CTO.add(v)
        if not v in self.vec: # vecindad de v
            self.vec[v] = set() # inicialmente no tiene nada
 
    def conecta(self, v, u, peso=1):
        self.agrega(v)
        self.agrega(u)
        self.MARI[(v, u)] = self.MARI[(u, v)] = peso # en ambos sentidos
        self.vec[v].add(u)
        self.vec[u].add(v)

    @property
    def complemento(self):
        comp=Grafo()
        for v in self.ver:
            for w in self.ver:
                if v!=w and (v,w) not in self.ARI:
                    comp.conecta(v,w,1)  
            return comp
        
    def DFS(self,ni):
        visitados =[]
        f=Pila()
        f.meter(ni)
        while(f.longitud>0):
            na =f.obtener()
            visitados.append(na)
            ln = self.vec[na]
            for nodo in ln:
                if nodo not in visitados:
                    f.meter(nodo)
        return visitados
      
    def BFS(self,ni):
        visitados =[]
        f=Fila()
        f.meter(ni)
        while(f.longitud>0):
            na =f.obtener()
            visitados.append(na)
            ln = self.vec[na]
            for nodo in ln:
                if nodo not in visitados:
                    f.meter(nodo)
        return visitados

g=Grafo()
g.conecta('a','b')
g.conecta('a','c')
g.conecta('a','d')
g.conecta('d','e')
g.conecta('d','f')
g.conecta('c','g')

print(g.BFS('a'))
print(g.DFS('a'))
