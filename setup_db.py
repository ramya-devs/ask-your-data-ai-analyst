import sqlite3,pandas as pd
df=pd.read_csv('sales.csv'); con=sqlite3.connect('sales.db')
df.to_sql('sales',con,if_exists='replace',index=False); con.close()
print('sales.db created')
