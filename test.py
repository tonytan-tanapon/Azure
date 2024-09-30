from sqlalchemy import create_engine

# Define connection string

server = 'mysqlserverman.database.windows.net'
database = 'mySampleDatabase'
username = 'azureuser'
password = 'ZRLaaMH82pXY@BY'


# Create the connection URL
connection_url = f'mssql+pyodbc://{username}:{password}@{server}:1433/{database}?driver=ODBC+Driver+18+for+SQL+Server'
print(connection_url)
# # Create the SQLAlchemy engine
engine = create_engine(connection_url)

# # Test connection
with engine.connect() as conn:
    print("pass")
    result = conn.execute("SELECT * from [dbo].[test]")
    for row in result:
        print(row)
