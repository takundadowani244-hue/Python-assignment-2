import sqlite3
connection = sqlite3.connect("students.db")
cursor = connection.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
""")

# Insert some data
students_data = [
    ("Takunda", 20),
    ("Timothy", 25),
    ("Takudzwa", 22)
]
cursor.executemany("INSERT INTO students (name, age) VALUES (?, ?)", students_data)
connection.commit()

# Retrieve and display the data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("Students table contents:")
for row in rows:
    print(row)

connection.close()




