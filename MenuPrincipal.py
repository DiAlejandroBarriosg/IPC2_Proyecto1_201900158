import os
from colorama import Fore
import xml.etree.ElementTree as ET

class Menu():

    def __init__(self):
        self.cargar_archivo = 1
        self.graficar_patron = 2
        self.cambiar_patron = 3
        self.imprimir = 4
        self.salir = 0

    def mostrar_menu(self) -> None:
        """
        Función que limpia la pantalla y muestra nuevamente el menu
        """
        os.system('cls')  # NOTA para windows tienes que cambiar clear por cls
        print(Fore.CYAN, f'''\t<--Menu Principal-->\n
Selecciona una opción:\n
    \t{self.cargar}) - Cargar Archivo 
    \t{self.graficar_patron}) - Graficar Patron
    \t{self.cambiar_patron}) - Cambiar Patron
    \t{self.imprimir}) - Imprimir Acción
    \t{self.salir}) - Salir\n''')

    def menu(self) -> bool:
        while True:

            self.mostrar_menu()

            opcionMenu = input("Inserta el numero de la opcion: >> ")

            try:
                opcionMenu = int(opcionMenu)

                os.system('cls')

                if opcionMenu == self.cargar:
                    pass
                elif opcionMenu == self.cambiar_patron:
                    opcPiso = ''
                elif opcionMenu == self.salir:
                    print("\nEsto no es un adios sino un asta pronto!!!!!!\n")
                    False
                    break
                else:
                    print(Fore.YELLOW, 'Opcion no válida...')
                input('\nPresiona enter para Ingresar al Menú...')

            except ValueError as error:
                opcionMenu = -1
                print(Fore.RED, f'Error: {error}')
                print(Fore.RED, 'El programa no permite carateres tipo Caracter')
                input('Presione la tecla para continuar@')