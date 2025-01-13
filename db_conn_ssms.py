import pyodbc
conn_str=(

"DRIVER={ODBC Driver 17 for SQL Server};"

"SERVER=OMKAR\SQLEXPRESS03;"

"DATABASE=python;"
"Trusted_Connection=yes;"
)
conn=pyodbc.connect(conn_str)
cur=conn.cursor()
cur.execute("create table jay1 (emp_id int, name varchar(20))")
cur.commit()
conn.close()