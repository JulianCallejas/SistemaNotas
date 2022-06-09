#Modulo para las funciones de creacion, lectura, edicion y eliminacion de la información
import pandas as pd
#Se crean las funciones para cargar datos
def CargaNotasCSV():
    # Leyendo archivo csv
    try:
        df1 = pd.read_csv("Notas.csv",dtype=str,sep = ';', index_col = "IdNota")
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
        df1 = pd.read_csv("Materias.csv",dtype=str,sep = ';', index_col = "IDMateria")
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
        df1 = pd.read_csv("Profesores.csv",dtype=str,sep=';', index_col = "IDProfesor")
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
        df1 = pd.read_csv("Estudiantes.csv",dtype=str,sep=';', index_col = "IDEstudiante")
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
        df1 = pd.read_csv("Grupos.csv",dtype=str,sep=';', index_col = "IDGrupo")
        print(df1)
        return df1,1
    except FileNotFoundError:
        return "Archivo no encontrado.", 0
    except pd.errors.EmptyDataError:
        return "No hay informacion que leer", 0  
    except pd.errors.ParserError:
        return "Error de analisis", 0  
    except Exception:
        return "Alguna otra Exepcion", 0  
    
def consultaMateriasXProfesor ( df : pd.DataFrame, df2: pd.DataFrame, IDProf:str = 0, IDMate:str = 0 ):
    #Se llaman las funciones para cargar las tablas

    # Dividir (explotar) entrada de cadena de marco de datos de pandas en filas separadas
    # Dataframe.assign()El método asigna nuevas columnas a un DataFrame, 
    # devolviendo un nuevo objeto (una copia) con las nuevas columnas agregadas a las originales.
    # Las columnas existentes que se reasignan se sobrescribirán.
    # Ejemplo: Asigne una nueva columna llamada Materia
    MateriasXProfesor =df.assign(Materia=df.IDMateria.str.split(",")).explode('Materia')
    if IDMate !=0:
        MateriasXProfesor = MateriasXProfesor[MateriasXProfesor.Materia == IDMate]
    #Se define cuales van a ser las llaves para hacer la union en cada tabla
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
    return MateriasXProfesor[[ 'Nombre','Materia','IDMateria']]

df,f = CargaProfesoresCSV()
df2,g = CargaMateriasCSV()    
consultaMateriasXProfesor(df,df2)    
    
