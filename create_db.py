import sqlite3

conn = sqlite3.connect("sample_db.sqlite")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
)
""")

cursor.executemany("""
INSERT INTO employees (name, department, salary)
VALUES (?, ?, ?)
""", [
    ("Ganesh", "IT", 50000),
    ("Ravi", "HR", 40000),
    ("Anu", "IT", 60000),
    ("Priya", "Finance", 55000)
])

conn.commit()
conn.close()
print("Data Base created sucessfully")