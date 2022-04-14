import pandas as pd
import numpy as nm

df = pd.read_csv('finance1.csv', encoding='latin-1')
pd.options.display.width= None
pd.options.display.max_columns= None
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)

#print(df.head())
df1 = df.dropna()
#print(df1.info())
df1['Starting Date']= pd.to_datetime(df1['Starting Date'])
#print(df1.info())
#print(df1.head())
df1['s_year']=df1['Starting Date'].dt.year

