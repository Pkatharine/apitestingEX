import json

import pyodbc as pyodbc
import requests


class Connection:

    def __init__(self):
        self.server = 'eventsexpress.database.windows.net'
        self.database = 'EventsExpress'
        self.username = 'katya'
        self.password = 'Popalava09'
        self.driver= 'ODBC Driver 17 for SQL Server'
        self.conn = pyodbc.connect('DRIVER='+self.driver+
                                   ';SERVER='+self.server+
                                   ';PORT=1433;DATABASE='+self.database+
                                   ';UID='+self.username+
                                   ';PWD='+ self.password)
        self.cursor = self.conn.cursor()

    def delete_user_with_email(self, name):
        self.cursor.execute("Delete from Users where Email like ?", name)
        self.cursor.commit()

    def delete_category_with_name(self, name):
        self.cursor.execute("Delete from Categories where Name like ?", name)
        self.cursor.commit()

    def edit_category_with_name(self, name, set):
        self.cursor.execute("Update Categories set Name = ? where Name like ?", (set,name))
        self.cursor.commit()


    def close(self):
        self.conn.close()

