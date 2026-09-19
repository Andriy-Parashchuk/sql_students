import sqlite3


def main():
    with open('schema.sql', 'r') as f:
        sql_script = f.read()
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.executescript(sql_script)
            print("Database initialized successfully.")


if __name__ == '__main__':
    main()
