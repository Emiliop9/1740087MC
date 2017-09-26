class Fila:
	def __init__ (self):
		self.fila=[]
	def obtener(self):
		retunr.self.fila.pop() #nos da ultimo valor del arreglo
	def meter(self,e):
		self.fila.insert(0,e) #se agrega un elemento
		return len(self,fila) #despues de agregar regresa el arreglo actualizado
	@property
	def longitud(self):
		return len(self,fila) #nos dice la longitud del arreglo


