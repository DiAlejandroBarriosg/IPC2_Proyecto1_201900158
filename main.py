from Paciente import Paciente
from Filas import Filas
from Matriz import Matriz
from Pacientes import Pacientes
from ListaDobleFila import ListaDobleFila
from ListaDobleColum import ListaDobleColum


columnas = ListaDobleColum()
columnas.insertar(1)
columnas.insertar(2)
columnas.insertar(3)

filas = Filas(1)
filas.lista_columnas.insertar(columnas)
matriz = Matriz(1)
matriz.lita_filas.insertar(filas)

paciente1 = Paciente('Juan','23','10','6')
paciente1.listaMatriz.agregar_principio(matriz)


matrices = Pacientes()

matrices.agregarAlPrincipio(paciente1)


matrices.recorrer()