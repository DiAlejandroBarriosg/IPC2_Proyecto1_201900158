from LMatriz import LMatriz


class Paciente:

    def __init__(self, nombre, edad, tamano, periodos) -> None:
        self.nombre = nombre
        self.edad = edad
        self.tamano = tamano
        self.periodos = periodos
        self.listaMatriz = LMatriz()