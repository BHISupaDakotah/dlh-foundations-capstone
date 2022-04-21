import sqlite3

def create_schema(cursor):
    # opens txt file (table_func)
    with open('create_table.sql', 'r') as sql_file:
        # variable to read file
        data = sql_file.read()
        #  calling executescript with data variable
        cursor.executescript(data)

# connecting to specific database
connection = sqlite3.connect('competency_tracking.db')

cursor = connection.cursor()

create_schema(cursor)