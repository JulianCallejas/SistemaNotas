#Importa librerias y modulos necesarios

import CRUD as crud
import InterfazConsola as ic
import ClassesApp as clapp

#Realiza el proceso de cargue de informacion
cargado = 0 #variable de control de cargue de archivos
tblMaterias, carga = crud.CargaMateriasCSV()
cargado += carga
tblProfesores, carga = crud.CargaProfesoresCSV()
cargado += carga
tblGrupos, carga = crud.CargaGruposCSV()
cargado += carga
tblEstudiantes, carga = crud.CargaEstudiantesCSV()
cargado += carga
tblNotas, carga = crud.CargaNotasCSV()
cargado += carga

#Opciones si falla el cargue de informacion
if cargado < 5:
    ic.limpiapantalla()
    print(" ---------------------------------------------------------- ")
    if type(tblMaterias)== str:
        print('|',tblMaterias,'Materias.csv')
    if type(tblProfesores)== str:
        print('|',tblProfesores,'Profesores.csv')
    if type(tblGrupos)== str:
        print('|',tblGrupos,'Grupos.csv')
    if type(tblEstudiantes)== str:
        print('|',tblEstudiantes,'Estudiantes.csv')
    if type(tblNotas)== str:
        print('|',tblNotas,'Notas.csv')
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

       #Se crea el diccionario de funciones del menu, que se llaman con la variable accion
DicMenu = { (0,)   :     ic.menuInicial,
            (0,1)  :     ic.menuAgregar,     #0 es el menu principal y 1 es la opcion 1 Agregar del menu principal por tanto la llave de esta funcion es (0,1)
            (0,2)  :     ic.menuConsultar,
            (0,2,1) :    ic.menuConsultarMaterias,
            (0,2,1,1):   (ic.InformeListadoMaterias,tblMaterias),
            (0,2,1,2):   (ic.InformeMateriasXCiclo,crud.consultaMateriasXCiclo,tblMaterias),
            (0,2,1,3):   (ic.InformeProfesoresXMateria, crud.consultaMateriasXProfesor, tblProfesores, tblMaterias ),
            (0,2,2) :    ic.menuConsultarProfesores,
            (0,2,2,1) :  (ic.InformeListadoProfesores, crud.consultaMateriasXProfesor, tblProfesores, tblMaterias ),
            (0,2,2,2) :  (ic.InformeGruposActivosXProfesor, crud.consultaEstudiantesXProfesor,tblEstudiantes, tblGrupos, tblProfesores),
            (0,2,3) :    ic.menuConsultarGrupos,
            (0,2,3,1) :  (ic.InformeListadoGrupos, crud.consultaEstudiantesXProfesor,tblEstudiantes, tblGrupos, tblProfesores),
            (0,2,3,2) :  (ic.InformeListadoDetalladoGrupos, crud.consultaEstudiantesXProfesor,tblEstudiantes, tblGrupos, tblProfesores),
            (0,2,4) :    ic.menuConsultarEstudiantes,
            (0,2,4,1) :  (ic.InformeListadoDeEstudiantes, crud.consultaEstudiantesXProfesor,tblEstudiantes, tblGrupos, tblProfesores),
            (0,2,4,3) :  (ic.InformeListadoNotasXEstudiantes, crud.consultaNotas, tblEstudiantes, tblNotas, tblMaterias),
            (0,2,4,2):   (ic.InformeEstudiantesXGrupo, crud.consultaEstudiantesXGrupo ,tblEstudiantes,tblGrupos),
            (0,2,5) :    ic.menuConsultarNotas,
            (0,3) :      ic.menuModificar,
            (0,4)  :     ic.menuEliminar,

}
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
    else:    
        opciones = DicMenu[accion]()
    return opciones

while continuar and cargado == 5 :
    opciones = MostarMenu(accion)
    try:
        seleccion = int(input("|"))
        if seleccion == 99:
            continuar = False
        elif seleccion == 9:
            accion = (0,)
        elif seleccion in range(opciones):
            if seleccion == 0:
                accion = accion[:-1]
            else:
                accion = accion + (seleccion,)
    except :
        input("Opcion Invalida")
    
