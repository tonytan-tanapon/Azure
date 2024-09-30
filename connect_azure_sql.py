# servername: mysqlserverman.database.windows.net
# database name: mySampleDatabase
# user: azureuser
# pass: ZRLaaMH82pXY@BY

import pyodbc

# Define connection string
server = 'mysqlserverman.database.windows.net'
database = 'mySampleDatabase'
username = 'azureuser'
password = 'ZRLaaMH82pXY@BY'
driver = '{ODBC Driver 18 for SQL Server}'

# Create connection

connection_string = f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'
print(connection_string)
# Establish connection
conn = pyodbc.connect(connection_string)

# Create a cursor
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * from [dbo].[test]")

# Fetch results
rows = cursor.fetchall()

# Print results
for row in rows:
    print(row)

# Close connection
cursor.close()
conn.close()
