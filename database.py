import sqlite3


def create_student(name, age, major):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO students (name, age, major) VALUES (?, ?, ?)', (name, age, major))
        conn.commit()
        cursor.close()
        print(f"Student {name} added successfully.")


def read_students():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()
        cursor.close()
        return students


def main():
    with open('schema.sql', 'r') as f:
        sql_script = f.read()
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.executescript(sql_script)
            print("Database initialized successfully.")


if __name__ == '__main__':
    main()
