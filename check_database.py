import sqlite3

def check_database(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM financial_table")
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    db_path = 'example.db'
    rows = check_database(db_path)
    for row in rows:
        print(row)
