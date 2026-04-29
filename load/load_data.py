from sqlalchemy import create_engine
import urllib
def load(df):
    conn=(
       "Driver={ODC Driver `8 for SQL Server};"
        "Server=localhost;"
        "DATABASE=SSIS_Tasks;"
        "Trusted_Connection=yes;"
    )
    quoted_conn = urllib.parse.quote_plus(conn)
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={quoted_conn}")

    df.to_sql('SALES_FULL_REPORT', schema='dbo', con=engine, if_exists='replace', index=False)

    print(f"✅ Success! Table created with {len(df.columns)} columns and {len(df)} rows.")