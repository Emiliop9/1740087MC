#class Pila
class Pila:
    def __init__(self):
        self.pila=[]

    def obtener(self):
        return self.pila.pop()
    def meter(self,e):
        self.pila.append(e)
        return len(self.pila)
    @property
    def longuitud(self):
        return len(self.pila)
#class grafo
class Grafo:
    def __init__(self):
        self.V=set()
        self.E=dict()
        self.vecinos=dict()

    def agrega(self,v):
        self.V.add(v)
        if not v in self.vecinos:
            self.vecinos[v]=set()

    def conecta(self,v,u,peso=1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v,u)]= self.E[(u,v)]=peso
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)

    def complemento(self):
        comp=Grafo()
        for v in self.V:
            for w in self.V:
                if v !=w and (v,w) not in self.E:
                    comp.conecta(v,w,1)
        return comp




class Pila(object):
    def __init__(self):
        self.a=[]
    def obtener(self):
        return self.a.pop()
    def meter(self, e):
        self.a.append(e)
        return len(self.a)
    @property
    def longitud(self):
        return len(self.a)
    
class Cola(Pila):
    def obtener(self):
        return self.a.pop(0)
        


class Grafo():
    def __init__(self):
        self.V=set()
        self.E=dict()
        self.vecinos=dict()
        
    def agrega(self,v):
        self.V.add(v)
        if not v in self.vecinos:
            self.vecinos[v]=set()
        
    def conecta(self,v,u,peso=1):
        self.agrega(u)
        self.agrega(v)
        self.E[(u,v)]=self.E[(v,u)]=peso
        self.vecinos[u].add(v)
        self.vecinos[v].add(u)
        
    def complemento(self):
        comp=Grafo()
        for u in self.V:
            for v in self.V:
                if u!=v and (u,v) not in self.E:
                    comp.conecta(u,v,1)
        return comp
        
        



    
def junta(a,b):
    return [(a[i],b[i]) for i in range(min(len(a),len(b)))]
    
    
    
def DFS(grafo,ini):
    vis =[ini]
    dist=[0]
    bus=Cola()
    bus.meter((ini,0))
    while bus.longitud>0:
        (act,d)=bus.obtener()
        vecinos=grafo.vecinos[act]
        for w in vecinos:
            if w not in vis:
                vis.append(w)
                dist.append(d+1)
                bus.meter((w,d+1))
    return junta(vis,dist)
    
    
    
    
def diametro(grafo):
    maxs,max1,bes=-1,0,0
    for v in grafo.V:
        resbfs=DFS(grafo,v) 
        (fin,dist)=resbfs[-1]
        if dist>maxs:
            maxs=dist
            max1=v
            bes=fin
    return [maxs,max1,bes]

g=Grafo()
g.conecta('Mexico','EU', 30)
g.conecta('Mexico','Spain',9045 )
g.conecta('Mexico','Francia', 9100)
g.conecta('Mexico','Canada', 4035)
g.conecta('Mexico','Chec', 9035)
g.conecta('Mexico','Italia', 10135)
g.conecta('Mexico','Egipto', 12000)
g.conecta('Mexico','China', 12095)
g.conecta('Mexico','UK', 8535)
g.conecta('EU','Mexico', 30)
g.conecta('EU','Spain', 8309)
g.conecta('EU','Francia', 8400)
g.conecta('EU','Canada', 2705)
g.conecta('EU','Chec', 9035)
g.conecta('EU','Italia', 9130)
g.conecta('EU','Egipto', 11100)
g.conecta('EU','China', 12805)
g.conecta('EU','UK', 1300)
g.conecta('Spain','Mexico',9045 )
g.conecta('Spain','EU', 8309)
g.conecta('Spain','Francia', 530)
g.conecta('Spain','Canada', 5505)
g.conecta('Spain','Chec', 1635)
g.conecta('Spain','Italia', 1184)
g.conecta('Spain','Egipto', 3566)
g.conecta('Spain','China', 7800)
g.conecta('Spain','UK', 1028)
g.conecta('Francia','Mexico', 9100)
g.conecta('Francia','EU', 8400)
g.conecta('Francia','Spain', 530)
g.conecta('Francia','Canada', 1025)
g.conecta('Francia','Chec', 1030)
g.conecta('Francia','Italia', 925)
g.conecta('Francia','Egipto', 3266)
g.conecta('Francia','UK', 1300)
g.conecta('Francia','China',9571)
g.conecta('Canada','Mexico', 4035)
g.conecta('Canada','EU', 2705)
g.conecta('Canada','Spain', 5505)
g.conecta('Canada','Francia', 1025)
g.conecta('Canada','Chec', 6300)
g.conecta('Canada','Italia', 4105)
g.conecta('Canada','Egipto', 9366)
g.conecta('Canada','China', 11700)
g.conecta('Canada','UK', 5300)
g.conecta('Chec','Mexico', 9035)
g.conecta('Chec','EU', 9035)
g.conecta('Chec','Spain', 1635)
g.conecta('Chec','Francia', 1030)
g.conecta('Chec','Italia', 815)
g.conecta('Chec','Egipto', 2885)
g.conecta('Chec','China', 6700)
g.conecta('Chec','UK', 1270)
g.conecta('Italia','Mexico', 10135)
g.conecta('Italia','EU', 9130)
g.conecta('Italia','Spain', 1184)
g.conecta('Italia','Francia', 925)
g.conecta('Italia','Canada', 4105)
g.conecta('Italia','Chec', 815)
g.conecta('Italia','Egipto', 2385)
g.conecta('Italia','China', 9040)
g.conecta('Italia','UK', 1740)
g.conecta('Egipto','Mexico', 12000)
g.conecta('Egipto','EU', 11100)
g.conecta('Egipto','Spain', 3566)
g.conecta('Egipto','Francia', 3266)
g.conecta('Egipto','Canada', 9366)
g.conecta('Egipto','Chec', 2885)
g.conecta('Egipto','Italia', 2385)
g.conecta('Egipto','China', 8440)
g.conecta('Egipto','UK', 4060)
g.conecta('China','Mexico', 12095)
g.conecta('China','EU', 12805)
g.conecta('China','Spain', 7800)
g.conecta('China','Francia',9571)
g.conecta('China','Canada', 11700)
g.conecta('China','Chec', 6700)
g.conecta('China','Italia', 9040)
g.conecta('China','Egipto', 8440)
g.conecta('China','UK', 9235)
g.conecta('UK','Mexico', 8535)
g.conecta('UK','EU', 1300)
g.conecta('UK','Spain', 1028)
g.conecta('UK','Francia', 1300)
g.conecta('UK','Canada', 5300)
g.conecta('UK','Chec', 1270)
g.conecta('UK','Italia', 1740)
g.conecta('UK','Egipto', 4060)
g.conecta('UK','Egipto', 9235)

#El primer Aspecto a revisar es el diametro(Menor recorrido de cantidad entre todos los nodos)
print("DFS para Mexico") #Nodo 
print("")
print(DFS(g,'Mexico'))
print("")
print("DFS para EU")#NODO
print("")
print(DFS(g,'EU'))
print("")
print("DFS para Spain")#nodo 
print("")
print(DFS(g,'Spain'))
print("")
print("DFS para Francia")#nodo 
print("")
print(DFS(g,'Francia'))
print("")
print("DFS para Canada")#nodo
print("")
print(DFS(g,'Canada'))
print("")
print("DFS para Chec")#nodo
print("")
print(DFS(g,'Chec'))
print("")
print("DFS para Italia")#nodo
print("")
print(DFS(g,'Italia'))
print("")
print("DFS para Egipto")#nodo
print("")
print(DFS(g,'Egipto'))
print("")
print("DFS para China")#nodo 
print("")
print(DFS(g,'China'))
print("")
print("DFS para UK")#nodo
print("")
print(DFS(g,'UK'))
print("")
print(diametro(g))
#El diametro de este grafo es [1, 'Italia', 'UK'] ya que para cualquier recorrido de cualquier nodo es la menor cantidad de nodos recorridos

#Ahora para Centralidad:

print("")
print("DFS para Mexico") #Nodo 
print("")
print(DFS(g,'Mexico'))
print("")
print("DFS para EU")#NODO
print("")
print(DFS(g,'EU'))
print("")
print("DFS para Spain")#nodo 
print("")
print(DFS(g,'Spain'))
print("")
print("DFS para Francia")#nodo 
print("")
print(DFS(g,'Francia'))
print("")
print("DFS para Canada")#nodo
print("")
print(DFS(g,'Canada'))
print("")
print("DFS para Chec")#nodo
print("")
print(DFS(g,'Chec'))
print("")
print("DFS para Italia")#nodo
print("")
print(DFS(g,'Italia'))
print("")
print("DFSpara Egipto")#nodo
print("")
print(DFS(g,'Egipto'))
print("")
print("DFS para China")#nodo
print("")
print(DFS(g,'China'))
print("")
print("DFS para UK")#nodo
print("")
print(DFS(g,'UK'))
print("")
# para todos los casos del dfs Recorre  2 nodos para realizar, ¿entonces cualquiera de los nodos se le puede considerar nodo central?
#Para saber si es un arbol:
#AL CHCECAR 1ERA CONDICION DE DOCUMENTO: LAS ARISTAS = VERTICES-1, Y NO SE CUMPLE
print("")
print("No es un arbol")
print("")
print("¿Cual es su densidad?")
print("")
#Densidad se da numero de aristas/ numero de aristas posibles total.
print("Aristas totales se da por (n*(n-1))/2,donde n son los nodos entonces el total son:")
print((10*9)/2)
print("")
print("Finalmente dividimos el numero de aristas que tenemos (45) entre el total de aristas (45)")
print("")
print("La densidad es: 1")








