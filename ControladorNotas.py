#Modulo Central de la app, que integra y ejecuta los modulos
#Modulo Central de la app, que integra y ejecuta los modulos
import pandas as pd
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
