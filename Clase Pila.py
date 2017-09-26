class Pila:
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


p=Pila()
p.meter(1)
p.meter(2)
p.meter(2)
p.meter(3)

print(p.longitud)
print(p.obtener())

