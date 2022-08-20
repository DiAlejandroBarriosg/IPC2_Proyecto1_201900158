from NodoDoble import NodoDoble
class ListaDobleColum:

    def __init__(self) -> None:
        self.primero = None

    def vacia(self):
        return self.primero == None

    def insertar(self, columnas):
        if self.vacia():
            self.primero = NodoDoble(datos=columnas)
        else:
            actual = NodoDoble(datos=columnas, siguiente=self.primero)
            self.primero.anterior = actual
            self.primero = actual

    def recorrer(self):
        if self.vacia():
            return

        actual = self.primero
        print(f'Fila: {actual.datos}')

        while actual != None:
            actual = actual.siguiente
            print(f'Fila: {actual.datos}')