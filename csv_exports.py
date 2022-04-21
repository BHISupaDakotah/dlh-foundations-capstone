import csv
import os
import sqlite3 

# def csv_exports():

#     connection = sqlite3.connect('competency_tracking.db')

#     cursor = connection.cursor()

#     cursor.execute("SELECT * FROM Users")

#     with open("users.csv" , "w") as csvfile:
#         csv_writer = csv.writer(csvfile, delimiter=",")
#         csv_writer.writerow([i[0] for i in cursor.description])
#         csv_writer.writerows(cursor)

#         dirpath = os.getcwd() + "users.csv"

def all_csv_comps():
    connection = sqlite3.connect('competency_tracking.db')

    cursor = connection.cursor()

    user_comps = cursor.execute("SELECT ar.assessment_id, u.first_name, u.last_name, a.name, ar.competency_score FROM Assessments a, Users u, Assessment_Results ar WHERE u.user_id = ar.user_id AND ar.assessment_id = a.assessment_id AND ar.active=1")
    connection.commit()

    with open("all_comps.csv" , "w") as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=",")
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)

        dirpath = os.getcwd() + "all_comps.csv"



def csv_comps(input_user):
    connection = sqlite3.connect('competency_tracking.db')

    cursor = connection.cursor()

    user_comps = cursor.execute("SELECT u.first_name, u.last_name, a.competency_type, a.name, ar.competency_score FROM Assessments a, Users u, Assessment_Results ar WHERE u.user_id = ar.user_id AND ar.assessment_id = a.assessment_id AND u.user_id=?", (input_user))
    connection.commit()

    with open("comps_for_user.csv" , "w") as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=",")
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)

        dirpath = os.getcwd() + "comps_for_user.csv"


# view_user_comps(input_user)
# csv_comps(input_user)



