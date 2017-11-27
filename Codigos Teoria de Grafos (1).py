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
g.conecta("Santa Lucia","Macroplaza",0.55)
g.conecta("Santa Lucia","Barrio Antiguo",0.48)
g.conecta("Santa Lucia","Estadio BBVA",6.4)
g.conecta("Santa Lucia","La Purisima",2.24)
g.conecta("Macroplaza","Santa Lucia",0.55)
g.conecta("Macroplaza","Barrio Antiguo",0.38)
g.conecta("Barrio Antiguo","Santa Lucia",0.48)
g.conecta("Barrio Antiguo","Macroplaza",0.38)
g.conecta("Estadio BBVA", "Santa Lucia",6.4)
g.conecta("Estadio BBVA", "Macroplaza",6.56)
g.conecta("Arena Monterrey","Ciudad Universitaria",5.61)
g.conecta("Arena Monterrey","Obelisco",3.17)
g.conecta("Obispado","Obelisco",2.9)
g.conecta("Obispado","Fundidora",6.35)




print(diametro(g))
