#Modulo para las funciones de creacion, lectura, edicion y eliminacion de la información
import pandas as pd
from pandas.core.frame import DataFrame
from pandas.core.indexes.base import Index
#------------------Se crean las funciones para cargar datos-------------------------------------
def CargaNotasCSV():
    # Leyendo archivo csv
    try:
        df1 = pd.read_csv("Notas.csv",dtype=str,sep = ';')
        return df1,1
    except FileNotFoundError:
        return "Archivo no encontrado.", 0
    except pd.errors.EmptyDataError:
        return "No hay informacion que leer", 0  
    except pd.errors.ParserError:
        return "Error de analisis", 0  
    except Exception:
        return "Alguna otra Exepcion", 0     


def CargaMateriasCSV():
    try:
        df1 = pd.read_csv("Materias.csv",dtype=str,sep = ';')
        return df1,1
    except FileNotFoundError:
        return "Archivo no encontrado.", 0
    except pd.errors.EmptyDataError:
        return "No hay informacion que leer", 0  
    except pd.errors.ParserError:
        return "Error de analisis", 0  
    except Exception:
        return "Alguna otra Exepcion", 0       


def CargaProfesoresCSV():
    try:
        df1 = pd.read_csv("Profesores.csv",dtype=str,sep=';')
        return df1,1
    except FileNotFoundError:
        return "Archivo no encontrado.", 0
    except pd.errors.EmptyDataError:
        return "No hay informacion que leer", 0  
    except pd.errors.ParserError:
        return "Error de analisis", 0  
    except Exception:
        return "Alguna otra Exepcion", 0       


def CargaEstudiantesCSV():
    try:
        df1 = pd.read_csv("Estudiantes.csv",dtype=str,sep=';')
        return df1,1
    except FileNotFoundError:
        return "Archivo no encontrado.", 0
    except pd.errors.EmptyDataError:
        return "No hay informacion que leer", 0  
    except pd.errors.ParserError:
        return "Error de analisis", 0  
    except Exception:
        return "Alguna otra Exepcion", 0 


def CargaGruposCSV():
    try:
        df1 = pd.read_csv("Grupos.csv",dtype=str,sep=';')
        return df1,1
    except FileNotFoundError:
        return "Archivo no encontrado.", 0
    except pd.errors.EmptyDataError:
        return "No hay informacion que leer", 0  
    except pd.errors.ParserError:
        return "Error de analisis", 0  
    except Exception:
        return "Alguna otra Exepcion", 0  

#------------------Se crean las funciones para Modificar Archivos CSV-------------------------------------

def ReiniciarDB():
    reiniciado = 0
    try:
        with open('Materias.csv','w') as archivo:
            print('IDMateria;Materia;Ciclo;Creditos', file = archivo)
        reiniciado += 1
    except :
        pass
    try:
        with open('Profesores.csv','w') as archivo:
            print('IDProfesor;Nombre;IDMateria', file = archivo)
        reiniciado +=1
    except :
        pass
    try:
        with open('Grupos.csv','w') as archivo:
            print('IDGrupo;Periodo;Horario;Activo;IDMaterias;IDProfesores', file = archivo)
        reiniciado +=1
    except:
        pass
    try:
        with open('Estudiantes.csv','w') as archivo:
            print('IDEstudiante;Nombres;Apellidos;Email;IDGrupo', file = archivo)
        reiniciado +=1
    except :
        pass
    try:
        with open('Notas.csv','w') as archivo:
            print('IdNota;IDEstudiante;Nota;IDMateria', file = archivo)
        reiniciado +=1
    except :
        pass
    return reiniciado


#------------------ Se crean las funciones para Consultar Informacion -------------------------------------

def consultaMateriasXProfesor ( df : pd.DataFrame, df2: pd.DataFrame, IDProf:str = 0, IDMate:str = 0 )-> DataFrame:
    '''
    Args:
        df:  DataFrame tblProfesores
        df2:  DataFrame tblMaterias
        IDProf: Si se desea filtrar por profesor se ingresa el IDProfesor
        IDMate: Si se desea filtrar por materia se ingresa el IDMateria
    '''

    # Dividir (explotar) entrada de cadena de marco de datos de pandas en filas separadas
    # Dataframe.assign()El método asigna nuevas columnas a un DataFrame, 
    # devolviendo un nuevo objeto (una copia) con las nuevas columnas agregadas a las originales.
    # Las columnas existentes que se reasignan se sobrescribirán.
    # Ejemplo: Asigne una nueva columna llamada Materia
    
    df = df[df['IDProfesor'] != 'P0']
    MateriasXProfesor = df.assign(Materia=df.IDMateria.str.split(",")).explode('Materia')
    
    if IDMate !=0:
        MateriasXProfesor = MateriasXProfesor[MateriasXProfesor.Materia == str(IDMate)]
    #Se define cuales van a ser las llaves para hacer la union en cada tabla
    MateriasXProfesor["IDMateria"] =  MateriasXProfesor['Materia']
    MateriasXProfesor = MateriasXProfesor.set_index('Materia')
    
    df2 = df2.set_index('IDMateria')

    #Se realiza la union de las dos tablas
    MateriasXProfesor = pd.merge(MateriasXProfesor, df2, left_index=True, right_index=True)

    #print(MateriasXProfesor)
    # Haciendo una consulta de un profesor por la llave IDProfesor
    if IDProf !=0:
        MateriasXProfesor = MateriasXProfesor[MateriasXProfesor['IDProfesor'] == IDProf]

    MateriasXProfesor = MateriasXProfesor.set_index('IDProfesor') 
    # Ordenando dataframe por nombre
    MateriasXProfesor.sort_values("Nombre", axis = 0, ascending = True,
                 inplace = True, na_position ='last') 
    #print(MateriasXProfesor)
    return MateriasXProfesor[[ 'Nombre','IDMateria','Materia']]


def consultaMateriasXCiclo ( TblMaterias : pd.DataFrame, ciclo:str = 0 )-> DataFrame: 
    '''
    Args:
        df:  DataFrame tblMaterias
        ciclo: string con el numero del ciclo
    '''
    if ciclo !=0:
        TblMaterias = TblMaterias[TblMaterias['Ciclo'] == str(ciclo)]
    
    TblMaterias = TblMaterias.sort_values(by  = 'Ciclo')
    TblMaterias = TblMaterias.set_index(['Ciclo','IDMateria',])
    return TblMaterias

def existeID (dFIngreso, nomCol, ID) -> bool:
    return ID in dFIngreso[nomCol].values
#------------------ CONSULTA DE ESTUDIANTES POR GRUPOS -----------------------

def consultaEstudiantesXGrupo( TblEstudiantes : pd.DataFrame, TblGrupo : pd.DataFrame ) -> DataFrame :
    TblEstudiantes = TblEstudiantes.set_index('IDGrupo')
    TblGrupo = TblGrupo.set_index('IDGrupo')
    EstudiantesXGrupo = pd.merge( TblEstudiantes, TblGrupo, left_index=True, right_index=True)
    EstudiantesXGrupo  = EstudiantesXGrupo.sort_values(by  = 'Apellidos')
    return(EstudiantesXGrupo)
    # Llamada a la funcion
    #print(consultaEstudiantesXGrupo(CargaEstudiantesCSV,CargaGruposCSV))

#------------------ FIN CONSULTA DE ESTUDIANTES POR GRUPOS -----------------------

#------------------ CONSULTA DE ESTUDIANTES POR PROFESOR -----------------------
#Se puede consultar por el IDEstudiante en particular
#Se puede consultar Por IDProfe de un Profesor en particular para saber que estudiantes tiene asignados para dar clase 
#Sacar el listado completo de estudiantes x profesor 


def consultaEstudiantesXProfesor(TblEstudiantes:pd.DataFrame, TblGrupo:pd.DataFrame, TblProfesores:pd.DataFrame, IDStu:str = 0, IDProfe:str = 0)->DataFrame:
    EstudiantesXGrupo = pd.merge( TblEstudiantes, TblGrupo, left_on='IDGrupo', right_on='IDGrupo')
    EstudiantesXGrupo = EstudiantesXGrupo.assign(IDProfe=EstudiantesXGrupo.IDProfesores.str.split(",")).explode('IDProfe')
    EstudiantesXGrupo = pd.merge(left=EstudiantesXGrupo,right=TblProfesores, left_on='IDProfe', right_on='IDProfesor')
    EstudiantesXGrupo.rename(columns={'Nombre':'Nombre Profesor','Nombres':'Nombre Estudiante'},inplace=True) 
    EstudiantesXGrupo = EstudiantesXGrupo [['IDEstudiante','Nombre Estudiante','Apellidos','Nombre Profesor','IDGrupo','IDProfe']]
    if IDStu != 0:
        EstudiantesXGrupo = EstudiantesXGrupo[EstudiantesXGrupo['IDEstudiante'] == IDStu]
        EstudiantesXGrupo = EstudiantesXGrupo.set_index(['IDEstudiante','Nombre Estudiante'])
    if IDProfe !=0:
        EstudiantesXGrupo = EstudiantesXGrupo[EstudiantesXGrupo['IDProfe'] == IDProfe] 
        EstudiantesXGrupo = EstudiantesXGrupo.set_index(['Nombre Profesor','IDProfe','IDGrupo'])   
    return EstudiantesXGrupo
# Llamada a la funcion
#print(consultaEstudiantesXProfesor(CargaEstudiantesCSV,CargaGruposCSV,CargaProfesoresCSV,IDProfe=0,IDStu=0))

#------------------ FIN CONSULTA DE ESTUDIANTES POR PROFESOR -----------------------

#------------------ INICIO CONSULTA DE NOTAS ESTUDIANTES ---------------------------

#Se puede sacar el listado completo de Todas las notas por estudiantes
#Se puede sacar el listado de notas de estudiante en particular
#Se puede sacar el listado de los estudiantes que sacaron determinada nota

def consultaNotas( TblEstudiantes:pd.DataFrame, TblNotas:pd.DataFrame, TblMaterias:pd.DataFrame, IDEstud:str = 0, Nota = 0  ) -> DataFrame:
    
    '''
    Args:
        TblEstudiantes:  DataFrame tabla estudiantes
        TblNotas:        DataFrame tabla notas
        TblMaterias:     DataFrame tabla materias
        IDEstud :        String con el id de estudiante
        Nota :           String con el numero de nota a consultar 

    '''
    NotasEstudiante = pd.merge(TblEstudiantes,TblNotas,left_on='IDEstudiante',right_on='IDEstudiante')
    NotasEstudiante = pd.merge(NotasEstudiante, TblMaterias, left_on='IDMateria', right_on='IDMateria')
    if IDEstud !=0: 
        NotasEstudiante = NotasEstudiante[NotasEstudiante['IDEstudiante'] == IDEstud ]
    if Nota !=0:
        NotasEstudiante = NotasEstudiante[NotasEstudiante['Nota'] >= Nota]    
    NotasEstudiante = NotasEstudiante.sort_values(by = 'Apellidos' )
    NotasEstudiante = NotasEstudiante[['IDEstudiante','Nombres','Apellidos','Materia', 'Nota', 'Creditos' ,'IDMateria', 'IdNota']]
    return NotasEstudiante
    #Llamada a la funcion
    #print(consultaNotas(TblEstudiantes,TblNotas, TblMaterias, IDEstud=0, Nota=0))
    
#------------------ FIN CONSULTA DE NOTAS ESTUDIANTES    ---------------------------

