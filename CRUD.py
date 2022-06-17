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

def guardaCambios (materiaActualizada):
    #Lee el csv y lo guarda en el archivo leerDoc
    leerDoc = pd.read_csv('Materias.csv', sep = ";")
    #extrae los nombres de las columnas del dataframe
    filaCambio = list(leerDoc.columns)
    #extra el valor de la primera columna, en este caso "IDMateria"
    filaModificar = filaCambio[0]
    #De la lista escoge el primer valor de la IDMateria, para encontrar la fila a modificar
    IDMateriaFila = materiaActualizada[0]
    #Modifica la fila con  loc, en donde el valor de "IDMateria" sea igual a la modificada
    leerDoc.loc[leerDoc[filaModificar] == IDMateriaFila] = materiaActualizada
    #Escribe los cambios en el csv
    leerDoc.to_csv('Materias.csv', index = False)
    #Retorna el archivo modificado
    return leerDoc
