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

def merge(file1, file2, file3, file4, file5):
    df1 = pd.read_csv(file1, sep=";")
    df2 = pd.read_csv(file2, sep=";")  
    df3 = pd.read_csv(file3, sep=";")  
    df4 = pd.read_csv(file4, sep=";")  
    df5 = pd.read_csv(file5, sep=";")      
    
    frames = [df1, df2, df3, df4, df5]
    result = pd.concat(frames)
    result.to_csv(r"data/out.csv", sep=";", index=False)
    
def removeDuplicates (file):
    df = pd.read_csv(file,sep=";")
    df.drop_duplicates(subset=['title'], keep='last', inplace=True, ignore_index=True)
    df.to_csv(r"data/mercadolibre_data.csv", sep=";", index=False)
    
   
merge("data/1.csv","data/2.csv","data/3.csv","data/4.csv","data/5.csv")
removeDuplicates("data/out.csv")    
#compare("data/mercadolibre_data.csv", "data/mercadolibre_data_old.csv", "title")