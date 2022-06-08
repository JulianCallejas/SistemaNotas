#Modulo para crear las funciones de impresion por pantalla para el usuario
from os import system as dossystem
from typing import Tuple  #añadida para limpiar consola
Version = "SNApp V1.0"
#Funcion para limpiar la pantalla cada vez que se abre un menu o un informe
def limpiapantalla():
    try:
        dossystem("cls")
    except :
        pass

#Funcion para imprimir en pantalla el Menu principal
def menuInicial():
    limpiapantalla()
    opciones = 5
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|               Menu Principal                             |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Agregar información                                   |")
    print("| 2. Consultar información                                 |")
    print("| 3. Modificar información                                 |")
    print("| 4. Eliminar información                                  |")
    print("| 5. Salir de la aplicación                                |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    
#Funcion para imprimir en pantalla el Menu Agregar
def menuAgregar():
    limpiapantalla()
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|               Agregar Informacion                        |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Agregar Materias                                      |")
    print("| 2. Agregar Profesores                                    |")
    print("| 3. Agregar Grupos                                        |")
    print("| 4. Agregar Estudiantes                                   |")
    print("| 5. Agregar Notas                                         |")
    print("| 6. Volver al menu anterior                               |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    
#Se crea un diccionario con la ruta y lista de las funciones de los menus para ser llamadas automaticamente
DicMenu = {(0,)   : menuInicial,
           (0,1)  : menuAgregar,     #0 es el menu principal y 1 es la opcion 1 Agregar del menu principal por tanto la llave de esta funcion es (0,1)
        
    }
