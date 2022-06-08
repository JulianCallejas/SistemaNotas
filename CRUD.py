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
