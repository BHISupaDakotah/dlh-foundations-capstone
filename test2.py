from datetime import *
from my_funcs import *
from classes import *
from csv_exports import *
from import_csv import *
import sqlite3
import bcrypt

my_user = login_test()
is_manager = my_user["user_type"] == "Manager" 
my_user_id = my_user["user_id"]

connection = sqlite3.connect('competency_tracking.db')
cursor = connection.cursor()

if is_manager:
    while True:
        print("\n**** Welcome to the Competency Tool Tracker ****\n")
        reg_input = input('''
        *** Main Menu ***
----please select an option below ---

(V) View Information
(A) Add Information
(E) Edit Information
(D) Delete Information
(X) Export a CSV
(I) Import a CSV
(L) Log Out
''')
    #  if user selects V
        if reg_input == "V".upper() or reg_input == "V".lower():
            while True:
                enter_add_menu = input('''
(V) continue to View menu
(Q) exit to main menu
''').upper()
                if enter_add_menu == "Q".upper():
                    print("\nReturning to main menu\n")
                    break

                if enter_add_menu == "V".upper():
                    while True:
                        add_menu = input('''
        *** View Menu ***

(U) View all users in a list
(S) Search a user by first or last name
(C) View a competency level report for an individual user
(R) View a report of all users and their competency levels for a given user
(A) View a list of assessments for a given user
(Q) Return to main menu
''')

                        if add_menu == "U".upper() or add_menu == "u".lower():
                            view_active_users()
                            
                        if add_menu == "S".upper() or add_menu == "s".lower():
                            while True:
                                search_item = input('''
(F) search by first name
(L) search by last name
(Q) return to view menu
''')
                                if search_item == "F".upper() or search_item == "F".lower():
                                    search_name = input("Enter first name: ")
                                    first_name_search(search_name)
                                    
                                if search_item == "L".upper() or search_item == "L".lower():
                                    search_name = input("Enter last name: ")
                                    last_name_search(search_name)

                                if search_item == "Q".upper() or search_item == "Q".lower():
                                    print("returning to search menu")
                                    break

                        if add_menu == "C".upper() or add_menu == "c".lower():
                            view_active_users()
                            input_user = input("\nselect user by id: ")
                            view_user_comps(input_user)

                        if add_menu == "R".upper() or add_menu == "r".lower():
                            view_active_assessments()
                            selected_comp = input("\nselect competency by ID: ")
                            view_comps_by_user(selected_comp)
                            
                        if add_menu == "A".upper() or add_menu == "a".lower():
                            view_active_users()
                            input_user = input("\nselect user by id: ")
                            view_asmts_by_user(input_user)

                        if add_menu == "Q".upper() or add_menu == "q".lower():
                            print("returning to main menu")
                            break
                else: 
                    print("Please enter V or Q")
    # if user selects A
        if reg_input == "A".upper() or reg_input == "A".lower():
            while True:
                enter_add_menu = input('''
(A) continue to the add menu
(Q) exit to main menu
''').upper()
                if enter_add_menu == "Q".upper():
                    print("\nReturning to main menu\n")
                    break

                if enter_add_menu == "A".upper():
                    while True:
                        add_menu = input('''
            *** Add Menu ***

(U) Add a user
(C) Add a competency
(A) Add a new assessment to a competency
(R) Add an assessment result for a user for an assessment
(Q) Return to main menu
''')

                        if add_menu == "U".upper() or add_menu == "u".lower():
                            print("\n### New User ###\n")
                            print("Please fill out the form below to create a new person: \n")
                            new_first_name = input("First Name: ")
                            new_last_name = input("Last Name: ")
                            new_phone = input("Phone: ")
                            new_email = input("Email: ")
                            new_password = input("Enter a password: ").encode()
                            hashed = bcrypt.hashpw(new_password, bcrypt.gensalt())
                            new_date_created = date.today()
                            new_hire_date = date.today()
                            new_user_type = input("User Type(User or Manager): ")

                            create_person(new_first_name, new_last_name, new_phone, new_email, hashed, new_date_created, new_hire_date, new_user_type)
                            break
                        if add_menu == "C".upper() or add_menu == "c".lower():
                            comp_name = input("Competency Name: ")
                            comp_date = date.today()

                            create_competency(comp_name, comp_date)
                            break
                        if add_menu == "A".upper() or add_menu == "a".lower():
                            view_active_competencies()
                            asmt_competencies = input("\nEnter a competencies' ID to enter them into a Assessment: ")
                            asmt_name = input("\nEnter a competencies' Name to enter them into a Assessment: ")
                            asmt_date = date.today()
                            create_assessment(asmt_competencies, asmt_name, asmt_date)
                            view_active_assessments()
                            break

                        if add_menu == "R".upper() or add_menu == "r".lower():
                            score_dict = {0: "No Competency", 1:"Basic Competency",2:"Intermediate Competency", 3:"Advancded Competency", 4:"Expert Competency"}
                            view_active_users()
                            selected_user = int(input("Select user by id: "))
                            view_active_assessments()
                            selected_asmt = int(input("select assessment by id: "))
                            score_dict = {0: "No Competency", 1:"Basic Competency",2:"Intermediate Competency", 3:"Advancded Competency", 4:"Expert Competency"}
                            print("\nGrading Values\n")
                            for i in score_dict.items():
                                key, value = i
                                print(f'{key} {value}')
                            score = input("\nEnter a score between 0-4: ")
                            date_taken = date.today()
                            view_active_Manager()
                            selected_manager = int(input("Enter a manager by id: "))

                            create_assessment_result(selected_user, selected_asmt, score, date_taken, selected_manager)
                            break

                        if add_menu == "Q".upper() or add_menu == "Q".lower():
                            print("returning to add menu")
                            break
                else: 
                    print("Please enter A or Q")
    # user Enters E
        if reg_input == "E".upper() or reg_input == "E".lower():
            while True:
                enter_edit_menu = input('''
    (E) Enter the edit menu
    (R) to return to main menu
    ''').upper()
                if enter_edit_menu == "R".upper():
                    print("\nReturning to main menu\n")
                    break

                if enter_edit_menu == "E".upper():
                    while True:
                        add_menu = input('''
(U) Edit User's information
(C) Edit a Competency
(A) Edit an Assessment
(R) Edit an Assessment Results
(Q) Return to main menu
''')

                        if add_menu == "U".upper() or add_menu == "U".lower():
                            while True:
                                search_item = input('''
(F) Edit User First Name
(L) Edit User Last Name
(N) Edit Phone Number
(E) Edit Email
(P) Edit User Password
(D) Edit Date Created
(H) Edit Hire Date
(U) Edit User Type
(Q) return to view menu
''')
                                if search_item == "F".upper() or search_item == "F".lower():
                                    my_users = edit_user_view()
                                    user_id = input("Enter Users ID: ")
                                    selected_user = ""
                                    for user in my_users:
                                        if user["user_id"]==user_id:
                                            selected_user = user
                                    user_x = Users(user["user_id"],user["first_name"],user["last_name"], user["phone"], user["email"], user["password"], user["date_created"], user["hire_date"], user["user_type"], user["active"])
                                    user_x.edit_fn(user_id)
                                    
                                if search_item == "L".upper() or search_item == "L".lower():
                                    my_users = edit_user_view()
                                    user_id = input("Enter Users ID: ")
                                    selected_user = ""
                                    for user in my_users:
                                        if user["user_id"]==user_id:
                                            selected_user = user
                                    user_x = Users(user["user_id"],user["first_name"],user["last_name"], user["phone"], user["email"], user["password"], user["date_created"], user["hire_date"], user["user_type"], user["active"])
                                    user_x.edit_ln(user_id)

                                if search_item == "N".upper() or search_item == "N".lower():
                                    my_users = edit_user_view()
                                    user_id = input("Enter Users ID: ")
                                    selected_user = ""
                                    for user in my_users:
                                        if user["user_id"]==user_id:
                                            selected_user = user
                                    user_x = Users(user["user_id"],user["first_name"],user["last_name"], user["phone"], user["email"], user["password"], user["date_created"], user["hire_date"], user["user_type"], user["active"])
                                    user_x.edit_phone(user_id)

                                if search_item == "E".upper() or search_item == "E".lower():
                                    my_users = edit_user_view()
                                    user_id = input("Enter Users ID: ")
                                    selected_user = ""
                                    for user in my_users:
                                        if user["user_id"]==user_id:
                                            selected_user = user
                                    user_x = Users(user["user_id"],user["first_name"],user["last_name"], user["phone"], user["email"], user["password"], user["date_created"], user["hire_date"], user["user_type"], user["active"])
                                    user_x.edit_email(user_id)

                                if search_item == "P".upper() or search_item == "P".lower():
                                    my_users = edit_user_view()
                                    user_id = input("Enter Users ID: ")
                                    selected_user = ""
                                    for user in my_users:
                                        if user["user_id"]==user_id:
                                            selected_user = user
                                    user_x = Users(user["user_id"],user["first_name"],user["last_name"], user["phone"], user["email"], user["password"], user["date_created"], user["hire_date"], user["user_type"], user["active"])
                                    user_x.edit_password(user_id)

                                if search_item == "D".upper() or search_item == "D".lower():
                                    my_users = edit_user_view()
                                    user_id = input("Enter Users ID: ")
                                    selected_user = ""
                                    for user in my_users:
                                        if user["user_id"]==user_id:
                                            selected_user = user
                                    user_x = Users(user["user_id"],user["first_name"],user["last_name"], user["phone"], user["email"], user["password"], user["date_created"], user["hire_date"], user["user_type"], user["active"])
                                    user_x.edit_dc(user_id)

                                if search_item == "H".upper() or search_item == "H".lower():
                                    my_users = edit_user_view()
                                    user_id = input("Enter Users ID: ")
                                    selected_user = ""
                                    for user in my_users:
                                        if user["user_id"]==user_id:
                                            selected_user = user
                                    user_x = Users(user["user_id"],user["first_name"],user["last_name"], user["phone"], user["email"], user["password"], user["date_created"], user["hire_date"], user["user_type"], user["active"])
                                    user_x.edit_hd(user_id)

                                if search_item == "U".upper() or search_item == "U".lower():
                                    my_users = edit_user_view()
                                    user_id = input("Enter Users ID: ")
                                    selected_user = ""
                                    for user in my_users:
                                        if user["user_id"]==user_id:
                                            selected_user = user
                                    user_x = Users(user["user_id"],user["first_name"],user["last_name"], user["phone"], user["email"], user["password"], user["date_created"], user["hire_date"], user["user_type"], user["active"])
                                    user_x.edit_user_type(user_id)

                                if search_item == "Q".upper() or search_item == "Q".lower():
                                    print("returning to search menu")
                                    break
                            
                        if add_menu == "C".upper() or add_menu == "c".lower():
                            while True:
                                search_item = input('''
(C) Edit Competency Name
(D) Edit Competency Date Created
(Q) return to view menu
''')
                                if search_item == "C".upper() or search_item == "C".lower():
                                    competencies = view_active_competencies()
                                    comp_id = input("Enter the competency id: ")
                                    selected_comp = ""
                                    for comp in competencies:
                                        if comp["comp_id"]==comp_id:
                                            selected_comp = comp
                                    competency = Competencies(comp["comp_id"], comp["name"], comp["date_created"], comp["active"])
                                    competency.edit_name(comp_id)
                                    
                                if search_item == "D".upper() or search_item == "D".lower():
                                    competencies = view_active_competencies()
                                    comp_id = input("Enter the competency id: ")
                                    selected_comp = ""
                                    for comp in competencies:
                                        if comp["comp_id"]==comp_id:
                                            selected_comp = comp
                                    competency = Competencies(comp["comp_id"], comp["name"], comp["date_created"], comp["active"])
                                    competency.edit_date(comp_id)

                                if search_item == "Q".upper() or search_item == "Q".lower():
                                    print("returning to search menu")
                                    break

                        if add_menu == "A".upper() or add_menu == "a".lower():
                            while True:
                                search_item = input('''
(N) Edit Assessment Name
(D) Edit Assessment Date Created
(Q) return to view menu
''')
                                if search_item == "N".upper() or search_item == "N".lower():
                                    assessments = edit_assessment_view()
                                    asmt_id = input("Enter the Assessment ID: ")
                                    selected_asmt = ""
                                    for asmt in assessments:
                                        if asmt["assessment_id"]==asmt_id:
                                            selected_asmt = asmt
                                    assessment = Assessments(asmt["assessment_id"], asmt["competency_type"], asmt["name"], asmt["date_created"], asmt["active"])
                                    assessment.edit_name(asmt_id)
                                    
                                if search_item == "D".upper() or search_item == "D".lower():
                                    assessments = edit_assessment_view()
                                    asmt_id = input("Enter the Assessment ID: ")
                                    selected_asmt = ""
                                    for asmt in assessments:
                                        if asmt["assessment_id"]==asmt_id:
                                            selected_asmt = asmt
                                    assessment = Assessments(asmt["assessment_id"], asmt["competency_type"], asmt["name"], asmt["date_created"], asmt["active"])
                                    assessment.edit_date(asmt_id)

                                if search_item == "Q".upper() or search_item == "Q".lower():
                                    print("returning to search menu")
                                    break
                            
                        if add_menu == "R".upper() or add_menu == "R".lower():
                            while True:
                                search_item = input('''
(S) Edit Assessment Result Score
(D) Edit Competency Date Created
(Q) return to view menu
''')
                                if search_item == "S".upper() or search_item == "S".lower():
                                    edit_user_view()
                                    input_user = int(input("\nselect user by id: "))
                                    edit_assessment_view()
                                    input_asmt = int(input("\nselect assessment by id: "))
                                    assessment_results =  edit_assessment_results_view(int(input_user), int(input_asmt))
                                    input_score = int(input("\nenter score(0-4): "))
                                    selected_asmt = ""
                                    for ar in assessment_results:
                                        if int(ar["user_id"])==int(input_user) and ar["assessment_id"]==int(input_asmt):
                                            selected_asmt = ar
                                    assessment_result = Assessment_Results(ar["user_id"], ar["assessment_id"],ar["competency_score"],ar["date_taken"],ar["manager_id"], ar["active"])
                                    assessment_result.edit_score(input_user, input_asmt, input_score)
                                    
                                if search_item == "D".upper() or search_item == "D".lower():
                                    edit_user_view()
                                    input_user = int(input("\nselect user by id: "))
                                    edit_assessment_view()
                                    input_asmt = int(input("\nselect assessment by id: "))
                                    assessment_results =  edit_assessment_results_view(int(input_user), int(input_asmt))
                                    input_date = input("\nenter date(YYYY-MM-DD): ")
                                    selected_asmt = ""
                                    for ar in assessment_results:
                                        if int(ar["user_id"])==int(input_user) and ar["assessment_id"]==int(input_asmt):
                                            selected_asmt = ar
                                    assessment_result = Assessment_Results(ar["user_id"], ar["assessment_id"],ar["competency_score"],ar["date_taken"],ar["manager_id"], ar["active"])
                                    assessment_result.edit_date(input_user, input_asmt, input_date)

                                if search_item == "Q".upper() or search_item == "Q".lower():
                                    print("returning to search menu")
                                    break
                            
                        if add_menu == "Q".upper() or add_menu == "q".lower():
                            print("returning to main menu")
                            break
                else: 
                    print("Please enter E or R")
    # user Enters D
        if reg_input == "D".upper() or reg_input == "D".lower():
            while True:
                enter_delete_menu = input('''
   ******DELETE MENU******

*** ACTIONS ARE PERMANENT ***

(DELETE) enter the DELETE menu
(Q) exit to main menu
''').upper()
                if enter_delete_menu == "Q".upper():
                    print("\nReturning to main menu\n")
                    break

                if enter_delete_menu == "DELETE".upper():
                    while True:
                        delete_menu = input('''
(R) DELETE an assessment result
(Q) Return to main menu
''')

                        if delete_menu == "R".upper() or delete_menu == "r".lower():
                            while True:
                                search_item = input('''
(U) search by user
(Q) return to view menu
''')
                                if search_item == "U".upper() or search_item == "u".lower():
                                    view_active_users()
                                    input_user = input("select user by id: ")
                                    view_asmts_by_user(input_user)
                                    deac_asmt = input("select assessment to DELETE: ")
                                    delete_assessment_result(input_user,deac_asmt)

                                if search_item == "Q".upper() or search_item == "Q".lower():
                                    print("returning to search menu")
                                    break
                            
                        if delete_menu == "Q".upper() or delete_menu == "q".lower():
                            print("returning to main menu")
                            break
                else: 
                    print("Please enter DELETE (ALL CAPS) or Q")
    # user Enters X
        if reg_input == "X".upper() or reg_input == "X".lower():
            while True:
                enter_add_menu = input('''
(C) CSV Export menu
(R) return to main menu
''').upper()
                if enter_add_menu == "R".upper():
                    print("\nReturning to main menu\n")
                    break

                if enter_add_menu == "C".upper():
                    while True:
                        add_menu = input('''
(A) View all Competencies
(S) Export CSV for Single User
(Q) Return to main menu
''')

                        if add_menu == "A".upper() or add_menu == "A".lower():
                            all_csv_comps()
                            print("Success! Check 'all_comps.csv' to see results")

                        if add_menu == "S".upper() or add_menu == "S".lower():
                            view_active_users()
                            input_user = input("\nselect user by id: ")
                            csv_comps(input_user)   
                            print("\nSuccess Check 'comps_for_user.csv' to see results")

                        if add_menu == "Q".upper() or add_menu == "q".lower():
                            print("returning to main menu")
                            break
                else: 
                    print("Please enter C or R")
    # user Enters I
        if reg_input == "I".upper() or reg_input == "I".lower():
            while True:
                enter_add_menu = input('''
(Y) continue to the add menu
(N) to return to main menu
''').upper()
                if enter_add_menu == "N".upper():
                    print("\nReturning to main menu\n")
                    break

                if enter_add_menu == "Y".upper():
                    while True:
                        add_menu = input('''
(I) Import CSV
(Q) return to main menu
''')

                        if add_menu == "I".upper() or add_menu == "i".lower():
                            csv_results()
                            
                        if add_menu == "Q".upper() or add_menu == "q".lower():
                            print("returning to main menu")
                            break
                else: 
                    print("Please enter Y or N")
    # if user enters Q
        elif reg_input == "L".upper() or reg_input == "L".lower():
            print("Logging Out - Goodbye!")
            break
else:
    while True:
        print("\n**** Welcome to the Competency Tool Tracker ****\n")
        reg_input = input('''
        *** Main Menu ***
----please select an option below ---

(V) View Information
(E) Edit My Information
(L) Log Out
''')
        if reg_input == "V".upper() or reg_input == "V".lower():
            my_user_id
            view_asmt(my_user_id)

        if reg_input == "E".upper() or reg_input == "E".lower():
            while True: 
                edit_menu = input('''
**** Edit Menu ****

Select an Option Below

(F) Edit First Name
(L) Edit Last Name
(N) Edit Phone Number
(E) Edit Email
(P) Edit Password
(Q) Return to main menu
''')

                if edit_menu == "F".upper() or edit_menu == "F".lower():
                    my_user_id
                    fn_change(my_user_id)
    
                if edit_menu == "L".upper() or edit_menu == "L".lower():
                    my_user_id
                    ln_change(my_user_id)

                if edit_menu == "N".upper() or edit_menu == "N".lower():
                    my_user_id
                    phone_change(my_user_id)

                if edit_menu == "E".upper() or edit_menu == "E".lower():
                    my_user_id
                    email_change(my_user_id)

                if edit_menu == "P".upper() or edit_menu == "P".lower():
                    my_user_id
                    pass_change(my_user_id)

                if edit_menu == "Q".upper() or edit_menu == "Q".lower():
                        print("Quit")
                        break

        if reg_input == "L".upper() or reg_input == "L".lower():
            print("Logging Out - Goodbye!")
            break