import os
import glob
import pandas as pd

# load and merge all data sets in folder
def load_data(dir_data):
    temp_df = None
    for file in glob.glob(dir_data):
        if temp_df is None:
            temp_df = pd.read_csv(file).head(0)
        print(file)
        df = pd.read_csv(file)
        temp_df = pd.concat([temp_df,df])

def column_split(df):
    # TODO  delete euro sign and m^2 ; seperate content of feature and feature2 columns.

def cleansing(df):
    # return description of necessary cleansing processes.
    txt = 'The following data cleansing steps have happend: '
    #drop duplicats
    if df.hasduplicats:
        df.drop_duplicates()
        txt.append('; droped duplicats')
    # TODO add missing cleansing process
    return df,txt

def load_to_database(df,name: str):
    # TODO add credentials file for specifications of database
    engine = create_engine()
    df.to_sql('name', engine, if_exists='replace')

def settings():
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

if __name__ == '__main__':
    # TODO add credentials
    data = load_data('')
    cleansing(temp_df)
    settings()