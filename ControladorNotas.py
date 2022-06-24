#Importa librerias y modulos necesarios
import CRUD as crud
import InterfazConsola as ic
import ClasesApp as clapp
#Realiza el proceso de cargue de informacion

cargado = crud.cargaDatos()
#Opciones si falla el cargue de informacion

if cargado < 5:
    ic.limpiapantalla()
    print(" ---------------------------------------------------------- ")
    if type(crud.tblMaterias)== str:
        print('|',crud.tblMaterias,'Materias.csv')
    if type(crud.tblProfesores)== str:
        print('|',crud.tblProfesores,'Profesores.csv')
    if type(crud.crud.tblGrupos)== str:
        print('|',crud.tblGrupos,'Grupos.csv')
    if type(crud.crud.tblEstudiantes)== str:
        print('|',crud.tblEstudiantes,'Estudiantes.csv')
    if type(crud.crud.tblNotas)== str:
        print('|',crud.tblNotas,'Notas.csv')
    print(" ---------------------------------------------------------- ")
    ic.menuFallaCarga()
    accion = input("|")
    if accion == '99':
        accion = input(' ---------------------------------------------------------- \n' \
                      +'|CONFIRME QUE DESEA BORRAR TODOS LOS DATOS E INICIAR UNA   |\n'  \
                      +'|BASE DE DATOS VACIA. Escriba "SI" para confirmar:  ')
        if accion.upper() == "SI":
            ic.limpiapantalla()
            print(" ---------------------------------------------------------- ")
            print("| !BORRANDO ARCHIVOS EXISTENTES Y CREANDO NUEVOS ARCHIVOS! |")
            print(" ---------------------------------------------------------- ")
            archivosreiniciados = crud.ReiniciarDB()
            print(" ---------------------------------------------------------- ")
            print(f"|              TOTAL ARCHIVOS NUEVOS {archivosreiniciados}                   |")
            print(" ---------------------------------------------------------- ")
            input("| Presione Enter para salir")

#Abre menu principal para manipular informacion
accion = (0,)
continuar = True
global tblMaterias , tblProfesores, tblGrupos, tblEstudiantes, tblNotas
global dic_materias, dic_profesores, dic_grupos, dic_estudiantes, dic_notas
tblMaterias , tblProfesores, tblGrupos, tblEstudiantes, tblNotas = crud.tblMaterias , crud.tblProfesores, crud.tblGrupos, crud.tblEstudiantes, crud.tblNotas
dic_materias, dic_profesores, dic_grupos, dic_estudiantes, dic_notas = crud.dic_materias, crud.dic_profesores, crud.dic_grupos, crud.dic_estudiantes, crud.dic_notas

#Se define la funcion para organizar las tuplas del diccionario de funciones, el primer objeto
#de la tupla es la funcion, los otros objetos de la tupla son parametros para la cuncion
def MostarMenu(accion: tuple):
    if type(DicMenu[accion]) == tuple:
        if len(DicMenu[accion]) == 2:
            opciones = DicMenu[accion][0](DicMenu[accion][1])
        elif len(DicMenu[accion]) == 3:
            opciones = DicMenu[accion][0](DicMenu[accion][1], DicMenu[accion][2])
        elif len(DicMenu[accion]) == 4:
            opciones = DicMenu[accion][0](DicMenu[accion][1], DicMenu[accion][2], DicMenu[accion][3] )
        elif len(DicMenu[accion]) == 5:
            opciones = DicMenu[accion][0](DicMenu[accion][1], DicMenu[accion][2], DicMenu[accion][3], DicMenu[accion][4])
        elif len(DicMenu[accion]) == 6:
            opciones = DicMenu[accion][0](DicMenu[accion][1], DicMenu[accion][2], DicMenu[accion][3], DicMenu[accion][4], DicMenu[accion][5])
        elif len(DicMenu[accion]) == 7:
            opciones = DicMenu[accion][0](DicMenu[accion][1], DicMenu[accion][2], DicMenu[accion][3], DicMenu[accion][4], DicMenu[accion][5],DicMenu[accion][6])
    else:    
        opciones = DicMenu[accion]()
    return opciones

while continuar and cargado == 5 :
#Se crea y actualiza el diccionario de funciones del menu, que se llaman con la variable accion
    DicMenu = { (0,)   :     ic.menuInicial,
                (0,1)  :     ic.menuAgregar,     #0 es el menu principal y 1 es la opcion 1 Agregar del menu principal por tanto la llave de esta funcion es (0,1)
                (0,1,1) :    (ic.menuAgregarMateria,crud.crearConsecutivoIDNumerico, tblMaterias, clapp.Materia,dic_materias),
                (0,1,2) :    (ic.menuAgregarProfesor,crud.crearIDProfesor, tblProfesores, clapp.Profesor,dic_profesores),
                (0,1,3) :    (ic.menuAgregarGrupo,crud.crearConsecutivoIDNumerico, tblGrupos, clapp.Grupo, dic_grupos),
                (0,1,4) :    (ic.menuAgregarEstudiante,crud.crearIDEstudiante,tblEstudiantes, clapp.Estudiante, dic_estudiantes),
                (0,1,5) :    (ic.menuAgregarNota,crud.crearConsecutivoIDNumerico, tblNotas, clapp.Nota, dic_notas, dic_estudiantes, dic_materias),
                (0,2)  :     ic.menuConsultar,
                (0,2,1) :    ic.menuConsultarMaterias,
                (0,2,1,1):   (ic.InformeListadoMaterias,tblMaterias),
                (0,2,1,2):   (ic.InformeMateriasXCiclo,crud.consultaMateriasXCiclo,tblMaterias),
                (0,2,1,3):   (ic.InformeProfesoresXMateria, crud.consultaMateriasXProfesor, tblProfesores, tblMaterias ),
                (0,2,2) :    ic.menuConsultarProfesores,
                (0,2,2,1) :  (ic.InformeListadoProfesores, crud.consultaMateriasXProfesor, tblProfesores, tblMaterias ),
                (0,2,2,2) :  (ic.InformeGruposActivosXProfesor, crud.consultaEstudiantesXProfesor,tblEstudiantes, tblGrupos, tblProfesores),
                (0,2,3) :    ic.menuConsultarGrupos,
                (0,2,3,1) :  (ic.InformeListadoTablaGrupos,tblGrupos),
                (0,2,3,2) :  (ic.InformeListadoGrupos, crud.consultaEstudiantesXProfesor,tblEstudiantes, tblGrupos, tblProfesores),
                (0,2,3,3) :  (ic.InformeListadoDetalladoGrupos, crud.consultaEstudiantesXProfesor,tblEstudiantes, tblGrupos, tblProfesores),
                (0,2,4) :    ic.menuConsultarEstudiantes,
                (0,2,4,1) :  (ic.InformeListadoDeEstudiantes, crud.consultaEstudiantesXProfesor,tblEstudiantes, tblGrupos, tblProfesores),
                (0,2,4,2):   (ic.InformeEstudiantesXGrupo, crud.consultaEstudiantesXGrupo ,tblEstudiantes,tblGrupos),
                (0,2,4,3) :  (ic.InformeListadoNotasXEstudiantes, crud.consultaNotas, tblEstudiantes, tblNotas, tblMaterias),
                (0,2,4,4) :  (ic.InformeListadoPromediosXEstudiantes, crud.consultaPromedios,tblEstudiantes, tblNotas, tblMaterias ),
                (0,2,5) :    ic.menuConsultarNotas,
                (0,2,5,1) :  (ic.InformeListadoGeneralNotas, crud.consultaNotas, tblEstudiantes, tblNotas, tblMaterias),
                (0,2,5,2) :  (ic.InformeListadoNotasxGrupo, crud.consultaNotas, tblEstudiantes, tblNotas, tblMaterias),
                (0,2,5,3) :  (ic.InformeListadoNotasXEstudiantes, crud.consultaNotas, tblEstudiantes, tblNotas, tblMaterias),
                (0,3) :      ic.menuModificar,
                (0,3,1) :    (ic.menuModificarMaterias, tblMaterias, crud.existeID, clapp.Materia,dic_materias),
                (0,3,2) :    (ic.menuModificarProfesores, tblProfesores, crud.existeID, clapp.Profesor,dic_profesores),           
                (0,3,3) :    (ic.menuModificarGrupos, tblGrupos, crud.existeID, clapp.Grupo, dic_grupos),
                (0,3,4) :    (ic.menuModificarEstudiantes, tblEstudiantes, crud.existeID, clapp.Estudiante, dic_estudiantes),
                (0,3,5) :    (ic.menuModificarNotas, tblNotas, crud.existeID, tblEstudiantes, tblMaterias, clapp.Nota, dic_notas),
                (0,4)  :     ic.menuEliminar,
    }
    #Llama la funcion del diccionario anterior con base en la eleccion del usuario
    opciones = MostarMenu(accion)
    if type(opciones) == tuple:
        opcion = opciones[0]
        for actualizacion in opciones[1:]:
            if actualizacion[0] == "tblMaterias":
                tblMaterias = actualizacion[1]
            elif actualizacion[0] == "tblProfesores":
                tblProfesores = actualizacion[1]
            elif actualizacion[0] == "tblEstudiantes":
                tblEstudiantes = actualizacion[1]
            elif actualizacion[0] == "tblGrupos":
                tblGrupos = actualizacion[1]
            elif actualizacion[0] == "tblNotas":
                tblNotas = actualizacion[1]
    else:
        opcion = opciones
    try:
        seleccion = int(input("|"))
        if seleccion == 99:
            continuar = False
        elif seleccion == 9:
            accion = (0,)
        elif seleccion in range(opcion):
            if seleccion == 0:
                accion = accion[:-1]
                if accion == ():
                    accion = (0,)
            else:
                accion = accion + (seleccion,)
    except :
        input("Opcion Invalida")
        
