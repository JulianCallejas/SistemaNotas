#menu
#Modulo para crear las funciones de impresion por pantalla para el usuario
import pandas as pd
from os import system as dossystem  #añadida para limpiar consola
dossystem('mode con: cols=175 lines=1500')

Version = "SNApp V1.0"
#Funcion para limpiar la pantalla cada vez que se abre un menu o un informe
def limpiapantalla():
    try:
        dossystem("cls")
    except :
        pass

#Funcion para imprimir en pantalla el Menu principal  (0,)
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
    print("| 99. Salir de la aplicación                               |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    return opciones

#Funcion para imprimir en pantalla el Menu Agregar (0,1)
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
    return opciones

#Funcion para imprimir en pantalla el Menu Consultar (0,2)
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
    print("| 5. Consultar Notas                                       |")
    print("| 0. Volver al menu anterior                               |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    return opciones

#Funcion para imprimir en pantalla el subMenu Consultar Materias (0,2,1)
def menuConsultarMaterias():
    limpiapantalla()
    opciones = 6
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|               Consultar Materias                         |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Listado de materias                                   |")
    print("| 2. Materias por ciclo                                    |")
    print("| 3. Profesores por materia                                |")
    print("| 0. Volver al menu anterior                               |")
    print("| 9. Volver al menu principal                              |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    return opciones

#Funcion para imprimir Lista de Materias (0,2,1,1)
def InformeListadoMaterias(tblMaterias ):
    tblMaterias = tblMaterias.set_index('IDMateria')
    limpiapantalla()
    opciones = 20
    print(Version)
    print(" --------------------------------------------------------- ")
    print("|                   LISTADO MATERIAS                      |")
    print(" --------------------------------------------------------- ")
    print(tblMaterias,"\n")
    print(" --------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                              |")
    print("| 9. Volver al menu principal                             |")
    print(" --------------------------------------------------------- ")
    return opciones

#Funcion para imprimir Lista de Materias (0,2,1,2)
def InformeMateriasXCiclo(informe, tblMaterias):
    limpiapantalla()
    opciones = 20
    print(Version)
    print(" --------------------------------------------------------- ")
    print("|             LISTADO MATERIAS POR CICLO                  |")
    print(" --------------------------------------------------------- ")
    print(informe(tblMaterias),"\n")
    print(" --------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                              |")
    print("| 9. Volver al menu principal                             |")
    print(" --------------------------------------------------------- ")
    return opciones

#Funcion para imprimir Lista de Profesores X Materia (0,2,1,3)
def InformeProfesoresXMateria(informe, tblProfesores, tblMaterias ):
    limpiapantalla()
    listado = informe(tblProfesores,tblMaterias).sort_values(by = ['Materia','Nombre'])
    listado = listado.reset_index()
    listado = listado.set_index(['IDMateria','Materia','Nombre'])
    opciones = 20
    print(Version)
    print(" --------------------------------------------------------------------- ")
    print("|               LISTADO DE PROFESORES POR MATERIA                     |")
    print(" --------------------------------------------------------------------- ")
    print(listado,"\n")
    print(" --------------------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                                          |")
    print("| 9. Volver al menu principal                                         |")
    print(" --------------------------------------------------------------------- ")
    return opciones

 #Funcion para imprimir en pantalla el subMenu Consultar Profesores (0,2,2)
def menuConsultarProfesores():
    limpiapantalla()
    opciones = 6
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|               Consultar Profesores                       |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Listado de Profesores                                 |")
    print("| 2. Grupos activos por profesor                           |")
    print("| 0. Volver al menu anterior                               |")
    print("| 9. Volver al menu principal                              |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    return opciones

#Funcion para imprimir Listado de Profesores (0,2,2,1)
def InformeListadoProfesores(informe, tblProfesores, tblMaterias ):
    limpiapantalla()
    listado = informe(tblProfesores,tblMaterias).sort_values(by = ['Nombre','Materia'])
    listado = listado.reset_index()
    listado = listado.set_index(['IDProfesor','Nombre','Materia'])
    opciones = 20
    print(Version)
    print(" --------------------------------------------------------------------- ")
    print("|               LISTADO DE PROFESORES POR MATERIA                     |")
    print(" --------------------------------------------------------------------- ")
    print(listado,"\n")
    print(" --------------------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                                          |")
    print("| 9. Volver al menu principal                                         |")
    print(" --------------------------------------------------------------------- ")
    return opciones

#Funcion para imprimir Listado de Profesores (0,2,2,2)
def InformeGruposActivosXProfesor(informe, tblEstudiantes, tblGrupos, tblProfesores):
    limpiapantalla()
    listado = informe(tblEstudiantes, tblGrupos, tblProfesores)
    listado = listado [listado['Activ'] == 'SI']
    listado = listado [listado['IDProfe'] != 'P0']
    listado = listado.set_index(['IDProfe','Nombre Profesor','IDGrupo'])
    opciones = 20
    print(Version)
    print(" --------------------------------------------------------------------- ")
    print("|              LISTADO GRUPOS ACTIVOS POR PROFESOR                    |")
    print(" --------------------------------------------------------------------- ")
    if len(listado) > 100:
        for paginas in range(0,int(len(listado)/100)):
            ini = paginas * 100
            fin = ini + 100
            print(listado['Nombre Estudiante'].iloc[ini:fin],"\n")
    else:
        print(listado['Nombre Estudiante'],"\n")
    print(" --------------------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                                          |")
    print("| 9. Volver al menu principal                                         |")
    print(" --------------------------------------------------------------------- ")
    return opciones


#Funcion para imprimir en pantalla el subMenu Consultar Grupos (0,2,3)
def menuConsultarGrupos():
    limpiapantalla()
    opciones = 4
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|                   Consultar Grupos                       |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Listado de grupos                                     |")
    print("| 2. Listado detallado de grupos activos                   |")
    print("| 0. Volver al menu anterior                               |")
    print("| 9. Volver al menu principal                              |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    return opciones


#Funcion para imprimir Listado de Grupos (0,2,3,1)
def InformeListadoGrupos(informe, tblEstudiantes, tblGrupos, tblProfesores):
    limpiapantalla()
    listado = informe(tblEstudiantes, tblGrupos, tblProfesores)
    #listado = listado [listado['Activ'] == 'SI']
    listado = listado.sort_values(by = ['Activ','IDGrupo'], ascending=[False,True] )
    listado = listado [listado['IDProfe'] != 'P0']
    listado['Grupo'] = listado['IDGrupo']
    listado = listado.set_index(['IDGrupo', 'Periodo', 'Horario', 'Activo','IDProfe'])
    listado = listado[['Nombre Profesor','Grupo']]
    listado = listado.drop_duplicates()
    opciones = 20
    print(Version)
    print(" --------------------------------------------------------------------- ")
    print("|                       LISTADO DE GRUPOS                             |")
    print(" --------------------------------------------------------------------- ")
    if len(listado) > 100:
        for paginas in range(0,int(len(listado)/100)):
            ini = paginas * 100
            fin = ini + 100
            print(listado['Nombre Profesor'].iloc[ini:fin],"\n")
    else:
        print(listado['Nombre Profesor'],"\n")
    print(" --------------------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                                          |")
    print("| 9. Volver al menu principal                                         |")
    print(" --------------------------------------------------------------------- ")
    return opciones

#Funcion para imprimir Listado Detallado de Grupos (0,2,3,2)
def InformeListadoDetalladoGrupos(informe, tblEstudiantes, tblGrupos, tblProfesores):
    limpiapantalla()
    listado = informe(tblEstudiantes, tblGrupos, tblProfesores)
    listado = listado [listado['Activ'] == 'SI']
    listado = listado.sort_values(by = ['IDGrupo','Apellidos','Nombre Estudiante'], ascending=[True, True, True] )
    listado = listado [listado['IDProfe'] != 'P0']
    listado['Grupo'] = listado['IDGrupo']
    listado = listado.set_index(['IDGrupo', 'Horario', 'IDEstudiante'])
    listado = listado[['Nombre Estudiante', 'Apellidos']]
    listado = listado.drop_duplicates()
    opciones = 20
    print(Version)
    print(" --------------------------------------------------------------------- ")
    print("|                LISTADO DETALLADO DE GRUPOS ACTIVOS                  |")
    print(" --------------------------------------------------------------------- ")
    if len(listado) > 100:
        for paginas in range(0,int(len(listado)/100)):
            ini = paginas * 100
            fin = ini + 100
            print(listado.iloc[ini:fin],"\n")
    else:
        print(listado,"\n")
    print(" --------------------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                                          |")
    print("| 9. Volver al menu principal                                         |")
    print(" --------------------------------------------------------------------- ")
    return opciones


 #Funcion para imprimir en pantalla el subMenu Consultar Estudiantes (0,2,4)
def menuConsultarEstudiantes():
    limpiapantalla()
    opciones = 6
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|                Consultar Estudiantes                     |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Listado de Estudantes                                 |")
    print("| 2. Listado de estudiantes por grupo                      |")
    print("| 3. Listado de notas por estudiante                       |")
    print("| 4. Listado de promedios por estudiante                   |")
    print("| 0. Volver al menu anterior                               |")
    print("| 9. Volver al menu principal                              |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    return opciones

#Funcion para imprimir Listado de Estudiantes (0,2,4,1) 
def InformeListadoDeEstudiantes(informe, tblEstudiantes, tblGrupos, tblProfesores):
    limpiapantalla()
    listado = informe(tblEstudiantes, tblGrupos, tblProfesores)
    #listado = listado [listado['Activ'] == 'SI']
    listado = listado.sort_values(by = ['Apellidos','Nombre Estudiante'], ascending=[True, True] )
    listado = listado [listado['IDProfe'] != 'P0']
    listado['Grupo'] = listado['IDGrupo']
    listado = listado.set_index(['IDEstudiante'])
    listado = listado[['Nombre Estudiante', 'Apellidos','Email', 'IDGrupo', 'Activ']]
    listado = listado.drop_duplicates()
    opciones = 20
    print(Version)
    print(" --------------------------------------------------------------------- ")
    print("|                      LISTADO DE ESTUDIANTES                         |")
    print(" --------------------------------------------------------------------- ")
    if len(listado) > 100:
        for paginas in range(0,int(len(listado)/100)):
            ini = paginas * 100
            fin = ini + 100
            print(listado.iloc[ini:fin],"\n")
    else:
        print(listado,"\n")
    print(" --------------------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                                          |")
    print("| 9. Volver al menu principal                                         |")
    print(" --------------------------------------------------------------------- ")
    return opciones

#Funcion para imprimir Lista de Estudiantes por Grupo (0,2,4,2)
def InformeEstudiantesXGrupo(informe, tblEstudiantes, tblGrupos ):
    limpiapantalla()
    listado = informe(tblEstudiantes,tblGrupos)
    listado = listado.reset_index()
    listado = listado.sort_values(by = ['IDGrupo','Apellidos','Nombres'])
    listado = listado.set_index(['IDGrupo','Apellidos','Nombres'])
    opciones = 20
    print(Version)
    print(" --------------------------------------------------------------------- ")
    print("|               LISTADO DE ESTUDIANTES POR GRUPO                      |")
    print(" --------------------------------------------------------------------- ")
    print(listado["IDEstudiante"],"\n")
    print(" --------------------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                                          |")
    print("| 9. Volver al menu principal                                         |")
    print(" --------------------------------------------------------------------- ")
    return opciones

#Funcion para imprimir Listado Notas por Estudiante (0,2,4,3) InformeListadoNotasXEstudiantes
def InformeListadoNotasXEstudiantes(informe, tblEstudiantes, tblGrupos, tblProfesores):
    limpiapantalla()

    print(Version)
    print(" --------------------------------------------------------------------- ")
    print("|                 LISTADO NOTAS POR ESTUDIANTES                       |")
    print(" --------------------------------------------------------------------- ")
    IdEstu = input("Ingrese el codigo del estudiante a consultar: ").upper()
    
    
    listado = informe(tblEstudiantes, tblGrupos, tblProfesores, IdEstu)
    #listado = listado [listado['Activ'] == 'SI']
    listado = listado.sort_values(by = ['Ciclo', 'IDMateria'], ascending=[True,True] )
    #listado = listado [listado['IDProfe'] != 'P0']
    listado = listado.set_index(['Nombres', 'Apellidos','Ciclo', 'Materia'])
    listado = listado[['Nota']]
    listado = listado.drop_duplicates()
    opciones = 20
    if len(listado) > 100:
        for paginas in range(0,int(len(listado)/100)):
            ini = paginas * 100
            fin = ini + 100
            print(listado.iloc[ini:fin],"\n")
    else:
        print(listado,"\n")
    print(" --------------------------------------------------------------------- ")
    print("| Enter para Consultar nuevo estudiante                               |")
    print("| 0. Volver al menu anterior                                          |")
    print("| 9. Volver al menu principal                                         |")
    print(" --------------------------------------------------------------------- ")
    return opciones


 #Funcion para imprimir en pantalla el subMenu Consultar Notas (0,2,5)
def menuConsultarNotas():
    limpiapantalla()
    opciones = 6
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|                   Consultar Notas                        |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Matriz general de notas                               |")
    print("| 2. Listado de notas por grupo                            |")
    print("| 3. Listado de notas por estudiante                       |")
    print("| 4. Listado de promedios ciclo por estudiante             |")
    print("| 0. Volver al menu anterior                               |")
    print("| 9. Volver al menu principal                              |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    return opciones


#Funcion para imprimir en pantalla el Menu Modificar (0,3)
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
    return opciones

 #Funcion para imprimir en pantalla el Menu Eliminar (0,4)
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
    return opciones
    
#Funcion para imprimir en pantalla que fallo el cargue de informacion
def menuFallaCarga():
    print(" ---------------------------------------------------------- ")
    print("|          !Error al cargar la informacion!                |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1.  Oprima 1 para cerrar la aplicacion                   |")
    print("|     Puede revisar los archivos con extension .csv y      |")
    print("|     verificar si hace falta alguno o alguno esta dañado  |")
    print("|                                                          |")
    print("| 99. oprima 99 si desea crear una base de datos nueva     |")
    print("|     tenga en cuenta que perdera toda la informacion      |")
    print("|     que contengan todos los archivos                     |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")


#Se crea un diccionario con la ruta y lista de las funciones de los menus para ser llamadas automaticamente
DicMenu = {(0,)   :     menuInicial,
           (0,1)  :     menuAgregar,     #0 es el menu principal y 1 es la opcion 1 Agregar del menu principal por tanto la llave de esta funcion es (0,1)
           (0,2)  :     menuConsultar,
           (0,2,1) :    menuConsultarMaterias,
          #(0,2,1,1):   (ic.InformeListadoMaterias,tblMaterias),
          #(0,2,1,2):   (ic.InformeMateriasXCiclo,crud.consultaMateriasXCiclo,tblMaterias),
          #(0,2,1,3):   (ic.InformeProfesoresXMateria, crud.consultaMateriasXProfesor)
           (0,2,2) :    menuConsultarProfesores,
          #(0,2,2,1) :  (ic.InformeListadoProfesores, crud.consultaMateriasXProfesor, tblProfesores, tblMaterias ),
          #(0,2,2,2) :  InformeGruposActivosXProfesor
           (0,2,3) :    menuConsultarGrupos,
          #(0,2,3,1) :  (ic.InformeListadoGrupos, crud.consultaEstudiantesXProfesor,tblEstudiantes, tblGrupos, tblProfesores),
          #(0,2,3,2) :  (ic.InformeListadoDetalladoGrupos, crud.consultaEstudiantesXProfesor,tblEstudiantes, tblGrupos, tblProfesores),
           (0,2,4) :    menuConsultarEstudiantes,
          #(0,2,4,1) :  (ic.InformeListadoDeEstudiantes, crud.consultaEstudiantesXProfesor,tblEstudiantes, tblGrupos, tblProfesores),
          #(0,2,4,2):   (ic.InformeEstudiantesXGrupo, crud.consultaEstudiantesXGrupo ,tblEstudiantes,tblGrupos),
          #(0,2,4,3) :  (ic.InformeListadoNotasXEstudiantes, crud.consultaNotas, tblEstudiantes, tblNotas, tblMaterias),
           (0,2,5) :    menuConsultarNotas,
           (0,3)   :    menuModificar,
           (0,4)   :    menuEliminar,
    }

#Menu para modificar materias (0,3,1)
def menuModificarMaterias (tblMaterias:pd.DataFrame,existeID):
    opciones = 5
    
    print(" ---------------------------------------------------------- ")
    print("|                 Modificar de materias                      |")
    print(" ---------------------------------------------------------- ")
    print(tblMaterias.set_index("IDMateria"))
    print(" ---------------------------------------------------------- ")

    id = str(input("Ingrese el id de la materia para modificar: "))
    
    #Revisar si se encuentra el elemento solicitado     
    if existeID(tblMaterias, "IDMateria", id):

        #Recolectar los nuevos datos        
        nuevaMateria = str(input("Nueva Materia: "))
        if nuevaMateria == "":
            nuevaMateria = tblMaterias.set_index("IDMateria")["Materia"][id]
                        
        nuevoCiclo = str(input("Nuevo Ciclo: "))
        if nuevoCiclo == "":
            nuevoCiclo = tblMaterias.set_index("IDMateria")["Ciclo"][id]
                
        nuevoCreditos = str(input("Nuevo número de creditos: "))     
        if nuevoCreditos == "":
            nuevoCreditos = tblMaterias.set_index("IDMateria")["Creditos"][id]
                
        materiaActualizada = [id, nuevaMateria, nuevoCiclo, nuevoCreditos ]   

    else:
        print("No ha sido encontrada la Materia para modificar!")
        
    print(" --------------------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                                          |")
    print("| 9. Volver al menu principal                                         |")
    print(" --------------------------------------------------------------------- ")
    
    return opciones
# Menu para modificar profesores (0,3,2)
def menuModificarProfesores(tblProfesores:pd.DataFrame,existeID):
    
    opciones = 5
    
    print(" ---------------------------------------------------------- ")
    print("|               Listado de profesores                      |")
    print(" ---------------------------------------------------------- ")
    print(tblProfesores.set_index("IDProfesor"))
    print(" ---------------------------------------------------------- ")

    id = str(input("Ingrese el id del profesor para modificar: "))
       
    #Revisar si se encuentra el elemento solicitado     
    if existeID(tblProfesores, "IDProfesor", id):

        #Recolectar los nuevos datos        
        nuevoNombre = str(input("Nuevo nombre: "))
        if nuevoNombre == "":
            nuevoNombre = tblProfesores.set_index("IDProfesor")["Nombre"][id]
                        
        nuevoIDMateria = str(input("Nuevo IDMateria: "))
        if nuevoIDMateria == "":
            nuevoIDMateria = tblProfesores.set_index("IDProfesor")["IDMateria"][id]
                
        materiaActualizada = [id, nuevoNombre, nuevoIDMateria ]   

    else:
        print("No ha sido encontrada el profesor para modificar!")
        
    print(" --------------------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                                          |")
    print("| 9. Volver al menu principal                                         |")
    print(" --------------------------------------------------------------------- ")
    
    return opciones
