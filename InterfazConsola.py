#menu
#Modulo para crear las funciones de impresion por pantalla para el usuario
import pandas as pd
import numpy as np
#Se intenta importar la libreria tabulate para tabular informes grandes sin subindices para instalar usar comando pip install tabulate
try:
    from tabulate import tabulate
    tabactive = True
except :
    tabactive = False
    
from os import system as dossystem, truncate  #añadida para limpiar consola
#dossystem('mode con: cols=175 lines=1500')

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
    print("|                     Menu Principal                       |")
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

#Funcion para pantalla Agregar Materia (0,1,1)
def menuAgregarMateria(creaID, tblMaterias, Materia, dic_materias):
    limpiapantalla()
    opciones = 1
    mater = ""
    cicl = ""
    cred = ""
    idm = ""
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|                    AGREGAR MATERIA                       |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el Nombre de la materia a agregar: ")
    while mater == "":
        mater = input("|  ")
        if mater.upper() == "SALIR":
            print(" ---------------------------------------------------------- ")
            print("|               AGREGAR MATERIA CANCELADO                  |")
            print(" ---------------------------------------------------------- ")
            print("| 0. Volver al menu anterior                               |")
            print("| 9. Volver al menu principal                              |")
            print(" ---------------------------------------------------------- ")
            return opciones
        elif mater == "":
            print("| Nombre de materia no valido")
            print("| Ingrese el nombre de la materia a agregar o escriba SALIR para cancelar: ")
    mater = mater.capitalize()
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el Ciclo en que la materia se dictara (numeros del 1 al 4): ")
    while cicl == "":
        cicl = input("|  ")
        if cicl.upper() == "SALIR":
            print(" ---------------------------------------------------------- ")
            print("|               AGREGAR MATERIA CANCELADO                  |")
            print(" ---------------------------------------------------------- ")
            print("| 0. Volver al menu anterior                               |")
            print("| 9. Volver al menu principal                              |")
            print(" ---------------------------------------------------------- ")
            return opciones
        elif cicl == "" or cicl not in ["1","2","3","4"]:
            print("| Ciclo no valido")
            print("| Ingrese el numero del ciclo entre 1, 2, 3 o 4; o escriba SALIR para cancelar: ")
            cicl = ""
    print(" ---------------------------------------------------------- ")
    print("| Ingrese los Creditos de la materia (numeros del 1 al 10): ")
    while cred == "":
        cred = input("|  ")
        if cred.upper() == "SALIR":
            print(" ---------------------------------------------------------- ")
            print("|               AGREGAR MATERIA CANCELADO                  |")
            print(" ---------------------------------------------------------- ")
            print("| 0. Volver al menu anterior                               |")
            print("| 9. Volver al menu principal                              |")
            print(" ---------------------------------------------------------- ")
            return opciones
        elif cred == "" or  cred not in ["1","2","3","4" ,"5","6","7","8","9","10"]:
            print("| Creditos no validos")
            print("| Ingrese el numero de creditos del 1 al 10; o escriba SALIR para cancelar: ")
            cred = ""
    idm = creaID(tblMaterias,"IDMateria")
    print(" --------------------------------------------------------- ")
    print("| Id Materia:", idm)
    print("| Materia:   ", mater)
    print("| Ciclo:     ", cicl)
    print("| Creditos:  ", cred)
    print(" --------------------------------------------------------- ")
    confirma = input("| Ingrese 1 para confirmar o 0 para cancelar: ")
    if confirma == '1':
            try:
                dic_materias[id] = Materia([idm,mater,cicl,cred])
                tblMaterias = dic_materias[id].agregaRegistro()
                opciones = (1,('tblMaterias',tblMaterias))
                print(" --------------------------------------------------------------------- ")
                print("| REGISTRO GUARDADO CON EXITO                                         |")
                print(" --------------------------------------------------------------------- ")
            except:
                print(" --------------------------------------------------------------------- ")
                print("| ERROR AL GUARDAR LA INFORMACION, REVISE LOS DATOS INGRESADOS        |")
                print(" --------------------------------------------------------------------- ")
    print(" --------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                              |")
    print("| 9. Volver al menu principal                             |")
    print(" --------------------------------------------------------- ")
    return opciones

#Funcion para pantalla Agregar Grupo (0,1,2)   
def menuAgregarProfesor(crearIDProfesor, tblProfesores, Profesor,dic_profesores):
    limpiapantalla()
    opciones = 1
    IDProfesor = ""
    Nombre = ""
    IDMateria = ""
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|                    AGREGAR PROFESOR                      |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el nombre completo del profesor a agregar: ")
    while Nombre == "":
        Nombre = input("|  ")
        if Nombre.upper() == "SALIR":
            print(" ---------------------------------------------------------- ")
            print("|               AGREGAR PROFESOR CANCELADO                 |")
            print(" ---------------------------------------------------------- ")
            print("| 0. Volver al menu anterior                               |")
            print("| 9. Volver al menu principal                              |")
            print(" ---------------------------------------------------------- ")
            return opciones
        elif Nombre == "":
            print("| Nombre no valido")
            print("| Ingrese el nombre completo del profesor a agregar o escriba SALIR para cancelar: ")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el id de las materias que el profesor dictara separados por coma 1,2,5,7: ")
    while IDMateria == "":
        IDMateria = input("|  ")
        if IDMateria.upper() == "SALIR":
            print(" ---------------------------------------------------------- ")
            print("|               AGREGAR PROFESOR CANCELADO                 |")
            print(" ---------------------------------------------------------- ")
            print("| 0. Volver al menu anterior                               |")
            print("| 9. Volver al menu principal                              |")
            print(" ---------------------------------------------------------- ")
            return opciones
        elif IDMateria == "":
            print("| ID de materias no valido")
            print("| Ingrese el id de las materias que el profesor dictara separados por coma 1,2,5,7; o escriba SALIR para cancelar: ")
            IDMateria = ""
    print(" ---------------------------------------------------------- ")
    IDProfesor = crearIDProfesor(dic_profesores)
    print(IDProfesor)
    print(" --------------------------------------------------------- ")
    print("| Id Profesor:   ", IDProfesor)
    print("| Nombre:        ", Nombre)
    print("| ID Materias:   ", IDMateria)
    print(" --------------------------------------------------------- ")
    confirma = input("| Ingrese 1 para confirmar o 0 para cancelar: ")
    if confirma == '1':
            try:
                dic_profesores[IDProfesor] = Profesor([IDProfesor,Nombre,IDMateria])
                tblProfesores = dic_profesores[IDProfesor].agregaRegistro()
                opciones = (1,('tblProfesores',tblProfesores))
                print(" --------------------------------------------------------------------- ")
                print("| REGISTRO GUARDADO CON EXITO                                         |")
                print(" --------------------------------------------------------------------- ")
            except:
                print(" --------------------------------------------------------------------- ")
                print("| ERROR AL GUARDAR LA INFORMACION, REVISE LOS DATOS INGRESADOS        |")
                print(" --------------------------------------------------------------------- ")
    print(" --------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                              |")
    print("| 9. Volver al menu principal                             |")
    print(" --------------------------------------------------------- ")
    return opciones

#Funcion para pantalla Agregar Grupo (0,1,3) 
def menuAgregarGrupo(creaID, tblGrupos, Grupo, dic_grupos):
    limpiapantalla()
    opciones = 1
    Periodo = ""
    Horario = ""
    Activo = "1"
    IDMaterias = 0
    IDProfesores = ""
    IDGrupo = ""
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|                     AGREGAR GRUPO                        |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el periodo (año) de estudio del grupo: ")
    while Periodo == "":
        Periodo = input("|  ")
        if Periodo.upper() == "SALIR":
            print(" ---------------------------------------------------------- ")
            print("|                AGREGAR GRUPO CANCELADO                   |")
            print(" ---------------------------------------------------------- ")
            print("| 0. Volver al menu anterior                               |")
            print("| 9. Volver al menu principal                              |")
            print(" ---------------------------------------------------------- ")
            return opciones
        elif Periodo == "":
            print("| Periodo no valido")
            print("| Ingrese el periodo (año) de estudio del grupo o escriba SALIR para cancelar: ")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese la franja horaria de estudio mañana, tarde, noche: ")
    while Horario == "":
        Horario = input("|  ").lower()
        if Horario.upper() == "SALIR":
            print(" ---------------------------------------------------------- ")
            print("|                AGREGAR GRUPO CANCELADO                   |")
            print(" ---------------------------------------------------------- ")
            print("| 0. Volver al menu anterior                               |")
            print("| 9. Volver al menu principal                              |")
            print(" ---------------------------------------------------------- ")
            return opciones
        elif Horario == "" or Horario not in ["mañana","tarde","noche"]:
            print("| Horario no valido")
            print("| Ingrese la franja horaria de estudio mañana, tarde, noche; o escriba SALIR para cancelar: ")
            Horario = ""
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el ID de las materias a cursar en orden ")
    print("| el orden predeterminado es: 1,5,9,2,6,10,3,7,11,4,8,12")
    print("| si desea conservar este orden oprima enter, de lo contrario ingrese el nuevo orden:")
    while IDMaterias == 0:
        IDMaterias = input("|  ")
        if IDMaterias.upper() == "SALIR":
            print(" ---------------------------------------------------------- ")
            print("|                AGREGAR GRUPO CANCELADO                   |")
            print(" ---------------------------------------------------------- ")
            print("| 0. Volver al menu anterior                               |")
            print("| 9. Volver al menu principal                              |")
            print(" ---------------------------------------------------------- ")
            return opciones
        elif IDMaterias == "" :
            IDMaterias = "1,5,9,2,6,10,3,7,11,4,8,12"
        elif IDMaterias == 0:
            print("| Materias no validas")
            print("| Ingrese el ID de las materias a cursar en orden; o escriba SALIR para cancelar: ")
            IDMaterias = 0
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el ID de los profesores que dictaran las materias en el mismo orden de las materias:")
    while IDProfesores == "":
        IDProfesores = input("|  ").upper()
        if IDProfesores.upper() == "SALIR":
            print(" ---------------------------------------------------------- ")
            print("|                AGREGAR GRUPO CANCELADO                   |")
            print(" ---------------------------------------------------------- ")
            print("| 0. Volver al menu anterior                               |")
            print("| 9. Volver al menu principal                              |")
            print(" ---------------------------------------------------------- ")
            return opciones
        elif IDProfesores == "":
            print("| Profesores no validos")
            print("| Ingrese el ID de los profesores que dictaran las materias en el mismo orden de las materias")
            print("| o escriba SALIR para cancelar: ")
            IDProfesores = ""
    IDGrupo = creaID(tblGrupos,"IDGrupo")
    print(" --------------------------------------------------------- ")
    print("| ID Grupo:      ", IDGrupo )
    print("| Periodo:       ", Periodo )
    print("| Horario:       ", Horario)
    print("| Activo:        ", Activo)
    print("| ID Materias:   ", IDMaterias)
    print("| ID Profesores: ", IDProfesores)
    print(" --------------------------------------------------------- ")
    confirma = input("| Ingrese 1 para confirmar o 0 para cancelar: ")
    if confirma == '1':
            try:
                dic_grupos[IDGrupo] = Grupo([IDGrupo, Periodo, Horario, Activo, IDMaterias, IDProfesores])
                tblGrupos = dic_grupos[IDGrupo].agregaRegistro()
                opciones = (1,('tblGrupos',tblGrupos))
                print(" --------------------------------------------------------------------- ")
                print("| REGISTRO GUARDADO CON EXITO                                         |")
                print(" --------------------------------------------------------------------- ")
            except:
                print(" --------------------------------------------------------------------- ")
                print("| ERROR AL GUARDAR LA INFORMACION, REVISE LOS DATOS INGRESADOS        |")
                print(" --------------------------------------------------------------------- ")
    print(" --------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                              |")
    print("| 9. Volver al menu principal                             |")
    print(" --------------------------------------------------------- ")
    return opciones

#Funcion para pantalla Agregar Estudiante (0,1,4)   IDEstudiante;Nombres;Apellidos;Email;IDGrupo
def menuAgregarEstudiante(creaID, tblEstudiantes, Estudiante, dic_estudiantes):
    limpiapantalla()
    opciones = 1
    Nombres = ""
    Apellidos = ""
    Email = ""
    IDGrupo = ""
    IDEstudiante = ""
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|                   AGREGAR ESTUDIANTE                     |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el nombre del estudiante: ")
    while Nombres == "":
        Nombres = input("|  ")
        if Nombres.upper() == "SALIR":
            print(" ---------------------------------------------------------- ")
            print("|             AGREGAR ESTUDIANTE CANCELADO                 |")
            print(" ---------------------------------------------------------- ")
            print("| 0. Volver al menu anterior                               |")
            print("| 9. Volver al menu principal                              |")
            print(" ---------------------------------------------------------- ")
            return opciones
        elif Nombres == "":
            print("| Nombres no valido")
            print("| Ingrese el nombre del estudiante o escriba SALIR para cancelar: ")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese los apellidos del estudiante: ")
    while Apellidos == "":
        Apellidos = input("|  ")
        if Apellidos.upper() == "SALIR":
            print(" ---------------------------------------------------------- ")
            print("|             AGREGAR ESTUDIANTE CANCELADO                 |")
            print(" ---------------------------------------------------------- ")
            print("| 0. Volver al menu anterior                               |")
            print("| 9. Volver al menu principal                              |")
            print(" ---------------------------------------------------------- ")
            return opciones
        elif Apellidos == "":
            print("| Apellidos no valido")
            print("| Ingrese los apellidos del estudiante o escriba SALIR para cancelar: ")
            Apellidos = ""
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el Email del estudiante: ")
    while Email == "":
        Email = input("|  ")
        if Email.upper() == "SALIR":
            print(" ---------------------------------------------------------- ")
            print("|             AGREGAR ESTUDIANTE CANCELADO                 |")
            print(" ---------------------------------------------------------- ")
            print("| 0. Volver al menu anterior                               |")
            print("| 9. Volver al menu principal                              |")
            print(" ---------------------------------------------------------- ")
            return opciones
        elif Email == "" or "@" and "." not in Email:
            print("| Email no valido")
            print("| Ingrese el Email del estudiante o escriba SALIR para cancelar: ")
            Email = ""
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el ID del grupo al que asignara al estudiante:")
    while IDGrupo == "":
        IDGrupo = input("|  ").upper()
        if IDGrupo.upper() == "SALIR":
            print(" ---------------------------------------------------------- ")
            print("|             AGREGAR ESTUDIANTE CANCELADO                 |")
            print(" ---------------------------------------------------------- ")
            print("| 0. Volver al menu anterior                               |")
            print("| 9. Volver al menu principal                              |")
            print(" ---------------------------------------------------------- ")
            return opciones
        elif IDGrupo == "" or not IDGrupo.isnumeric():
            print("| Grupo no valido")
            print("| Ingrese el ID del grupo al que asignara al estudiante o escriba SALIR para cancelar: ")
            IDGrupo = ""
    IDEstudiante = creaID(dic_estudiantes, Nombres, Apellidos)
    print(" --------------------------------------------------------- ")
    print("| ID Estudiante: ", IDEstudiante )
    print("| Nombres:       ", Nombres )
    print("| Apellidos:     ", Apellidos)
    print("| Email:         ", Email)
    print("| Grupo:         ", IDGrupo)
    print(" --------------------------------------------------------- ")
    confirma = input("| Ingrese 1 para confirmar o 0 para cancelar: ")
    if confirma == '1':
            try:
                dic_estudiantes[IDEstudiante] = Estudiante([IDEstudiante, Nombres, Apellidos, Email, IDGrupo])
                tblEstudiantes = dic_estudiantes[IDEstudiante].agregaRegistro()
                opciones = (1,('tblEstudiantes',tblEstudiantes))
                print(" --------------------------------------------------------------------- ")
                print("| REGISTRO GUARDADO CON EXITO                                         |")
                print(" --------------------------------------------------------------------- ")
            except:
                print(" --------------------------------------------------------------------- ")
                print("| ERROR AL GUARDAR LA INFORMACION, REVISE LOS DATOS INGRESADOS        |")
                print(" --------------------------------------------------------------------- ")
    print(" --------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                              |")
    print("| 9. Volver al menu principal                             |")
    print(" --------------------------------------------------------- ")
    return opciones

#Funcion para pantalla Agregar Nota (0,1,5)  IdNota;IDEstudiante;Nota;IDMateria
def menuAgregarNota(creaID, tblNotas, Nota, dic_notas, dic_estudiantes, dic_materias):
    limpiapantalla()
    opciones = 1
    IDEstudiante = ""
    IDMateria = ""
    calificacion = ""
    IdNota = ""
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|                     AGREGAR NOTA                         |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el Id del estudiante: ")
    while IDEstudiante == "":
        IDEstudiante = input("|  ").upper()
        if IDEstudiante.upper() == "SALIR":
            print(" ---------------------------------------------------------- ")
            print("|                 AGREGAR NOTA CANCELADO                   |")
            print(" ---------------------------------------------------------- ")
            print("| 0. Volver al menu anterior                               |")
            print("| 9. Volver al menu principal                              |")
            print(" ---------------------------------------------------------- ")
            return opciones
        elif IDEstudiante == "" or IDEstudiante not in dic_estudiantes.keys() :
            print("| ID de estudiante no valido")
            print("| Ingrese el Id del estudiante o escriba SALIR para cancelar: ")
            IDEstudiante = ""
    print("| ", dic_estudiantes[IDEstudiante] )
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el Id de la materia: ")
    while IDMateria == "":
        IDMateria = input("|  ")
        if IDMateria.upper() == "SALIR":
            print(" ---------------------------------------------------------- ")
            print("|                 AGREGAR NOTA CANCELADO                   |")
            print(" ---------------------------------------------------------- ")
            print("| 0. Volver al menu anterior                               |")
            print("| 9. Volver al menu principal                              |")
            print(" ---------------------------------------------------------- ")
            return opciones
        elif IDMateria == "" or IDMateria not in dic_materias.keys():
            print("| Id Materia no valido")
            print("| Ingrese el Id de la materia o escriba SALIR para cancelar: ")
            IDMateria = ""
    print("| ", dic_materias[IDMateria] )
    print(" ---------------------------------------------------------- ")
    print("| Ingrese la nota (entre 0 y 5): ")
    while calificacion == "":
        calificacion = input("|  ")
        if calificacion.upper() == "SALIR":
            print(" ---------------------------------------------------------- ")
            print("|                 AGREGAR NOTA CANCELADO                   |")
            print(" ---------------------------------------------------------- ")
            print("| 0. Volver al menu anterior                               |")
            print("| 9. Volver al menu principal                              |")
            print(" ---------------------------------------------------------- ")
            return opciones
        elif calificacion == "" or  float(calificacion) < 0 or  float(calificacion)> 5:
            print("| Nota no valida")
            print("| Ingrese la nota (entre 0 y 5) o escriba SALIR para cancelar: ")
            calificacion = ""
           
    IdNota = creaID(tblNotas,"IdNota")
    IdNota = str(IdNota)
    print(" --------------------------------------------------------- ")
    print("| Id Nota:       ", IdNota)
    print("| Estudiante:    ", dic_estudiantes[IDEstudiante])
    print("| Materia:       ", dic_materias[IDMateria])
    print("| Nota:          ", calificacion)
    print(" --------------------------------------------------------- ")
    confirma = input("| Ingrese 1 para confirmar o 0 para cancelar: ")
    if confirma == '1':
            try:
                dic_notas[IdNota] = Nota([IdNota,IDEstudiante,calificacion,IDMateria])
                tblNotas = dic_notas[IdNota].agregaRegistro()
                opciones = (1,('tblNotas',tblNotas))
                print(" --------------------------------------------------------------------- ")
                print("| REGISTRO GUARDADO CON EXITO                                         |")
                print(" --------------------------------------------------------------------- ")
            except:
                print(" --------------------------------------------------------------------- ")
                print("| ERROR AL GUARDAR LA INFORMACION, REVISE LOS DATOS INGRESADOS        |")
                print(" --------------------------------------------------------------------- ")
    print(" --------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                              |")
    print("| 9. Volver al menu principal                             |")
    print(" --------------------------------------------------------- ")
    return opciones

#Funcion para imprimir en pantalla el Menu Consultar (0,2)
def menuConsultar():
    limpiapantalla()
    opciones = 6
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
    opciones = 4
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
def InformeListadoMaterias(tblMaterias):
    tblMaterias = tblMaterias.set_index('IDMateria')
    limpiapantalla()
    opciones = 1
    print(Version)
    print(" --------------------------------------------------------------- ")
    print("|                   LISTADO MATERIAS                            |")
    print(" --------------------------------------------------------------- ")
    if tabactive:
        print(tabulate(tblMaterias, headers='keys', tablefmt = 'psql' ),"\n")
    else:
        print(tblMaterias,"\n")
    print(" --------------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                                    |")
    print("| 9. Volver al menu principal                                   |")
    print(" --------------------------------------------------------------- ")
    tblMaterias = tblMaterias.reset_index()
    return opciones

#Funcion para imprimir Lista de Materias (0,2,1,2)
def InformeMateriasXCiclo(informe, tblMaterias):
    limpiapantalla()
    opciones = 1
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
    opciones = 1
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
    opciones = 3
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
    opciones = 1
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
    opciones = 1
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
    print("| 1. Tabla de grupos                                       |")
    print("| 2. Listado de grupos                                     |")
    print("| 3. Listado detallado de grupos activos                   |")
    print("| 0. Volver al menu anterior                               |")
    print("| 9. Volver al menu principal                              |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    return opciones


#Funcion para imprimir Listado de Grupos (0,2,3,1)
def InformeListadoTablaGrupos(tblGrupos):
    limpiapantalla()
    tblGrupos = tblGrupos.set_index("IDGrupo")
    opciones = 1
    print(Version)
    print(" --------------------------------------------------------------------- ")
    print("|                    LISTADO TABLA DE GRUPOS                          |")
    print(" --------------------------------------------------------------------- ")
    if tabactive:
        print(tabulate(tblGrupos, headers='keys', tablefmt = 'psql' ),"\n")
    else:
        if len(tblGrupos) > 100:
            for paginas in range(0,int(len(tblGrupos)/100)):
                ini = paginas * 100
                fin = ini + 100
                print(tblGrupos['IDGrupo'].iloc[ini:fin],"\n")
        else:
            print(tblGrupos,"\n")
    print(" --------------------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                                          |")
    print("| 9. Volver al menu principal                                         |")
    print(" --------------------------------------------------------------------- ")
    tblGrupos = tblGrupos.reset_index()
    return opciones


#Funcion para imprimir Listado de Grupos (0,2,3,2)
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
    opciones = 1
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
    tblEstudiantes = tblEstudiantes.reset_index()
    tblGrupos = tblGrupos.reset_index()
    tblProfesores = tblProfesores.reset_index()
    return opciones

#Funcion para imprimir Listado Detallado de Grupos (0,2,3,3)
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
    opciones = 1
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
    opciones = 5
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
    opciones = 1
    print(Version)
    print(" --------------------------------------------------------------------- ")
    print("|                      LISTADO DE ESTUDIANTES                         |")
    print(" --------------------------------------------------------------------- ")
    if tabactive:
        print(tabulate(listado, headers='keys', tablefmt = 'psql' ),"\n")
    else:
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
    opciones = 1
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
    print("|                 LISTADO NOTAS POR ESTUDIANTE                        |")
    print(" --------------------------------------------------------------------- ")
    IdEstu = input("Ingrese el codigo del estudiante a consultar: ").upper()
    listado = informe(tblEstudiantes, tblGrupos, tblProfesores, IdEstu)
    #listado = listado [listado['Activ'] == 'SI']
    listado = listado.sort_values(by = ['Ciclo', 'IDMateria'], ascending=[True,True] )
    #listado = listado [listado['IDProfe'] != 'P0']
    listado = listado.set_index(['Nombres', 'Apellidos','Ciclo', 'Materia'])
    listado = listado[['Nota']]
    listado = listado.drop_duplicates()
    opciones = 1
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

#Funcion para imprimir Listado Promedios por Estudiante (0,2,4,4) 
def InformeListadoPromediosXEstudiantes(informe, tblEstudiantes, tblGrupos, tblProfesores):
    limpiapantalla()
    opciones = 1
    print(Version)
    print(" --------------------------------------------------------------------- ")
    print("|            LISTADO PROMEDIOS DETALLADO POR ESTUDIANTE               |")
    print(" --------------------------------------------------------------------- ")
    IdEstu = input("Ingrese el codigo del estudiante a consultar: ").upper()
    limpiapantalla()
    print(Version)
    print(" --------------------------------------------------------------------- ")
    print("|            LISTADO PROMEDIOS DETALLADO POR ESTUDIANTE               |")
    print(" --------------------------------------------------------------------- ")
    listado = informe(tblEstudiantes, tblGrupos, tblProfesores, IdEstu)
    estudiante = listado[['IDEstudiante', 'Nombres', 'Apellidos']]
    estudiente = estudiante.drop_duplicates()
    estudiente = estudiente.set_index(['IDEstudiante'])
    print(estudiente)
    print(" --------------------------------------------------------------------- ")
    listado = listado[['Ciclo', 'NotaFinalCiclo', 'Materia', 'Promedio', 'Creditos','Nota']]
    listado = listado.sort_values(by = ['Ciclo', 'Materia'], ascending=[True,True] )
    listado = listado.set_index(['Ciclo', 'NotaFinalCiclo','Materia','Promedio','Creditos'])
    #listado = listado[['Nota']]
    listado = listado.drop_duplicates()
    
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
    opciones = 4
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|                   Consultar Notas                        |")
    print(" ---------------------------------------------------------- ")
    print("|                                                          |")
    print("| 1. Matriz general de notas                               |")
    print("| 2. Listado de notas por grupo                            |")
    print("| 3. Listado de notas por estudiante                       |")
    print("| 0. Volver al menu anterior                               |")
    print("| 9. Volver al menu principal                              |")
    print("|                                                          |")
    print(" ---------------------------------------------------------- ")
    print("| Ingrese el número de la acción que desea realizar: ")
    return opciones

#Funcion para imprimir Lista de notas (0,2,5,1)
def InformeListadoGeneralNotas(informe, tblEstudiantes, tblNotas, tblMaterias):
    #tblMaterias = tblMaterias.set_index('IDMateria')
    limpiapantalla()
    opciones = 1
    print(Version)
    print(" ------------------------------------------------------------------------- ")
    print("|                          LISTADO TABLA NOTAS                            |")
    print(" ------------------------------------------------------------------------- ")
    listado = informe(tblEstudiantes, tblNotas, tblMaterias)
    listado = listado[[ 'IdNota', 'IDEstudiante', 'Nombres', 'Apellidos', 'IDMateria', 'Materia', 'Nota']]
    listado['idnf'] = listado['IdNota'].astype(float)
    listado = listado.sort_values(by = ['idnf'], ascending=[True] )
    listado = listado.set_index(['IdNota'])
    if tabactive:
        print(tabulate(listado[['IDEstudiante', 'Nombres', 'Apellidos', 'IDMateria', 'Materia', 'Nota']], headers='keys', tablefmt = 'psql' ),"\n")
    else:
        print(listado[['IDEstudiante', 'Nombres', 'Apellidos', 'IDMateria', 'Materia', 'Nota']],"\n")
    print(" ------------------------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                                              |")
    print("| 9. Volver al menu principal                                             |")
    print(" ------------------------------------------------------------------------- ")
    return opciones


#Funcion para imprimir Lista de notas (0,2,5,2)
def InformeListadoNotasxGrupo(informe, tblEstudiantes, tblNotas, tblMaterias):
    #tblMaterias = tblMaterias.set_index('IDMateria')
    limpiapantalla()
    opciones = 1
    print(Version)
    print(" ------------------------------------------------------------------------- ")
    print("|                        LISTADO NOTAS POR GRUPO                          |")
    print(" ------------------------------------------------------------------------- ")
    IdGru = input("Ingrese Grupo a consultar: ").upper()
    limpiapantalla()
    print(" ------------------------------------------------------------------------- ")
    print("|                        LISTADO NOTAS POR GRUPO                          |")
    print(" ------------------------------------------------------------------------- ")
    listado = informe(tblEstudiantes, tblNotas, tblMaterias)
    listado = listado[listado['IDGrupo'] == IdGru ]
    listado['Nota'] = listado['Nota'].astype(float)
    listado['IDMateria'] = listado['IDMateria'].astype(int)
    promediogeneral = pd.pivot_table(listado, values=['Nota'], index=['IDGrupo'], columns=['IDMateria'], aggfunc=np.average )
    promedioestu = pd.pivot_table(listado, values=['Nota'], index=['IDEstudiante','Nombres','Apellidos'], columns=['IDMateria'], aggfunc=np.average )
    if tabactive:
        print(f"                    LISTADO DE MATERIAS                \n")
        print(tabulate(tblMaterias[['IDMateria','Materia']], headers='keys', tablefmt = 'psql',showindex = False ),"\n")
        print(f"                    PROMEDIO GENERAL DEL GRUPO {IdGru} \n")
        print(tabulate(promediogeneral, headers=list(map(lambda x: x[1],promediogeneral.columns)), tablefmt = 'psql' ),"\n")
        print(f"                   PROMEDIO DETALLADO DEL GRUPO {IdGru} \n")
        promedioestu = promedioestu.reset_index()
        print(tabulate(promedioestu, headers=list(map(lambda x: x[1],promedioestu.columns)), tablefmt = 'psql' ),"\n")
    else:
        print(f"                    PROMEDIO GENERAL DEL GRUPO {IdGru} \n")
        print(promediogeneral.head(100),"\n")
        print(f"                   PROMEDIO DETALLADO DEL GRUPO {IdGru} \n")
        print(promedioestu.head(100),"\n")

    print(" ------------------------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                                              |")
    print("| 9. Volver al menu principal                                             |")
    print(" ------------------------------------------------------------------------- ")
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


#Menu para modificar materias (0,3,1)
def menuModificarMaterias (tblMaterias:pd.DataFrame,existeID,Materia:object,dic_materias):
    limpiapantalla()
    opciones = 1
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|                  Modificar materias                      |")
    print(" ---------------------------------------------------------- ")
    id = str(input("| Ingrese el id de la materia que desea modificar: "))
    #Revisar si se encuentra el elemento solicitado     
    if existeID(tblMaterias, "IDMateria", id):
        print(" ---------------------------------------------------------- ")
        print("Materia a modificar: ")
        print(tblMaterias.set_index("IDMateria").loc[id].to_string())
        print(" ---------------------------------------------------------- ")
        #Recolectar los nuevos datos        
        nuevaMateria = str(input("| Ingrese la nueva Materia: "))
        if nuevaMateria == "":
            nuevaMateria = tblMaterias.set_index("IDMateria")["Materia"][id]
        nuevoCiclo = "_"
        while nuevoCiclo == "_":                 
            nuevoCiclo = str(input("| Ingrese el numero del nuevo ciclo entre 1, 2, 3 o 4: "))
            if nuevoCiclo == "":
                nuevoCiclo = tblMaterias.set_index("IDMateria")["Ciclo"][id]
            elif nuevoCiclo not in ["1","2","3","4"]:
                nuevoCiclo = "_"
                print("| Ciclo no valido")
        nuevoCreditos = "_"
        while nuevoCreditos == "_":   
            nuevoCreditos = str(input("| Ingrese el nuevo número de creditos (de 1 a 10): "))     
            if nuevoCreditos == "":
                nuevoCreditos = tblMaterias.set_index("IDMateria")["Creditos"][id]
            elif nuevoCreditos not in ["1","2","3","4","5","6","7","8","9","10"]:
                nuevoCreditos = "_"
                print("| Numero de creditos no valido")        
        materiaActualizada = [id, nuevaMateria, nuevoCiclo, nuevoCreditos ]   
        print(" --------------------------------------------------------- ")
        print("| Id Materia:", id)
        print("| Materia:   ", nuevaMateria)
        print("| Ciclo:     ", nuevoCiclo)
        print("| Creditos:  ", nuevoCreditos)
        print(" --------------------------------------------------------- ")
        confirma = input("| Ingrese 1 para confirmar o 0 para cancelar: ")
        if confirma == '1':
            try:
                dic_materias[id] = Materia(materiaActualizada)
                tblMaterias = dic_materias[id].guardaCambios()
                opciones = (1,('tblMaterias',tblMaterias))
                print(" --------------------------------------------------------------------- ")
                print("| REGISTRO GUARDADO CON EXITO                                         |")
                print(" --------------------------------------------------------------------- ")
            except:
                print(" --------------------------------------------------------------------- ")
                print("| ERROR AL GUARDAR LA INFORMACION, REVISE LOS DATOS INGRESADOS        |")
                print(" --------------------------------------------------------------------- ")
    else:
        print("| No ha sido encontrada la Materia para modificar!")
    print(" --------------------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                                          |")
    print("| 9. Volver al menu principal                                         |")
    print(" --------------------------------------------------------------------- ")
    return opciones


# Menu para modificar profesores (0,3,2)
def menuModificarProfesores(tblProfesores:pd.DataFrame,existeID,Profesor:object,dic_profesores):
    limpiapantalla()
    opciones = 1
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|               Modificar profesores                      |")
    print(" ---------------------------------------------------------- ")
    id = str(input("| Ingrese el id del profesor que desea modificar: ")).upper()
    #Revisar si se encuentra el elemento solicitado     
    if existeID(tblProfesores, "IDProfesor", id):
        print(" ---------------------------------------------------------- ")
        print("Profesor a modificar: ")
        print(tblProfesores.set_index("IDProfesor").loc[id].to_string())
        print(" ---------------------------------------------------------- ")
        #Recolectar los nuevos datos        
        nuevoNombre = str(input("| Ingrese el nuevo nombre: "))
        if nuevoNombre == "":
            nuevoNombre = tblProfesores.set_index("IDProfesor")["Nombre"][id]
        nuevoIDMateria = str(input("| Ingrese los id de materias que dicta el profesor separados por coma: "))
        if nuevoIDMateria == "":
            nuevoIDMateria = tblProfesores.set_index("IDProfesor")["IDMateria"][id]
        profesorActualizado = [id, nuevoNombre, nuevoIDMateria ]   
        print(" --------------------------------------------------------- ")
        print("| Id Profesor:       ", id)
        print("| Nombre:            ", nuevoNombre)
        print("| Materias a dictar: ", nuevoIDMateria)
        print(" --------------------------------------------------------- ")
        confirma = input("| Ingrese 1 para confirmar o 0 para cancelar: ")
        if confirma == '1':
            try:
                dic_profesores[id] = Profesor(profesorActualizado)
                tblProfesores = dic_profesores[id].guardaCambios()
                opciones = (1,('tblProfesores',tblProfesores))
                print(" --------------------------------------------------------------------- ")
                print("| REGISTRO GUARDADO CON EXITO                                         |")
                print(" --------------------------------------------------------------------- ")
            except:
                print(" --------------------------------------------------------------------- ")
                print("| ERROR AL GUARDAR LA INFORMACION, REVISE LOS DATOS INGRESADOS        |")
                print(" --------------------------------------------------------------------- ")
    else:
        print("| No ha sido encontrado el profesor para modificar!")
    print(" --------------------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                                          |")
    print("| 9. Volver al menu principal                                         |")
    print(" --------------------------------------------------------------------- ")
    return opciones

# Menu para modificar grupos (0,3,3)
def menuModificarGrupos(tblGrupos:pd.DataFrame,existeID,Grupo:object,dic_grupos):
    limpiapantalla()
    opciones = 1
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|                  Modificar Grupos                      |")
    print(" ---------------------------------------------------------- ")
    id = str(input("| Ingrese el id del grupo que desea modificar: "))
    #Revisar si se encuentra el elemento solicitado     
    if existeID(tblGrupos, "IDGrupo", id):
        print(" ---------------------------------------------------------- ")
        print("Grupo a modificar: ")
        print(tblGrupos.set_index("IDGrupo").loc[id].to_string())
        print(" ---------------------------------------------------------- ")
        #Recolectar los nuevos datos        
        nuevoPeriodo = str(input("| Ingrese el nuevo periodo: "))
        if nuevoPeriodo == "":
            nuevoPeriodo = tblGrupos.set_index("IDGrupo")["Periodo"][id]
        nuevoHorario = "_"
        while nuevoHorario == "_":                
            nuevoHorario = str(input("| Ingrese el nuevo horario (mañana, tarde o noche): "))
            if nuevoHorario == "":
                nuevoHorario = tblGrupos.set_index("IDGrupo")["Horario"][id]
            elif nuevoHorario not in ["mañana", "tarde", "noche"]:
                nuevoHorario = "_"
                print("| Horario no valido")
        nuevoEstado = "_"        
        while nuevoEstado =="_":
            nuevoEstado = str(input("| Ingrese el nuevo estado (Activo: 1 o Inactivo: 0): "))     
            if nuevoEstado == "":
                nuevoEstado = tblGrupos.set_index("IDGrupo")["Activo"][id]
            elif nuevoEstado not in ["0","1"]:
                nuevoEstado = "_"
                print("| Estado no valido")
        nuevoMaterias = "1,5,9,2,6,10,3,7,11,4,8,12"
        nuevoProfesor = str(input("| Ingrese los nuevos profesores del grupo: "))     
        if nuevoProfesor == "":
            nuevoProfesor = tblGrupos.set_index("IDGrupo")["IDProfesores"][id]
        grupoActualizado = [id, nuevoPeriodo, nuevoHorario, nuevoEstado, nuevoMaterias, nuevoProfesor ]   
        print(" --------------------------------------------------------- ")
        print("| ID Grupo:      ", id)
        print("| Periodo:       ", nuevoPeriodo)
        print("| Horario:       ", nuevoHorario)
        print("| Activo:        ", nuevoEstado)
        print("| IDMaterias:    ", nuevoMaterias)
        print("| IDProfesores:  ", nuevoProfesor)
        print(" --------------------------------------------------------- ")
        confirma = input("| Ingrese 1 para confirmar o 0 para cancelar: ")
        if confirma == '1':
            try:
                dic_grupos[id] = Grupo(grupoActualizado)
                tblGrupos = dic_grupos[id].guardaCambios()
                opciones = (1,('tblGrupos',tblGrupos))
                print(" --------------------------------------------------------------------- ")
                print("| REGISTRO GUARDADO CON EXITO                                         |")
                print(" --------------------------------------------------------------------- ")
            except:
                print(" --------------------------------------------------------------------- ")
                print("| ERROR AL GUARDAR LA INFORMACION, REVISE LOS DATOS INGRESADOS        |")
                print(" --------------------------------------------------------------------- ")
    else:
        print("No ha sido encontrado el grupo para modificar!")
    print(" --------------------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                                          |")
    print("| 9. Volver al menu principal                                         |")
    print(" --------------------------------------------------------------------- ")
    return opciones
    
    
# Menu para modificar estudiantes (0,3,4)
def menuModificarEstudiantes(tblEstudiantes:pd.DataFrame,existeID,Estudiante:object, dic_estudiantes):
    limpiapantalla()
    opciones = 5
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|               Modificar Estudiantes                      |")
    print(" ---------------------------------------------------------- ")
    id = str(input("| Ingrese el id del estudiante que desea modificar: ")).upper()
    #Revisar si se encuentra el elemento solicitado     
    if existeID(tblEstudiantes, "IDEstudiante", id):
        print(" ---------------------------------------------------------- ")
        print("Estudiante a modificar: ")
        print(tblEstudiantes.set_index("IDEstudiante").loc[id].to_string())
        print(" ---------------------------------------------------------- ")
        #Recolectar los nuevos datos        
        nuevoNombre = str(input("| Ingrese los nuevos nombres: "))
        if nuevoNombre == "":
            nuevoNombre = tblEstudiantes.set_index("IDEstudiante")["Nombres"][id]
        nuevoApellido = str(input("| Ingrese los nuevos apellidos: "))
        if nuevoApellido == "":
            nuevoApellido = tblEstudiantes.set_index("IDEstudiante")["Apellidos"][id]
        nuevoEmail = "_"
        while nuevoEmail == "_":
            nuevoEmail = str(input("| Ingrese el nuevo Email: "))
            if nuevoEmail == "":
                nuevoEmail = tblEstudiantes.set_index("IDEstudiante")["Email"][id]
            elif "@" and ".com" not in nuevoEmail:
                nuevoEmail = "_"
                print("| Email no valido")
        nuevoGrupo = str(input("| Ingrese el id del nuevo grupo: "))
        if nuevoGrupo == "":
            nuevoGrupo = tblEstudiantes.set_index("IDEstudiante")["IDGrupo"][id]
        estudianteActualizado = [id, nuevoNombre, nuevoApellido, nuevoEmail, nuevoGrupo ]   
        print(" --------------------------------------------------------- ")
        print("| ID Estudiante: ", id)
        print("| Nombre:        ", nuevoNombre)
        print("| Apellido:      ", nuevoApellido)
        print("| Email:         ", nuevoEmail)
        print("| Grupo:         ", nuevoGrupo)
        print(" --------------------------------------------------------- ")
        confirma = input("| Ingrese 1 para confirmar o 0 para cancelar: ")
        if confirma == '1':
            try:
                dic_estudiantes[id] = Estudiante(estudianteActualizado)
                tblEstudiantes = dic_estudiantes[id].guardaCambios()
                opciones = (1,('tblEstudiantes',tblEstudiantes))
                print(" --------------------------------------------------------------------- ")
                print("| REGISTRO GUARDADO CON EXITO                                         |")
                print(" --------------------------------------------------------------------- ")
            except:
                print(" --------------------------------------------------------------------- ")
                print("| ERROR AL GUARDAR LA INFORMACION, REVISE LOS DATOS INGRESADOS        |")
                print(" --------------------------------------------------------------------- ")
    else:
        print("| No ha sido encontrado el estudiante para modificar!")
    print(" --------------------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                                          |")
    print("| 9. Volver al menu principal                                         |")
    print(" --------------------------------------------------------------------- ")
    return opciones

# Menu para modificar notas(0,3,5)
def menuModificarNotas(tblNotas:pd.DataFrame, existeID, tblEstudiantes, tblMaterias, Nota:object, dic_notas):
    limpiapantalla()
    opciones = 5
    print(Version)
    print(" ---------------------------------------------------------- ")
    print("|                  Modificar Notas                         |")
    print(" ---------------------------------------------------------- ")
    id = str(input("| Ingrese el id de la nota que desea modificar:  "))
    #Revisar si se encuentra el elemento solicitado     
    if existeID(tblNotas, "IdNota", id):
        print(" ---------------------------------------------------------- ")
        print("Nota a modificar: ")
        print(tblNotas.set_index("IdNota").loc[id].to_string())
        print(" ---------------------------------------------------------- ")
        #Recolectar los nuevos datos
        nuevoEstudiante = "_"
        while nuevoEstudiante == "_":        
            nuevoEstudiante = str(input("| Ingrese el id del nuevo estudiante: "))
            if nuevoEstudiante == "":
                    nuevoEstudiante = tblNotas.set_index("IdNota")["IDEstudiante"][id]
            elif existeID(tblEstudiantes, "IDEstudiante", nuevoEstudiante):
                pass
            else:
                print("| No ha sido encontrado el id del nuevo estudiante!")
                nuevoEstudiante = "_"
        nuevaNota = "_"
        while nuevaNota == "_":                
            nuevaNota = str(input("| Ingrese la nueva nota (de 0 a 5): "))
            if nuevaNota == "":
                nuevaNota = tblNotas.set_index("IdNota")["Nota"][id]
            elif float(nuevaNota) not in [x / 100.0 for x in range(0, 501)]:
                print("| La nota no es valida")
                nuevaNota = "_"
        nuevaMateria = "_"
        while nuevaMateria == "_":    
            nuevaMateria = str(input("| Ingrese el id de la nueva materia: "))     
            if nuevaMateria == "":
                nuevaMateria = tblNotas.set_index("IdNota")["IDMateria"][id]
            elif existeID(tblMaterias, "IDMateria", nuevaMateria):
                pass
            else:
                print("| No ha sido encontrado el id de la nueva materia!")
                nuevaMateria = "_"
        notaActualizada = [id, nuevoEstudiante, nuevaNota, nuevaMateria]  
        print(" --------------------------------------------------------- ")
        print("| ID Nota:       ", id)
        print("| ID Estudiante: ", nuevoEstudiante)
        print("| Nota:          ", nuevaNota)
        print("| IdMateria:     ", nuevaMateria)
        print(" --------------------------------------------------------- ")
        confirma = input("| Ingrese 1 para confirmar o 0 para cancelar: ")
        if confirma == '1':
            try:
                dic_notas[id] = Nota(notaActualizada)
                tblNotas = dic_notas[id].guardaCambios()
                opciones = (1,('tblNotas',tblNotas))
                print(" --------------------------------------------------------------------- ")
                print("| REGISTRO GUARDADO CON EXITO                                         |")
                print(" --------------------------------------------------------------------- ")
            except:
                print(" --------------------------------------------------------------------- ")
                print("| ERROR AL GUARDAR LA INFORMACION, REVISE LOS DATOS INGRESADOS        |")
                print(" --------------------------------------------------------------------- ")
    else:
        print("| No ha sido encontrada la nota para modificar!")
    print(" --------------------------------------------------------------------- ")
    print("| 0. Volver al menu anterior                                          |")
    print("| 9. Volver al menu principal                                         |")
    print(" --------------------------------------------------------------------- ")
    return opciones


 #Funcion para imprimir en pantalla el Menu Eliminar (0,4)
def menuEliminar():
    limpiapantalla()
    opciones = 1
    print(Version)
    print(" -------------------------------------------------------------- ")
    print("|                   Eliminar Información                       |")
    print(" -------------------------------------------------------------- ")
    print("|                                                              |")
    print("| ¡LA OPCION PARA ELIMINAR NO ESTA DISPONIBLE POR SEGURIDAD!   |")
    print("| 0. Volver al menu anterior                                   |")
    print("| 9. Volver al menu principal                                  |")
    print("|                                                              |")
    print(" -------------------------------------------------------------- ")
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
