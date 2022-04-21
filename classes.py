from datetime import date
import sqlite3
import bcrypt

connection = sqlite3.connect('competency_tracking.db')

cursor = connection.cursor()
class Users:

    def __init__(self, user_id, first_name, last_name, phone, email, password, date_created, hire_date, user_type, active):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.password = password
        self.date_created = date_created
        self.hire_date = hire_date
        self.user_type = user_type
        self.active = active

    def edit_fn(self, user_id):
        self.user_id = user_id
        new_name = input("update first name: ")
        self.first_name = new_name
        cursor.execute("UPDATE Users SET first_name=? WHERE user_id=?",(self.first_name, self.user_id))
        connection.commit()
        print("Name Change Successful!")

    def edit_ln(self, user_id):
        self.user_id = user_id
        new_name = input("update last name: ")
        self.last_name = new_name
        cursor.execute("UPDATE Users SET last_name=? WHERE user_id=?",(self.last_name, self.user_id))
        connection.commit()
        print("Name Change Successful!")

    def edit_phone(self,user_id):
        self.user_id = user_id
        new_number = input("update phone number: ")
        self.phone = new_number
        cursor.execute("UPDATE Users SET phone=? WHERE user_id=?",(self.phone, self.user_id))
        connection.commit()
        print("Phone Number Update Successful!")

    def edit_email(self, user_id):
        self.user_id = user_id
        new_email = input("update email address: ")
        self.email = new_email
        cursor.execute("UPDATE Users SET email=? WHERE user_id=?",(self.email, self.user_id))
        connection.commit()
        print("Email Update Successful!")

    def edit_password(self, user_id):
        self.user_id = user_id
        new_password = input("update password: ").encode()
        self.password = new_password
        hashed = bcrypt.hashpw(self.password, bcrypt.gensalt())
        cursor.execute("UPDATE Users SET password=? WHERE user_id=?",(hashed, self.user_id))
        connection.commit()
        print("Password Update Successful!")

    def edit_dc(self, user_id):
        self.user_id = user_id
        new_date = input("update date created: ")
        self.date_created = new_date
        cursor.execute("UPDATE Users SET date_created=? WHERE user_id=?",(self.date_created, self.user_id))
        connection.commit()
        print("Date Created Update Successful!")

    def edit_hd(self, user_id):
        self.user_id = user_id
        new_date = input("update hire date: ")
        self.hire_date = new_date
        cursor.execute("UPDATE Users SET hire_date=? WHERE user_id=?",(self.hire_date, self.user_id))
        connection.commit()
        print("Hire Date Update Successful!")
        
    def edit_user_type(self, user_id):
        self.user_id = user_id
        new_user_type = input("update user type: ")
        self.email = new_user_type
        cursor.execute("UPDATE Users SET user_type=? WHERE user_id=?",(self.user_type, self.user_id))
        connection.commit()
        print("User Type Update Successful!")

class Competencies:

    def __init__(self, comp_id, name, date_created, active):
        self.comp_id = comp_id
        self.name = name
        self.date_created = date_created
        self.active = active

    def edit_name(self, comp_id):
        self.comp_id = comp_id
        new_name = input("update competency name: ")
        self.name = new_name
        cursor.execute("UPDATE Competencies SET name=? WHERE comp_id=?",(self.name, self.comp_id))
        connection.commit()
        print("Name Change Successful!")

    def edit_date(self, comp_id):
        self.comp_id = comp_id
        print("date format YYYY-MM-DD")
        new_date = input("update date created: ")
        self.date_created = new_date
        cursor.execute("UPDATE Competencies SET date_created=? WHERE comp_id=?",(self.date_created, self.comp_id))
        connection.commit()
        print("Date Created Change Successful!")

class Assessments:

    def __init__(self, assessment_id, competency_type, name, date_created, active):
        self.assessment_id = assessment_id
        self.competency_type = competency_type
        self.name = name
        self.date_created = date_created
        self.actvie = active

    def edit_comp_id(self,asmt_id):
        while True:
            try:
                self.assessment_id = asmt_id
                new_comp_id = int(input("update Competency Type: "))
                self.competency_type = new_comp_id
                cursor.execute("UPDATE Assessments SET competency_type=? WHERE assessment_id=?",(self.competency_type, self.assessment_id))
                connection.commit()
                print("Competency Change Successful!")
                break
            except:
                print("\n*** value must be an integer ***\n")


    def edit_name(self, asmt_id):
        self.assessment_id = asmt_id
        new_name = input("update assessment name: ")
        self.name = new_name
        cursor.execute("UPDATE Assessments SET name=? WHERE assessment_id=?",(self.name, self.assessment_id))
        connection.commit()
        print("Name Change Successful!")

    def edit_date(self, asmt_id):
        self.assessment_id = asmt_id
        print("date format YYYY-MM-DD")
        new_date = input("update date created: ")
        self.date_created = new_date
        cursor.execute("UPDATE Assessments SET date_created=? WHERE comp_id=?",(self.date_created, self.comp_id))
        connection.commit()
        print("Date Created Change Successful!")


class Assessment_Results:

    def __init__(self, user_id, assessment_id, competency_score, date_taken, manager_id, active):
        self.user_id = user_id,
        self.assessment_id = assessment_id,
        self.competency_score = competency_score,
        self.date_taken = date_taken,
        self.manager_id = manager_id,
        self.active = active

    def edit_score(self, user_id, assessment_id, competency_score):
        self.user_id = user_id
        self.assessment_id = assessment_id
        self.competency_score = competency_score
        update_score = "UPDATE Assessment_Results SET competency_score=?  WHERE assessment_id=? AND user_id=?"
        update_values = (self.competency_score, self.assessment_id, self.user_id)
        cursor.execute(update_score, update_values)
        cursor.connection.commit()
        print("Score Change Successful!")

    def edit_date(self, user_id, assessment_id, date_taken):
        self.user_id = user_id
        self.assessment_id = assessment_id
        self.date_taken = date_taken
        update_date = "UPDATE Assessment_Results SET date_taken=?  WHERE assessment_id=? AND user_id=?"
        update_values = (self.date_taken, self.assessment_id, self.user_id)
        cursor.execute(update_date, update_values)
        cursor.connection.commit()
        print("Date Change Successful!")