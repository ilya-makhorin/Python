import pyodbc

server = 'yand.dyndns.org'
database = 'AdventureWorks'
user = 'northwind'
password = 'northwind'


class Product:
    def __init__(self, productID, name, productNumber, listPrice):
        self.productID = productID
        self.name = name
        self.productNumber = productNumber
        self.listPrice = listPrice


class ProductRepository:
    def __init__(self):
        self.connection_string = f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={user};PWD={password}"

    def get_all_products(self):
        query = "SELECT ProductID, Name, ProductNumber, ListPrice FROM Production.Product"
        return self.__execute_query(query)

    def get_products_starting_with(self, starting_letter):
        query = f"SELECT ProductID, Name, ProductNumber, ListPrice FROM Production.Product WHERE Name LIKE '{starting_letter}%'"
        return self.__execute_query(query)

    def get_products_in_price_range(self, min_price, max_price):
        query = f"SELECT ProductID, Name, ProductNumber, ListPrice FROM Production.Product WHERE ListPrice BETWEEN {min_price} AND {max_price}"
        return self.__execute_query(query)

    def __execute_query(self, query):
        with pyodbc.connect(self.connection_string) as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()

        products = []
        for row in results:
            productID = row[0]
            name = row[1]
            productNumber = row[2]
            listPrice = row[3]
            product = Product(productID, name, productNumber, listPrice)
            products.append(product)

        return products