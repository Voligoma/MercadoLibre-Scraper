import pandas as pd
import os

def compare(file1, file2, columna):
    df_new = pd.read_csv(file1, sep=None)
    df_old = pd.read_csv(file2, sep=None)
    new_articles = df_new[columna].isin(df_old[columna])
    new_articles = df_new[~new_articles]
    print(new_articles)
    try:
        new_articles.to_csv(r"data/mercadolibre_data_dif.csv", sep=";")
    except FileExistsError:
        os.remove("data/mercadolibre_data_odif.csv")
        new_articles.to_csv(r"data/mercadolibre_data_dif.csv", sep=";")
        print("Archivo dif antiguo eliminado")
    except FileNotFoundError:
        print("el archivo no existe creeando.... ") 
        new_articles.to_csv(r"data/mercadolibre_data_dif.csv", sep=";") 
    

compare("data/mercadolibre_data.csv", "data/mercadolibre_data_old.csv", "title")