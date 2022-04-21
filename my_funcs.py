import sqlite3
from datetime import *
import bcrypt

connection = sqlite3.connect('competency_tracking.db')

cursor = connection.cursor()

# ****************************** 1 Create a Person Record  *******************************
def create_person(new_first_name, new_last_name, new_phone, new_email, hashed, new_date_created, new_hire_date, new_user_type):

    new_records = [new_first_name, new_last_name, new_phone, new_email, hashed, new_date_created, new_hire_date, new_user_type]

    cursor.execute("INSERT INTO Users (first_name, last_name, phone, email, password, date_created, hire_date, user_type) VALUES (?,?,?,?,?,?,?,?)", new_records)

    connection.commit()

    print(f'\nCustomer {new_first_name} {new_last_name} Successfully Added')

# ****************************** 2 Create a competency Record  *******************************
def create_competency(comp_name, comp_date):
    new_records = [comp_name, comp_date]

    cursor.execute("INSERT INTO Competencies (name, date_created) VALUES(?,?)", new_records)

    connection.commit()

    print(f'\nCompetency {comp_name} Successfully Added\n')

    # ****************************** 3 Create a new assessmen to a competency Record  *********************
def create_assessment(asmt_competencies, asmt_name, asmt_date):
    new_records = [asmt_competencies, asmt_name, asmt_date]

    cursor.execute("INSERT INTO Assessments (competency_type, name, date_created) VALUES (?,?,?)", new_records)

    connection.commit()
    print(f'\nAssessment {asmt_name} Successfully Added\n')
# ****************************** 4 Add an assessment result for a user for an assessment *********************

def create_assessment_result(selected_user, selected_asmt, score, date_taken, selected_manager):
    new_records = [selected_user, selected_asmt, score, date_taken, selected_manager]

    cursor.execute("INSERT INTO Assessment_Results (user_id,assessment_id,competency_score,date_taken,manager_id) VALUES (?,?,?,?,?)", new_records)

    connection.commit()
    print(f'\nAssessment Record Successfully Added\n')
# ****************************** VIEW ACTIVE USERS *********************
def view_active_users():
    print("\n-- Users --\n")
    rows = cursor.execute("SELECT * FROM Users WHERE user_type LIKE '%User%'AND active=1").fetchall()
    print(f'{"ID":5}{"First Name":15}{"Last Name":15}{"Email":22}{"Account Type"}')
    for c in rows:
        c = [str(x) for x in c]
        print(f'{c[0]:5}{c[1]:15}{c[2]:15}{c[4]:22}{c[-2]}')

# ****************************** VIEW ACTIVE Managers *********************
def view_active_Manager():
    print("\n-- Managers --\n")
    rows = cursor.execute("SELECT * FROM Users WHERE user_type LIKE '%Manager%' AND active=1").fetchall()
    print(f'{"ID":5}{"First Name":15}{"Last Name":15}{"Email":22}{"Account Type"}')
    for c in rows:
        c = [str(x) for x in c]
        print(f'{c[0]:5}{c[1]:15}{c[2]:15}{c[4]:22}{c[-2]}')

# ****************************** VIEW ACTIVE Competencies *********************
def view_active_competencies():
    comp_list = []
    print("\n-- Competencies --\n")
    rows = cursor.execute("SELECT * FROM Competencies WHERE active=1").fetchall()
    print(f'{"ID":5}{"Competency Name":30}{"Date Created":15}')
    for row in rows:
        temp_row = [str(x) for x in row]
        new_row = {
            "comp_id":temp_row[0],
            "name":temp_row[1],
            "date_created":temp_row[2],
            "active":temp_row[3]
        }
        comp_list.append(new_row)
    for row in comp_list:
        print(f'{row["comp_id"]:5}{row["name"]:30}{row["date_created"]:15}')
    return comp_list
# ****************************** VIEW ACTIVE Assessments *********************

def view_active_assessments():
    print("\n-- Assessments --\n")
    rows = cursor.execute("SELECT * FROM Assessments WHERE active=1").fetchall()
    print(f'{"ID":5}{"Competency Name"}')
    for c in rows:
        c = [str(x) for x in c]
        print(f'{c[0]:5}{c[2]}')
# ****************************** VIEW ACTIVE Assessments *********************

def view_active_assessmentsx():
    print("\n-- Competencies --\n")
    rows = cursor.execute("SELECT * FROM Assessments WHERE active=1").fetchall()
    print(f'{"ID":5}{"Competency Name"}')
    for c in rows:
        c = [str(x) for x in c]
        print(f'{c[1]:5}{c[2]}')
# ****************************** Search by Last Name *******************
def first_name_search(search_name):
    print("\n-- User Info --\n")
    rows = cursor.execute("SELECT * FROM Users WHERE first_name LIKE ? AND active=1", ['%'+search_name+'%']).fetchall()
    print(f'{"ID":5}{"First Name":15}{"Last Name":15}{"Email":22}{"Account Type"}')
    for c in rows:
        c = [str(x) for x in c]
        print(f'{c[0]:5}{c[1]:15}{c[2]:15}{c[4]:22}{c[-2]}')
# ****************************** Search by last name *******************
def last_name_search(search_name):
    print("\n-- User Info --\n")
    rows = cursor.execute("SELECT * FROM Users WHERE last_name LIKE ? AND active=1", ['%'+search_name+'%']).fetchall()
    print(f'{"ID":5}{"First Name":15}{"Last Name":15}{"Email":22}{"Account Type"}')
    for c in rows:
        c = [str(x) for x in c]
        print(f'{c[0]:5}{c[1]:15}{c[2]:15}{c[4]:22}{c[-2]}')
# ****************************** VIEW user by competency *******************
def view_user_comps(input_user):
    user_comps = cursor.execute("SELECT u.first_name, u.last_name, a.competency_type, a.name, ar.competency_score FROM Assessments a, Users u, Assessment_Results ar WHERE u.user_id = ar.user_id AND ar.assessment_id = a.assessment_id AND u.user_id=?", (input_user))
    connection.commit()
    print(f'\n{"First Name":15}{"Last Name":15}{"Competency Type":18}{"Competency Name":30}{"Score"}')
    for c in user_comps:
        c = [str(x) for x in c]
        print(f'{c[0]:15}{c[1]:15}{c[2]:18}{c[3]:30}{c[4]}')

# ****************************** VIEW competencies by user *******************
def view_comps_by_user(selected_comp):
    selected_comps = cursor.execute("SELECT a.competency_type, a.name, u.first_name, u.last_name, ar.competency_score FROM Assessments a, Users u, Assessment_Results ar WHERE u.user_id = ar.user_id AND ar.assessment_id = a.assessment_id AND competency_type=?", (selected_comp))
    connection.commit()
    print(f'\n{"Competency Type":18}{"Competency Name":30}{"First Name":15}{"Last Name":15}{"Score"}')
    for c in selected_comps:
        c = [str(x) for x in c]
        print(f'{c[0]:18}{c[1]:30}{c[2]:15}{c[3]:18}{c[4]}')

# ****************************** VIEW Assessments by user *******************
def view_asmts_by_user(input_user):
    selected_asmts = cursor.execute("SELECT ar.assessment_id, u.first_name, u.last_name, a.name, ar.competency_score FROM Assessments a, Users u, Assessment_Results ar WHERE u.user_id = ar.user_id AND ar.assessment_id = a.assessment_id AND ar.active=1 AND u.user_id=?", (input_user))
    connection.commit()
    print(f'\n{"Assessment ID":15}{"First Name":15}{"Last Name":15}{"Name":30}{"Score"}')
    for c in selected_asmts:
        c = [str(x) for x in c]
        print(f'{c[0]:15}{c[1]:15}{c[2]:15}{c[3]:30}{c[4]}')
# ****************************** deactivate an assessment record*******************
def delete_assessment_result(input_user,deac_asmt):
    cursor.execute("UPDATE Assessment_Results SET active=0 WHERE user_id=? AND assessment_id=?",(input_user,deac_asmt))
    connection.commit()
    print("\n****Record has been DELETED!****")

# ****************************** edit user *******************

def edit_user_view():
    user_list = []
    print("\n---Users---\n")
    rows = cursor.execute("SELECT * FROM Users WHERE active=1").fetchall()
    print(f'{"ID":5}{"First Name":17}{"Last Name":17}{"Phone":15}{"Email":30}{"Date Created":23}{"Hire Date":23}{"User Type"}')
    for row in rows:
        temp_row = [str(x) for x in row]
        new_row = {
            "user_id":temp_row[0],
            "first_name":temp_row[1],
            "last_name":temp_row[2],
            "phone":temp_row[3],
            "email":temp_row[4],
            "password":temp_row[5],
            "date_created":temp_row[6],
            "hire_date":temp_row[7],
             "user_type":temp_row[8],
            "active":temp_row[9]
        }
        user_list.append(new_row)
    for row in user_list:
        print(f'{row["user_id"]:5}{row["first_name"]:17}{row["last_name"]:17}{row["phone"]:15}{row["email"]:30}{row["date_created"]:23}{row["hire_date"]:23}{row["user_type"]}')
    return user_list
# ****************************** edit Assessment *******************

def edit_assessment_view():
    user_list = []
    print("\n---Assessments---\n")
    rows = cursor.execute("SELECT * FROM Assessments WHERE active=1").fetchall()
    print(f'{"ID":5}{"Competency Type":17}{"Name":17}{"Date Created"}')
    for row in rows:
        temp_row = [str(x) for x in row]
        new_row = {
            "assessment_id":temp_row[0],
            "competency_type":temp_row[1],
            "name":temp_row[2],
            "date_created":temp_row[3],
            "active":temp_row[4]
        }
        user_list.append(new_row)
    for row in user_list:
        print(f'{row["assessment_id"]:5}{row["competency_type"]:17}{row["name"]:17}{row["date_created"]}')
    return user_list


# ****************************** edit Assessment results *******************

def edit_assessment_results_view(input_user, input_asmt):
    user_list = []
    print("\n--- Assessments Results ---\n")
    rows = cursor.execute('''SELECT ar.assessment_id,u.user_id, u.first_name, u.last_name, a.name, ar.competency_score, ar.date_taken, ar.manager_id, Managers.first_name AS "manager_first_name", Managers.last_name AS "manager_last_name", ar.active
FROM Assessments a, Users u, Assessment_Results ar, (SELECT user_id, first_name, last_name FROM Users WHERE user_type='Manager') AS 'Managers' 
WHERE u.user_id = ar.user_id AND ar.assessment_id = a.assessment_id AND ar.active=1 AND u.user_type='User' AND Managers.user_id = ar.manager_id AND u.user_id=? AND ar.assessment_id=?''', (input_user, input_asmt))
    print(f'{"ID":5}{"User ID":8}{"First Name":17}{"Last Name":17}{"Competency Name":30}{"Score":7}{"Date Taken":20}{"Manager ID":12}{"First Name":17}{"Last Name"}')
    for row in rows:
        temp_row = [str(x) for x in row]
        new_row = {
            "assessment_id":temp_row[0],
            "user_id":temp_row[1],
            "first_name":temp_row[2],
            "last_name":temp_row[3],
            "name":temp_row[4],
            "competency_score":row[5],
            "date_taken":temp_row[6],
            "manager_id":temp_row[7],
            "manager_first_name":temp_row[8],
            "manager_last_name":temp_row[9],
            "active":temp_row[10]
        }
        user_list.append(new_row)
    for row in user_list:
        print(f'{row["assessment_id"]:5}{row["user_id"]:8}{row["first_name"]:17}{row["last_name"]:17}{row["name"]:30}{row["competency_score"]:7}{row["date_taken"]:20}{row["manager_id"]:12}{row["manager_first_name"]:17}{row["manager_last_name"]}')
    return user_list
# ************************************* login function *********************************

# def login():
    # email = input("enter email: \n")
    # password = input("enter password: \n")
    # check_sql = cursor.execute("SELECT password FROM Users WHERE email = ?", (email,)).fetchone()

    # if check_sql[0] == "password":
    #     print("Please re-enter password")
    # elif check_sql[0] == bcrypt.hashpw(password.encode('utf-8'), check_sql[0]):

#  ************************************* test login function *********************************
def login_test():
    email = input("enter email: \n")
    password = input("enter password: \n")
    check_sql = cursor.execute("SELECT password FROM Users WHERE email = ?", (email,)).fetchone()
    hashpass = bcrypt.hashpw(password.encode('utf-8'), check_sql[0])

    if check_sql[0] != hashpass:
        print("Please re-enter password")
        
    elif check_sql[0] == hashpass:
        print("Welcome")

    row = cursor.execute("SELECT * FROM Users WHERE email = ? AND active=1", (email,)).fetchone()

    new_row = {
        "user_id":row[0],
        "first_name":row[1],
        "last_name":row[2],
        "phone":row[3],
        "email":row[4],
        "password":row[5],
        "date_created":row[6],
        "hire_date":row[7],
            "user_type":row[8],
        "active":row[9]
    }
    
    return new_row

#  ************************************* single user first name *********************************
def fn_change(my_user_name):
    new_name = input("update first name: ")
    cursor.execute("UPDATE Users SET first_name=? WHERE user_id=?;",(new_name, my_user_name))
    
    print("\nFirst Name was Updated!")

    connection.commit()

#  ************************************* single user last name  function *********************************
def ln_change(my_user_name):
    new_name = input("update last name: ")
    cursor.execute("UPDATE Users SET last_name=? WHERE user_id=?;",(new_name, my_user_name))
    
    print("\nLast Name was Updated!")

    connection.commit()
#  ************************************* single user phone function *********************************
def phone_change(my_user_name):
    new_phone = input("update phone number: ")
    cursor.execute("UPDATE Users SET phone=? WHERE user_id=?;",(new_phone, my_user_name))
    
    print("\nPhone Number was Updated!")

    connection.commit()
#  ************************************* single user email function *********************************
def email_change(my_user_name):
    new_email = input("update email: ")
    cursor.execute("UPDATE Users SET email=? WHERE user_id=?;",(new_email, my_user_name))
    
    print("\nEmail was Updated!")

    connection.commit()
#  ************************************* single user password function *********************************
def pass_change(my_user_name):
    new_pass = input("update password: ").encode()
    hashed = bcrypt.hashpw(new_pass, bcrypt.gensalt())
    cursor.execute("UPDATE Users SET password=? WHERE user_id=?;",(hashed, my_user_name))
    
    print("\nPassword was Updated!")

    connection.commit()

#  ************************************* single user password function *********************************
def view_asmt(my_user_name):
    asmt = cursor.execute('''SELECT ar.assessment_id, u.first_name, u.last_name, a.name, ar.competency_score, ar.date_taken, Managers.first_name AS "manager_first_name", Managers.last_name AS "manager_last_name"
FROM Assessments a, Users u, Assessment_Results ar, (SELECT user_id, first_name, last_name FROM Users WHERE user_type='Manager') AS 'Managers' 
WHERE u.user_id = ar.user_id AND ar.assessment_id = a.assessment_id AND ar.active=1 AND u.user_type = 'User' AND ar.user_id=? AND Managers.user_id = ar.manager_id;''',(my_user_name,))
    connection.commit()
    print(f'\n{"ID":5}{"First Name":15}{"Last Name":15}{"Name":30}{"Score":20}{"Completion Date":20}{"Manager First Name":20}{"Manager Last Name":20}')
    for c in asmt:
        c = [str(x) for x in c]
        print(f'{c[0]:5}{c[1]:15}{c[2]:15}{c[3]:30}{c[4]:20}{c[5]:20}{c[6]:20}{c[7]:20}')