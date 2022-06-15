#Modulo para las funciones de creacion, lectura, edicion y eliminacion de la información
import numpy as np
from numpy.lib.function_base import average
import pandas as pd
from pandas.core.frame import DataFrame
from pandas.core.indexes.base import Index
# Se importan las clases personalizadas
from ClasesApp import *
pd.options.display.max_rows = 100  #Imprime todas las filas del DataFrame
pd.options.display.max_columns = 100 #Imprime todas las columnas del DataFrame

# Se declaran las listas de objetos que seran globales para ser usados en distintos metodos
lista_materias = []
lista_profesores = []
lista_grupos = []
lista_estudiantes = []
lista_notas = []


#------------------Se crean las funciones para crear los objetos -------------------------------------

def crear_lista_objeto_materias(materias: pd.DataFrame) -> None:
    """Crea una lista de objetos de tipo materia con base en el dataframe que llega por parametro
    Args:
        materias (pd.DataFrame): El dataframe de materias
    """
    # Para trabajar con variables locales dentro de una función se utiliza la palabra reservada global antes de la variable
    # para indicar que se usara una variable del scope global
    global lista_materias
    
    # Crea la lista de materias utilizando una función lambda para extraer cada linea del dataframe y
    # usando el constructor de materia se crea el respectivo elemento, para cada campo se hace la conversión explicita al tipo correspondiente
    # según la clase
    lista_materias = list(map(lambda x:Materia(int(x[0]),x[1],int(x[2]),int(x[3])),materias.values.tolist()))

def crear_lista_objeto_profesores(profesores: pd.DataFrame) -> None:
    """Crea una lista de objetos de tipo profesores con base en el dataframe que llega por parametro
    Args:
        profesores (pd.DataFrame): El dataframe de profesores
    """
    
    global lista_profesores
    # Se usa map para crear un profesor según cada linea leida del dataframe, para el caso de los id de materias
    # se hace un split con la "," y se transforma a int para obtener la lista de ids de materias que puede dictar el profesor
    lista_profesores = list(map(lambda x:Profesor(x[0],x[1],list(map(int,x[2].split(",")))),profesores.values.tolist()))
    
def crear_lista_objeto_grupos(grupos: pd.DataFrame)-> None:
    """Crea una lista de objetos de tipo grupos con base en el dataframe que llega por parametro
    Args:
        grupos (pd.DataFrame): El dataframe de grupos
    """
    global lista_grupos
    # Se usa map para iterar sobre cada linea del dataframe y crear un objeto de tipo grupo, se hace el casteo
    # a los tipos correspondientes y para el caso de materias y profesores se usa compresión de listas usando
    # el id de las listas (haciendo un slit con ",") que vienen como campo en el dataframe para compararlo con los id de las materias y profesores registrados
    # en el caso de las materias, como el id del objeto materia es int se hace el casteo de este a string para compararlo con la lista de id.
    lista_grupos = list(map(lambda x:Grupo(int(x[0]),int(x[1]),x[2],int(x[3]),[materia for materia in lista_materias if str(materia.id) in x[4].split(",")],[profesor for profesor in lista_profesores if profesor.id in x[5].split(",")]),grupos.values.tolist()))

def crear_lista_objeto_estudiantes(estudiantes: pd.DataFrame) -> None:
    global lista_estudiantes
    lista_estudiantes = list(map(lambda x:Estudiante(x[0],x[1],x[2],x[3],int(x[4])),estudiantes.values.tolist()))

def crear_lista_objeto_notas(notas: pd.DataFrame) -> None:
    """Crea una lista de objetos de tipo notas con base en el dataframe que llega por parametro
    Args:
        notas (pd.DataFrame): El dataframe de notas
    """
    global lista_notas
    # Se usa map para iterar sobre cada linea del dataframe y crear un objeto de tipo grupo, se hace el casteo correspondiente a los tipos 
    # según objeto y se usa un filter para obtener el estudiante y la materia correspondiente, dado que esto retorna una lista se saca la primera posición
    # que corresponde con los elementos estudiante y materia buscado
    lista_notas = list(map(lambda x:Nota(int(x[0]),list(filter(lambda y: (y.id==x[1]),lista_estudiantes))[0],float(x[2]),list(filter(lambda y: (y.id==int(x[3])),lista_materias))[0]),notas.values.tolist()))

#------------------Se crean las funciones para cargar datos-------------------------------------
def CargaNotasCSV():
    # Leyendo archivo csv
    try:
        df1 = pd.read_csv("Notas.csv",dtype=str,sep = ';')
        crear_lista_objeto_notas(df1)
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
        crear_lista_objeto_materias(df1)
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
        crear_lista_objeto_profesores(df1)
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
        crear_lista_objeto_estudiantes(df1)
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

def prueba_carga_objeto():
    
    CargaMateriasCSV()
    CargaProfesoresCSV()
    CargaGruposCSV()
    CargaEstudiantesCSV()
    CargaNotasCSV()
    CargaGruposCSV()
    #print([profesor for profesor in lista_profesores if profesor.id in ["P1","P2"]])
    #print ([profesor for profesor in lista_profesores if profesor.id in ["P1","P2"]][0])
    print(list(map(str,lista_notas)))
      
#------------------Se crean las funciones para Modificar Archivos CSV-------------------------------------

def existeID (dFIngreso, nomCol, ID) -> bool:
    '''
    Args:
        dFIngreso:  DataFrame a comsultar
        nomCol: string con el nombre de la columna a consultar
        ID: valor para verificar si tiene duplicados en la columna
    '''
    return ID in dFIngreso[nomCol].values


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

#------------------ CONSULTA DE ESTUDIANTES POR GRUPOS -----------------------

def consultaEstudiantesXGrupo( TblEstudiantes : pd.DataFrame, TblGrupo : pd.DataFrame ) -> DataFrame :
    '''
    Args:
        TblEstudiantes:  Ingrese el DataFrame de estudiantes
        TblGrupo: Ingrese el DataFrame de grupo
    '''
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
    EstudiantesXGrupo['Activ'] = list(map(lambda x: "SI" if(int(x)==1) else "NO",list(EstudiantesXGrupo['Activo'])))
    EstudiantesXGrupo1 = EstudiantesXGrupo.assign(IDMater=EstudiantesXGrupo.IDMaterias.str.split(",")).explode('IDMater')
    EstudiantesXGrupo = EstudiantesXGrupo.assign(IDProfe=EstudiantesXGrupo.IDProfesores.str.split(",")).explode('IDProfe')
    EstudiantesXGrupo["IdMater"] = EstudiantesXGrupo1['IDMater']
    EstudiantesXGrupo = pd.merge(left=EstudiantesXGrupo,right=TblProfesores, left_on='IDProfe', right_on='IDProfesor')
    EstudiantesXGrupo.rename(columns={'Nombre':'Nombre Profesor','Nombres':'Nombre Estudiante'},inplace=True) 
    EstudiantesXGrupo = EstudiantesXGrupo #[['IDEstudiante','Nombre Estudiante','Apellidos','Nombre Profesor','IDGrupo','IDProfe','Activ','IdMater']]
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
# Saber el promedio de notas por ciclo de determinado de un estudiante envias el ciclo y  id estudiante
# Saber el promedio de notas por Materia  de determinado estudiante envias el string Materia
def consultaNotas( TblEstudiantes:pd.DataFrame, TblNotas:pd.DataFrame, TblMaterias:pd.DataFrame, IDEstud:str = 0, Nota = 0, CicloE:str = 0, Materia:str = 0  ) -> DataFrame:
    
    '''
    Args:
        TblEstudiantes:  DataFrame tabla estudiantes
        TblNotas:        DataFrame tabla notas
        TblMaterias:     DataFrame tabla materias
        IDEstud :        String con el id de estudiante
        Nota :           String con el numero de nota a consultar 
        CicloE :         String con el numero de ciclo a consultar para saber el promedio de un estudiante con su id
        Materia :        String con el nombre de la materia que quieres saber el promedio y el idestudiante   
    '''
    NotasEstudiante = pd.merge(TblEstudiantes,TblNotas,left_on='IDEstudiante',right_on='IDEstudiante')
    NotasEstudiante = pd.merge(NotasEstudiante, TblMaterias, left_on='IDMateria', right_on='IDMateria')


    if IDEstud !=0 and Materia != 0 : 
        NotasEstudiante = NotasEstudiante[(NotasEstudiante.IDEstudiante == IDEstud) & (NotasEstudiante.Materia == Materia)]
        NotasEstudiante['Nota'] = pd.to_numeric(NotasEstudiante['Nota'], errors='ignore')
        total = NotasEstudiante['Nota'].count()
        promedio = NotasEstudiante['Nota'].sum() / total
        NotasEstudiante['Promedio'] = promedio
        NotasEstudiante = NotasEstudiante[['IDEstudiante','Nombres','Apellidos','Materia', 'Nota', 'Creditos' ,'IDMateria', 'IdNota','Ciclo','Promedio','IDGrupo']]    
        NotasEstudiante = NotasEstudiante.set_index(['Promedio','IDEstudiante']) 
        return NotasEstudiante  

    if IDEstud !=0 : 
        NotasEstudiante = NotasEstudiante[NotasEstudiante['IDEstudiante'] == IDEstud ]
        NotasEstudiante['Nota'] = pd.to_numeric(NotasEstudiante['Nota'], errors='ignore')
        total = NotasEstudiante['Nota'].count()
        promedio = NotasEstudiante['Nota'].sum() / total
        NotasEstudiante['Promedio'] = promedio
        NotasEstudiante = NotasEstudiante[['IDEstudiante','Nombres','Apellidos','Materia', 'Nota', 'Creditos' ,'IDMateria', 'IdNota','Ciclo','Promedio','IDGrupo']]    
        NotasEstudiante = NotasEstudiante.set_index(['Promedio','IDEstudiante']) 
        return NotasEstudiante  

    #Saber el promedio de notas
    if IDEstud != 0 and CicloE != 0 :
        NotasEstudiante = NotasEstudiante[(NotasEstudiante.IDEstudiante == IDEstud) & (NotasEstudiante.Ciclo == CicloE)]
        NotasEstudiante['Nota'] = pd.to_numeric(NotasEstudiante['Nota'], errors='ignore')
        total = NotasEstudiante['Nota'].count()
        promedio = NotasEstudiante['Nota'].sum() / total
        NotasEstudiante['Promedio'] = promedio
        NotasEstudiante = NotasEstudiante[['IDEstudiante','Nombres','Apellidos','Materia', 'Nota', 'Creditos' ,'IDMateria', 'IdNota','Ciclo','Promedio','IDGrupo']]    
        NotasEstudiante = NotasEstudiante.set_index(['Promedio','IDEstudiante']) 
        return NotasEstudiante  
    
    if Nota !=0:
        NotasEstudiante = NotasEstudiante[NotasEstudiante['Nota'] >= Nota]     
    NotasEstudiante = NotasEstudiante.sort_values(by = 'Apellidos' )
    NotasEstudiante['Ciclo'] = pd.to_numeric(NotasEstudiante['Ciclo'], errors='ignore')
    NotasEstudiante = NotasEstudiante[['IDEstudiante','Nombres','Apellidos','Materia', 'Nota', 'Creditos' ,'IDMateria', 'IdNota','Ciclo','IDGrupo']]
    return NotasEstudiante
    #Llamada a la funcion
    #print(consultaNotas(TblEstudiantes,TblNotas, TblMaterias, IDEstud='JUCA01', Nota=0, CicloE=0, Materia=0))
 
#------------------ FIN CONSULTA DE NOTAS ESTUDIANTES    ---------------------------


#Funcion para calcular el promedio por materia y la Nota final del Ciclo
def consultaPromedios(tblEstudiantes,tblNotas,tblMaterias,idEstudiante = 0):
    '''
    Args:
        TblEstudiantes:  DataFrame tabla estudiantes
        TblNotas:        DataFrame tabla notas
        TblMaterias:     DataFrame tabla materias
        IDEstud :        String con el id de estudiante
    '''
    NotasEstudiante = consultaNotas(tblEstudiantes,tblNotas,tblMaterias,idEstudiante)
    NotasEstudiante = NotasEstudiante.reset_index()
    NotasEstudiante['Creditos'].astype(float)
    datospromedio = NotasEstudiante
    datospromedio = datospromedio[['IDMateria','Materia','Nota','IDEstudiante','Creditos','Ciclo']]
    listaMaterias = [set(datospromedio['IDMateria']),set(datospromedio['IDEstudiante'])]
    datospromedio = datospromedio.set_index(['Materia'])
    datospromedio['Nota'].astype(float)
    datospromedio['Creditos'].astype(float)
    datospromedio=datospromedio.values
    listaprom = []
    listaidmateria = []
    listaidestudiante = []
    listapromciclo =[]
    listaciclo = []
    for est in listaMaterias[1]:
        for idm in listaMaterias[0]:
            promedios = list(map(lambda x:float(x[1]),list(filter(lambda x: x[0]==idm and x[2]==est, datospromedio))))
            if promedios == []:
                promedios = 0.0
            else:
                promedios = np.average(promedios)
            pesomateria = list(set(map(lambda x:float(x[3]),list(filter(lambda x: x[0]==idm and x[2]==est, datospromedio)))))
            cic = list(set(map(lambda x:int(x[4]),list(filter(lambda x: x[0]==idm and x[2]==est, datospromedio)))))
            if cic == []:
                cic = 0
            else:
                cic = cic[0]
            if pesomateria ==[]:
                pesomateria = [0,]
            numeronotas = len(list(map(lambda x:float(x[1]),list(filter(lambda x: x[0]==idm and x[2]==est, datospromedio)))))
            if numeronotas == 0:
                numeronotas = 1
            PromCiclo = ((pesomateria[0]/10) * promedios) / numeronotas
            listaprom.append(promedios)
            listaidmateria.append(idm)
            listaidestudiante.append(est)
            listapromciclo.append(PromCiclo)
            listaciclo.append(cic)
    dfpromedios = pd.DataFrame(list(zip(listaidmateria,listaidestudiante,listaprom,listapromciclo)), columns=['IDMateria','IDEstudiante', 'Promedio','NotaCiclo'])
    NotasEstudiante = pd.merge(left=NotasEstudiante,right=dfpromedios, left_on=['IDMateria','IDEstudiante'], right_on=['IDMateria','IDEstudiante'])
    NotaCiclo1 = NotasEstudiante[['IDEstudiante','Ciclo','NotaCiclo']]
    NotaCiclo1 = NotaCiclo1.groupby(by = ['IDEstudiante','Ciclo']).sum()
    NotasEstudiante.rename({'IDEstudiante': 'PesoNota'}, axis=1)
    NotasEstudiante = pd.merge(left=NotasEstudiante,right=NotaCiclo1, left_on=['IDEstudiante','Ciclo'], right_on=['IDEstudiante','Ciclo'])
    NotasEstudiante.columns = ['index', 'IDEstudiante', 'Nombres', 'Apellidos', 'Materia', 'Nota', 'Creditos', 'IDMateria', 'IdNota',  'Ciclo', 'IDGrupo', 'Promedio',  'PesoCiclo',  'NotaFinalCiclo']
    return NotasEstudiante

#------------------ INICIO CREAR EL ULTIMO CONSECUTIVO DE LAS TABLAS MATERIA, O NOTA, O IDGRUPO    ---------------------------

# Se agrega nueva funcionalidad
# Genera un nuevo consecutivo secuencial para segun la tabla
# Materias, o Tabla Notas, o Tabla Grupo al momento del usuario ingresar una nueva materia


def crearConsecutivoIDNumerico(tabla:pd.DataFrame, columna:str = 0 )-> int:
    '''
    Args:
    tabla   :   DataFrame tabla Materias
    columna :   string con la columna de llave da cada tabla 
                ejemplo: 
                IdNota para tabla notas, 
                IDGrupo para grupos, 
                IDMateria para materias.
    ''' 
    tabla[ columna ] = pd.to_numeric(tabla[ columna ], errors='ignore')
    nuevoConsecutivo = tabla [ columna ].max() + 1 
    return nuevoConsecutivo
#--------------------Se crea la funcion de validar el ID de los profesores y crear un codigo-------------------
def ConsultarIDProfesor(Diccionario_Profesores: dict, IDProfesor):
    return IDProfesor in Diccionario_Profesores.keys()

def crearIDProfesor(Diccionario_Profesores:dict):
    lista =[]
    for llave in Diccionario_Profesores.keys():
        letra, numero = llave[0], int(llave[1:])
        lista.append(numero)
    Nmax = max(lista)
    nuevoID = Nmax + 1
    nuevoID = "P"+ str(nuevoID)
    if ConsultarIDProfesor(Diccionario_Profesores, nuevoID) == False:
        return nuevoID 
    else:
        return "CrearCodigoManual"

#------------------ FIN SABER EL ULTIMO CONSECUTIVO DE LA TABLA MATERIA    ---------------------------

#------------------Se crean las funciones para Crear Diccionarios de Objetos-------------------------------------

def creaDiccionarioObjetos(DataFrame,objeto) -> dict:
    '''
    Args:
        tblMaterias:  Ingrese el DataFrame de materias
    '''
    diccionario = {}
    for datos in DataFrame.values:
        diccionario[datos[0]] = objeto(list(datos))
    return diccionario


