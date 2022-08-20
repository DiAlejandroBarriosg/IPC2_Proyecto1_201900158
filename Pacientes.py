from NodoSimple import NodoSimple

class Pacientes:

    def __init__(self) -> None:
        self.primero = None

    def vacia(self):
        return self.primero == None

    def agregarAlPrincipio(self, paciente):
        if self.vacia():
            self.primero = NodoSimple(datos=paciente)
            return

        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = NodoSimple(datos=paciente)

    def recorrer(self):
        actual = self.primero
        while actual != None:
            cantidad = actual.datos.listaMatriz.leng()
            print(f'Nombre: {actual.datos.nombre}, Edad: {actual.datos.nombre}, Periodos: {actual.datos.periodos}, Matrices: {cantidad}')
            actual = actual.siguiente