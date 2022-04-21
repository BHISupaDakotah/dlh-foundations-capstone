import sqlite3

connection = sqlite3.connect('competency_tracking.db')

cursor = connection.cursor()

competency_records = [
    (1,"Computer Anatomy", "2022-04-07", 1),
    (2,"Data Types", "2022-04-07", 1),
    (3,"Variables", "2022-04-07",1),
    (4,"Functions", "2022-04-07",1),
    (5,"Boolean Logic", "2022-04-07",1),
    (6,"Conditionals", "2022-04-07",1),
    (7,"Loops", "2022-04-07",1),
    (8,"Lists", "2022-04-07",1),
    (9,"Dictionaries", "2022-04-07",1),
    (10,"Working with Files", "2022-04-07",1),
    (11,"Exception Handling", "2022-04-07",1),
    (12,"Quality Assurance (QA)", "2022-04-07",1),
    (13,"Object-Oriented Programming", "2022-04-07",1),
    (14,"Recursion", "2022-04-07",1),
    (15,"Databases", "2022-04-07",1)
]

sql_update = "INSERT INTO Competency (comp_id, name, date_created, active) VALUES (?,?,?,?)"
cursor.executemany(sql_update, competency_records)

connection.commit()