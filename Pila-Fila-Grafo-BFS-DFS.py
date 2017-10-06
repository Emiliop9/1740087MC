Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Fila:#creamos una clase que utilice las carctertisticas para meter, sacar, devolver la longitud del arreglo.
    def __init__(self):
        self.fila=[]
    def obtener(self):
        return self.fila.pop() #Nos da ultimo valor almacenado
    def meter(self,e):
        self.fila.insert(0,e) #Se agrega un elemento
        return len(self.fila) #Nos regresa la longitud del arreglo
    @property
    def longitud(self):
        return len(self.fila) #Nos dice la longitud del arreglo
	#De esta manera se crea una clase Fila
 #Recordadndo que el primer dato que metamos, va a ser el primero en salir.

>>> class Pila: #Creamos la clase con las carcteristicas para sacar,meter e imprimir la longitud de la pila
    def __init__(self):
        self.pila=[]


    def obtener(self):
        return self.pila.pop() #regresa ultimo valor en la pila
    def meter(self,e):
        self.pila.append(e) #metes un ultimo valor
        return len(self.pila) #regresa tamaño de la pila
    @property
    def longitud(self):
        return len(self.pila) #imprime la longitud de la clase
#En el caso de la pila recordamos que si metemos un dato y poco a poco algunos mas el primer dato que obtenedremos al llamar tal caracteristica será el ultimo dato que metimos y no el primero como en fila

>>> class Grafo:
 
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
#Mediante el grafo podemos conectar los elementos que ya estan dentro de nuestras estrucutras como lo son fila o pila y medir tanto su longitud y anchura,este es un gran  uso que se le da a un grafo.

>>> #Para el siguiente algoritmo BFS que significa que Medidor de anchura, en este caso ocupasmos el grafo y fila mediante estos el grafo crea las relaciones entre los elementos y mediante esto se mide la anchura.
>>> def BFS(grafo,ni):
        visitados=[ni]
        f=Fila()
        f.meter(ni)
        while (f.longitud>0):
            na=f.obtener()
            visitados.append(na)
            ln= grafo.vecinos[na]
            for nodo in ln:
                if nodo not in visitados:
                    f.meter(nodo)

        return visitados

>>> #Como ya tenemos tanto fila como pila y el Grafo solo es necesario crear las relaciones
>>> prueba= Grafo()
>>> prueba.conecta('1','2')
>>> prueba.conecta('1','3')
>>> prueba.conecta('3','5')
>>> prueba.conecta('1','4')
>>> prueba.conecta('4','6')
>>> BFS(prueba,'1')
['1', '1', '2', '3', '4', '5', '6']
>>> #ahora intentaremos usar DFS para medir la longitud de una pila, utilizando obviamente Pila y Grafo
>>> proof=Grafo()
>>> proof.conecta('a','b')
>>> proof.conecta('a','c')
>>> proof.conecta('c','d')
>>> proof.conecta('d','f')
>>> proof.conecta('c','e')
>>> def DFS(g,ni):
	visitados=[]
	p=Pila()
	p.meter(ni)
	while(p.longitud>0):
		na=p.obtener()
		visitados.append(na)
		ln=g.vecinos[na]
		for nodo in ln:
                    if nodo not in visitados:
                        p.meter(nodo)
		return visitados

	
>>> DFS(proof,'a')
['a']
>>> #creo que como inserte o conecte dos 'a' seguidas quiza por eso me diga que su longiutd es a, pero este es la manera en euq ese puede medir la longitud de una Pila.
