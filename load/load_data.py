import pyodbc
def load(df):
    conn=pyodbc.connect(
       "Driver={ODC Driver `8 for SQL Server};"
        "Server=localhost;"
        "DATABASE=sales_etl;"
        "Trusted_Connection=yes;"
    )

    cursor=conn.cursor()

    for index,row in df.iterrows():
        cursor.execute("""INSERT INTO SALES(Product,Quantity,Price,Total_Amount)
                       VALUES (?,?,?,?)""",row['Product'],row['Quantity'],row['Price'],row['Total_Amount']
                       )
        
    conn.commit()
    conn.close()