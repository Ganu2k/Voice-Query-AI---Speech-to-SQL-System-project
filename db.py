import sqlite3

def get_connection():
    return sqlite3.connect("sample_db.sqlite")

def execute_query(query):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(query)
    results = cursor.fetchall()
    
    conn.close()
    return results

