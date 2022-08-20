from NodoDoble import NodoDoble

class ListaDobleFila:

    def __init__(self) -> None:
        self.primero = None

    def vacia(self):
        return self.primero == None

    def insertar(self, filas):
        if self.vacia():
            self.primero = NodoDoble(datos=filas)
        else:
            actual = NodoDoble(datos=filas, siguiente=self.primero)
            self.primero.anterior = actual
            self.primero = actual

    def recorrer(self):
        if self.vacia():
            return

        actual = self.primero
        print(f'Fila: {actual.datos.fila}')

        while actual != None:
            actual = actual.siguiente
            print(f'Fila: {actual.datos.fila}')