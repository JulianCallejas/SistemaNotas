#Modulo Central de la app, que integra y ejecuta los modulos

import pandas as pd

def CargaNotasCSV():
    # Leyendo archivo csv
    try:
        df1 = pd.read_csv("Notas.csv",dtype=str,sep = ';')
        return df1,1
    except FileNotFoundError:
        print("Archivo no encontrado.")    
    except pd.errors.EmptyDataError:
        print("No hay informacion que leer")   
    except pd.errors.ParserError:
        print("Error de analisis")  
    except Exception:
        print("Alguna otra Exepcion")   
