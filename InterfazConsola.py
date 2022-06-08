#menu
#Modulo para crear las funciones de impresion por pantalla para el usuario
from os import system as dossystem  #añadida para limpiar consola
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
    opciones = 6
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|               Agregar Información                        |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Agregar Materias                                      |")
    print("| 2. Agregar Profesores                                    |")
    print("| 3. Agregar Grupos                                        |")
    print("| 4. Agregar Estudiantes                                   |")
    print("| 5. Agregar Notas                                         |")
    print("| 0. Volver al menu anterior                               |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    



#Funcion para imprimir en pantalla el Menu Consultar
def menuConsultar():
    limpiapantalla()
    opciones = 7
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|               Consultar Información                      |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Consultar Materias                                    |")
    print("| 2. Consultar Profesores                                  |")
    print("| 3. Consultar Grupos                                      |")
    print("| 4. Consultar Estudiantes                                 |")
    print("| 5. Consultar Notas por estudiante                        |")
    print("| 6. Consultar promedio de Notas en ciclo por estudiante   |")
    print("| 0. Volver al menu anterior                               |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    
#Funcion para imprimir en pantalla el Menu Modificar
def menuModificar():
    limpiapantalla()
    opciones = 6
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|               Modificar Información                      |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Modificar Materias                                    |")
    print("| 2. Modificar Profesores                                  |")
    print("| 3. Modificar Grupos                                      |")
    print("| 4. Modificar Estudiantes                                 |")
    print("| 5. Modificar Notas                                       |")
    print("| 0. Volver al menu anterior                               |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")

 #Funcion para imprimir en pantalla el Menu Eliminar
def menuEliminar():
    limpiapantalla()
    opciones = 6
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|               Eliminar Información                       |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Eliminar Materias                                     |")
    print("| 2. Eliminar Profesores                                   |")
    print("| 3. Eliminar Grupos                                       |")
    print("| 4. Eliminar Estudiantes                                  |")
    print("| 5. Eliminar Notas                                        |")
    print("| 0. Volver al menu anterior                               |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")

 #Funcion para imprimir en pantalla el subMenu Consultar Materias
def ConsultarMaterias():
    limpiapantalla()
    opciones = 6
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|               Consultar materias                         |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Listado de materias                                   |")
    print("| 2. Materias por ciclo                                    |")
    print("| 3. Profesores por materia                                |")
    print("| 4. Estudiantes por materia                               |")
    print("| 9. Volver al menu anterior                               |")
    print("| 0. Volver al menu principal                              |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    

 #Funcion para imprimir en pantalla el subMenu Consultar Profesores
def ConsultarProfesores():
    limpiapantalla()
    opciones = 6
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|               Consultar Profesores                       |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Listado de Profesores                                 |")
    print("| 2. Profesores por ciclo                                  |")
    print("| 3. Materias de profesores                                |")
    print("| 4. Estudiantes de profesores                             |")
    print("| 9. Volver al menu anterior                               |")
    print("| 0. Volver al menu principal                              |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")

 #Funcion para imprimir en pantalla el subMenu Consultar Grupos
def ConsultarGrupos():
    limpiapantalla()
    opciones = 4
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|                   Consultar Grupos                       |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Listado de Grupos                                     |")
    print("| 2. Estudiantes por grupos                                |")
    print("| 9. Volver al menu anterior                               |")
    print("| 0. Volver al menu principal                              |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")


 #Funcion para imprimir en pantalla el subMenu Consultar Estudiantes
def ConsultarEstudiantes():
    limpiapantalla()
    opciones = 6
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|                   Consultar estudiantes                  |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Listado general de Estudantes                         |")
    print("| 2. Listado de Estudiantes por materia                    |")
    print("| 3. Listado de estudiantes por grupo                      |")
    print("| 4. Listado de estudantes con notas aprobad               |")
    print("| 9. Volver al menu anterior                               |")
    print("| 0. Volver al menu principal                              |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
#Se crea un diccionario con la ruta y lista de las funciones de los menus para ser llamadas automaticamente
DicMenu = {(0,)   : menuInicial,
           (0,1)  : menuAgregar,     #0 es el menu principal y 1 es la opcion 1 Agregar del menu principal por tanto la llave de esta funcion es (0,1)
           (0,2)  : menuConsultar,
           (0,2,1) : ConsultarMaterias,
           (0,2,2) : ConsultarProfesores,
           (0,2,3) : ConsultarGrupos,
           (0,2,4) : ConsultarEstudiantes,
           (0,3) : menuModificar,
           (0,4)  : menuEliminar,
    }
