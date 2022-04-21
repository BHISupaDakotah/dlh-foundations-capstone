import sqlite3
from tabnanny import check
from my_funcs import *
from classes import *
import bcrypt
from csv_exports import *
connection = sqlite3.connect('competency_tracking.db')

cursor = connection.cursor()

# score_dict = {0: "No Competency", 1:"Basic Competency",2:"Intermediate Competency", 3:"Advancded Competency", 4:"Expert Competency"}
# view_active_users()
# selected_user = int(input("Select user by id: "))
# view_active_assessments()
# selected_asmt = int(input("select assessment by id: "))
# score_dict = {0: "No Competency", 1:"Basic Competency",2:"Intermediate Competency", 3:"Advancded Competency", 4:"Expert Competency"}
# for i in score_dict.items():
#     key, value = i
#     print("Grading Values\n")
#     print(f'{key} {value}')
# score = input("\nEnter a score between 0-4: ")
# date_taken = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# view_active_Manager()
# selected_manager = int(input("Enter a manager by id: "))

# create_assessment_result(selected_user, selected_asmt, score, date_taken, selected_manager)


# view_active_users()
# input_user = input("select user by id: ")
# view_user_comps(input_user)

# view_active_users()
# input_user = input("\nselect user by id: ")
# view_asmts_by_user(input_user)

# view_active_users()
# input_user = input("select user by id: ")
# view_asmts_by_user(input_user)
# deac_asmt = input("select assessment to DELETE: ")
# delete_assessment_result(input_user,deac_asmt)


# competencies = view_active_competencies()
# input_id = input("Enter the competency id: ")
# selected_comp = ""
# for comp in competencies:
#     if comp["comp_id"]==input_id:
#         selected_comp = comp
# competency = Competencies(comp["comp_id"], comp["name"], comp["date_created"], comp["active"])
# competency.edit_name()

# competencies = view_active_competencies()
# input_id = input("Enter the competency id: ")
# selected_comp = ""
# for comp in competencies:
#     if comp["comp_id"]==input_id:
#         selected_comp = comp
# competency = Competencies(comp["comp_id"], comp["name"], comp["date_created"], comp["active"])
# competency.edit_date()

# my_users = edit_user_view()
# input_id = input("Enter Users ID: ")
# selected_user = ""
# for user in my_users:
#     if user["user_id"]==input_id:
#         selected_user = user
# user_x = Users(user["user_id"],user["first_name"],user["last_name"], user["phone"], user["email"], user["password"], user["date_created"], user["hire_date"], user["user_type"], user["active"])
# user_x.edit_password()


# my_users = edit_user_view()
# input_id = input("input users id: ")
# for user in my_users:
#     if user["user_id"]==input_id:
#         selected_user = user
# user_x = Users(user["user_id"],user["first_name"],user["last_name"], user["phone"], user["email"], user["password"], user["date_created"], user["hire_date"], user["user_type"], user["active"])
# if bcrypt.checkpw("",user["password"]):
#     print("It Matches!")
# else:
#      print("It Does not Match :(")

# ********* start with the exports tommorrow saturday *******************
# view_active_users()
# input_user = input("\nselect user by id: ")
# view_user_comps(input_user)

# view_active_users()
# input_user = input("\nselect user by id: ")
# csv_comps(input_user)

# all_csv_comps()

#  ********* build the rest of the functions views  tommorrow sunday *******************
# competencies = view_active_competencies()
# input_id = input("Enter the competency id: ")
# selected_comp = ""
# for comp in competencies:
#     if comp["comp_id"]==input_id:
#         selected_comp = comp
# competency = Competencies(comp["comp_id"], comp["name"], comp["date_created"], comp["active"])
# competency.edit_date()

# assessments = edit_assessment_view()
# input_id = input("Enter the Assessment ID: ")
# selected_asmt = ""
# for asmt in assessments:
#     if asmt["assessment_id"]==input_id:
#         selected_asmt = asmt
# assessment = Assessments(asmt["assessment_id"], asmt["competency_type"], asmt["name"], asmt["date_created"], asmt["active"])
# assessment.edit_comp_id()

# assessments = edit_assessment_view()
# input_id = input("Enter the Assessment ID: ")
# selected_asmt = ""
# for asmt in assessments:
#     if asmt["assessment_id"]==input_id:
#         selected_asmt = asmt
# assessment = Assessments(asmt["assessment_id"], asmt["competency_type"], asmt["name"], asmt["date_created"], asmt["active"])
# assessment.edit_comp_id()


# view_active_users()
# input_user = int(input("\nselect user by id: "))
# view_active_assessments()
# input_asmt = int(input("\nselect assessment by id: "))
# assessment_results =  edit_assessment_results_view(int(input_user), int(input_asmt))
# selected_asmt = ""
# for ar in assessment_results:
#     if int(ar["user_id"])==int(input_user) and ar["assessment_id"]==int(input_asmt):
#         selected_asmt = ar
# assessment_result = Assessment_Results(ar["user_id"], ar["assessment_id"],ar["competency_score"],ar["date_taken"],ar["manager_id"], ar["active"])
# assessment_result.edit_score()

# edit_user_view()
# input_user = int(input("\nselect user by id: "))
# edit_assessment_view()
# input_asmt = int(input("\nselect assessment by id: "))
# assessment_results =  edit_assessment_results_view(int(input_user), int(input_asmt))
# input_score = int(input("\nenter score: "))
# selected_asmt = ""
# for ar in assessment_results:
#     if int(ar["user_id"])==int(input_user) and ar["assessment_id"]==int(input_asmt):
#         selected_asmt = ar
# assessment_result = Assessment_Results(ar["user_id"], ar["assessment_id"],ar["competency_score"],ar["date_taken"],ar["manager_id"], ar["active"])
# assessment_result.edit_score(input_user, input_asmt, input_score)
# edit_user_view()
# input_user = int(input("\nselect user by id: "))
# edit_assessment_view()
# input_asmt = int(input("\nselect assessment by id: "))
# assessment_results =  edit_assessment_results_view(int(input_user), int(input_asmt))
# input_date = input("\nenter date(YYYY-MM-DD): ")
# selected_asmt = ""
# for ar in assessment_results:
#     if int(ar["user_id"])==int(input_user) and ar["assessment_id"]==int(input_asmt):
#         selected_asmt = ar
# assessment_result = Assessment_Results(ar["user_id"], ar["assessment_id"],ar["competency_score"],ar["date_taken"],ar["manager_id"], ar["active"])
# assessment_result.edit_date(input_user, input_asmt, input_date)

# edit_user_view()
# input_user = int(input("\nselect user by id: "))
# edit_assessment_view()
# input_asmt = int(input("\nselect assessment by id: "))
# assessment_results =  edit_assessment_results_view(int(input_user), int(input_asmt))
# input_date = input("\nenter date(YYYY-MM-DD): ")
# selected_asmt = ""
# for ar in assessment_results:
#     if int(ar["user_id"])==int(input_user) and ar["assessment_id"]==int(input_asmt):
#         selected_asmt = ar
# assessment_result = Assessment_Results(ar["user_id"], ar["assessment_id"],ar["competency_score"],ar["date_taken"],ar["manager_id"], ar["active"])
# assessment_result.edit_date(input_user, input_asmt, input_date)


#  login function
# def login():
#     email = input("enter email: \n")
#     password = input("enter password: \n")
#     check_sql = cursor.execute("SELECT password FROM Users WHERE email = ?", (email,)).fetchone()

#     if check_sql[0] == "password":
#         print("Please re-enter password")
#     elif check_sql[0] == bcrypt.hashpw(password.encode('utf-8'), check_sql[0]):
#         print("Welcome")
# login()
# count = 3
# while count > 0:
#     if login() not True:

#         try:
#             login()
#         except:
#             print("Incorrect username or password")

#         count -=1
#     print(f'you have {count} more attempts to log in ')

# managerx = str("Manager")

# # login()

# if login_test== managerx:
#     print("Manager")
# else:
#     print("Edit Name")
#     print("Edit Email")
#     print("View Assessments")

# my_user = login_test()

# is_manager = my_user["user_type"] == "Manager" 

# my_user_id = my_user["user_id"]

# if is_manager:
#     print("Manager")
# else:
#     print("User")
#     while True:
#         print("\n**** Welcome to the Competency Tool Tracker ****\n")
#         reg_input = input('''
#         *** Main Menu ***
# ----please select an option below ---

# (V) View Information
# (E) Edit My Information
# (L) Log Out
# ''')
#         if reg_input == "V".upper() or reg_input == "V".lower():
#             my_user_id
#             view_asmt(my_user_id)

#         if reg_input == "E".upper() or reg_input == "E".lower():
#             while True: 
#                 edit_menu = input('''
# **** Edit Menu ****

# Select an Option Below

# (F) Edit First Name
# (L) Edit Last Name
# (N) Edit Phone Number
# (E) Edit Email
# (P) Edit Password
# (Q) Return to main menu
# ''')

#                 if edit_menu == "F".upper() or edit_menu == "F".lower():
#                     my_user_id
#                     fn_change(my_user_id)
    
#                 if edit_menu == "L".upper() or edit_menu == "L".lower():
#                     my_user_id
#                     ln_change(my_user_id)

#                 if edit_menu == "N".upper() or edit_menu == "N".lower():
#                     my_user_id
#                     phone_change(my_user_id)

#                 if edit_menu == "E".upper() or edit_menu == "E".lower():
#                     my_user_id
#                     email_change(my_user_id)

#                 if edit_menu == "P".upper() or edit_menu == "P".lower():
#                     my_user_id
#                     pass_change(my_user_id)

#                 if edit_menu == "Q".upper() or edit_menu == "Q".lower():
#                         print("Quit")
#                         break


#         if reg_input == "L".upper() or reg_input == "L".lower():
#             print("Logging Out - Goodbye!")
#             break

# def logx():
#     print("this is logx")
    
#     email = input("enter email: \n")
#     check_email = cursor.execute("SELECT email FROM Users WHERE email=?", (email,)).fetchone()

#     if check_email[0] == email:
        
#         password = input("enter password: \n")
#         check_sql = cursor.execute("SELECT password FROM Users WHERE email=?", (email,)).fetchone()
#         hashpass = bcrypt.hashpw(password.encode('utf-8'), check_sql[0]) 
#         if hashpass == password:
#             print("Welcome!")
#         else:
#             print("That is the wrong password.")
#     else:
#         print("That is the wrong username.")

#         row = cursor.execute("SELECT * FROM Users WHERE email=? AND active=1", (email,)).fetchone()

#         new_row = {
#             "user_id":row[0],
#             "first_name":row[1],
#             "last_name":row[2],
#             "phone":row[3],
#             "email":row[4],
#             "password":row[5],
#             "date_created":row[6],
#             "hire_date":row[7],
#                 "user_type":row[8],
#             "active":row[9]
#         }
        
#         return new_row

# logx()
