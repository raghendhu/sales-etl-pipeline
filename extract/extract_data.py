import pandas as pd
def extract():
    df=pd.read_csv("C:\\Users\\DELL\\Documents\\sales-etl-pipeline\\data\\Sales\\sales_data_sample.csv",header=0)
    df.columns = [c.replace(' ', '_').replace('.', '') for c in df.columns]
    return df