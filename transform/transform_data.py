def transform(df):
    df.dropna(inplace=True)
    df['Total_Amount']=df['Quantity']*df['Price']
    return df