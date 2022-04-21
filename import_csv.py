import csv
from dataclasses import field
import sqlite3 


def csv_results():
    connection = sqlite3.connect('competency_tracking.db')
    cursor = connection.cursor()

    with open('assessment_result_import.csv', "r") as csvfile:
        # contents = csv.reader(file)

        # insert_records = "INSERT INTO Assessment_Results (user_id, assessment_id, competency_score, date_taken, manager_id) VALUES (?,?,?,?,?)"
        # fields = next(csvfile)
        rows = csv.reader(csvfile)
        for row in rows:
            # print(row)
            insert_sql = '''INSERT INTO Assessment_Results (user_id, assessment_id, competency_score, date_taken, manager_id) VALUES
        (?,?,?,?,?)'''
        cursor.execute(insert_sql, row)
        connection.commit()