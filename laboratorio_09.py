##------------ Lista simple Circular ------------
class listaCircular():
    class Nodo ():
        def __init__(self, dato):
            self.dato = dato
            self.siguiente = None
    
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    def esVacio(self):
        return self.primero == None
    
    def AgregarInicio(self, dato):
        if self.esVacio():
            self.primero = self.ultimo = self.Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            auxiliar = self.Nodo(dato)
            auxiliar.siguiente = self.primero
            self.primero = auxiliar
            self.ultimo.siguiente = self.primero

    def AgregarFinal(self, dato):
        if self.esVacio():
            self.primero = self.ultimo = self.Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            auxiliar = self.ultimo
            self.ultimo = auxiliar.siguiente = self.Nodo(dato)
            self.ultimo.siguiente = self.primero
      
    def EliminarInicio(self, dato):
        if self.esVacio():
            print ('Vacio')
        
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        
        else:
            self.primero = self.primero.siguiente
    
    def EliminarFinal(self):
        if self.esVacio():
            print('Vacio')
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            auxiliar = self.primero
            while auxiliar.siguiente != self.ultimo:
                auxiliar = auxiliar.siguiente
            auxiliar.siguiente = self.primero
            self.ultimo = auxiliar
            
    def agregarDespues(self, dato, valor):
        nodo = self.Nodo(valor)
        auxiliar = self.primero
        while auxiliar.dato != dato:
            auxiliar = auxiliar.siguiente
        nodo.siguiente = auxiliar.siguiente
        auxiliar.siguiente = nodo
        
    def agregarAntes (self, dato, valor):
        nodo = self.Nodo(valor)
        auxiliar = self.primero
        auxiliar2 = self.primero
        while auxiliar2.dato != dato:
            auxiliar2 = auxiliar
            auxiliar = auxiliar.siguiente

    def Recorrer(self):
        cadena = ""
        auxiliar = self.primero
        while auxiliar:
            cadena += str(auxiliar.dato)
            cadena += '--->'
            auxiliar = auxiliar.siguiente
            if auxiliar == self.primero:
                cadena += str(auxiliar.dato)
                break
            return cadena

miLista = listaCircular()
"""Agrega al inico"""
miLista.AgregarInicio(10)
"""Agrega al final"""
miLista.AgregarFinal(20)
miLista.AgregarFinal(30)
"""Eliminar inicio"""
miLista.EliminarInicio()
"""Eliminar final"""
miLista.EliminarFinal()
"""Agregar despues de ..."""
miLista.agregarDespues(10, 15)
"""Agregar antes"""
miLista.agregarAntes(30, 25)
print(miLista.Recorrer())