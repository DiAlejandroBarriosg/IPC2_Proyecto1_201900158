from NodoSimple import NodoSimple


class LMatriz:

    def __init__(self) -> None:
        self.primero = None
        self.long = 0

    def leng (self):
        return self.long

    def vacia (self):
        return self.primero == None

    def agregar_principio (self, matrices):
        if self.vacia():
            self.primero = NodoSimple(datos=matrices)
            self.long += 1
            return

        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = NodoSimple(datos=matrices)
        self.long += 1

    def recorrer (self):
        actual = self.primero
        while actual != None:
            print('Id: ', actual.datos.id)
            actual = actual.siguiente