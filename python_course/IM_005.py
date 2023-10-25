import pyodbc

# Строка подключения к базе данных MS SQL
connection_string = 'DRIVER={SQL Server};SERVER=<yand.dyndns.org>;DATABASE=<AdventureWorks>;UID=<northwind>;PWD=<northwind>'

# Установка соединения
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# SQL-запрос для выборки товаров с сочетанием букв "wa" из таблицы Production.Product
sql_query = '''
SELECT Name FROM Production.Product WHERE Name LIKE '%wa%'
'''

# Выполнение запроса
cursor.execute(sql_query)
rows = cursor.fetchall()

# Запись данных в таблицу Junk
for row in rows:
    name = row.Name
    data = f'<IM>{name}</IM>'
    insert_query = f"INSERT INTO Junk (Data) VALUES ('{data}')"
    cursor.execute(insert_query)

# Подтверждение транзакции и закрытие соединения
conn.commit()
conn.close()
