import sqlite3

class FinancialDataGateway:
    def __init__(self, db_path):
        self.db_path = db_path

    def fetch_data(self, query):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data
