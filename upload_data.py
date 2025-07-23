import numpy as np
import pandas as pd
import time
import sqlalchemy

def read_csv(path):
    #Formating the file to make it easy to read by Pandas
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = [line.replace('"', '') for line in lines]

    with open('./hp_data.csv', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    return pd.read_csv('./hp_data.csv', sep=';')

def save_csv(df, path):
    df.to_csv(path, sep=";", index=False)

def format_csv():
    #Read the file
    df = read_csv('./hp_data_raw.csv')

    #Renaming the columns
    df.columns = [
        "canal", "campanha", "grupo_anuncio", "data",
        "impressoes", "cliques", "leads", "valor_gasto"
    ]

    #Changing all the Excel/Sheets date format to YYYY-mm-dd format
    df['data'] = pd.to_datetime("1899-12-30") + pd.to_timedelta(df["data"], unit="D")

    #Replacing ',' by '.'
    df[['leads', 'valor_gasto']] = df[['leads', 'valor_gasto']].apply(lambda col: 
                                                                    col.str.replace(",", "."))

    #Approaching the float values to the lowest integer (lead value should not be float)
    df['leads'] = np.floor(df['leads'].astype('float'))

    #Filling the NaN values to 0 and setting the correct types of the columns
    df[['impressoes', 'cliques', 'leads']] = df[['impressoes', 'cliques', 'leads']].apply(lambda col: 
                                                                                        col.fillna(0)
                                                                                        .astype(int))
    
    save_csv(df, "./hp_data.csv")

    return df

def db_connect():
    #Wait for database to load
    time.sleep(10)

    #Connect with the Database
    return sqlalchemy.create_engine("mysql+pymysql://admin:admin@mysql:3306/hp_mysql")

def db_insert_data():
    #Read the csv file
    df = format_csv()

    #Connect to DB
    engine = db_connect()

    #Insert the data on table
    df.to_sql("performance_campanhas", con=engine, if_exists='append', index=False)
    print("The data was inserted with success")

db_insert_data()