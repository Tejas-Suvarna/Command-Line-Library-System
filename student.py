import display_strings

dbcursor = None # Stores the database cursor
db = None # Stores the database connection

# Function checks if entered student data is valid or not
def is_student_data_correct(student_data):

    (student_name, student_class, student_dob) = student_data # Unpack tuple student data

    # Checks the length of the student full_name
    if (len(student_name) > 40 or len(student_name) == 0):
        print('Please enter a name with 40 characters. ')
        return False

    if (len(student_class) > 2 or len(student_class) == 0):
        print('Please enter a valid class')
        return False

    if (not student_class.isnumeric()):
        print('Please enter a valid class number')
        return False

    if (len(student_dob) != 10):
        print('Please enter data in the format (dd-mm-yyyy)')
        return False
    
    if (int(student_class) > 12 or int(student_class) == 0):
        print('Enter a class that is from 1 to 12.')
        return False

    return True # The data is correct


# Displays student menu
def student_menu(mycursor, mydb):

    dbcursor = mycursor # Initialize database cursor
    db = mydb

    print(display_strings.student_menu_text) # Displays student menu
    student_menu_choice_number = input('Enter your choice: ')
    
    if (student_menu_choice_number.strip() == '1'): 
        create_student(dbcursor, db) # Function to inserts a new student and the details into the database

    elif (student_menu_choice_number.strip() == '2'):
        delete_student(dbcursor, db) # Function to delete student of a particular student ID from the database

    elif (student_menu_choice_number.strip() == '3'):
        display_all_students(dbcursor, db) # Function to display all students from database

    elif (student_menu_choice_number.strip() == '4'):
        return

    else:
        print('Invalid option selected.\n')


# This function inserts a new student and the details into the database
def create_student(mycursor, mydb): # The function receives the database cursor parameter

    # Accepts student details from user
    print('Student details\n---------------')
    student_name = input('Enter the student full name (40 characters max): ')
    student_class = input('Enter the class of the student (1,2,...,10,11,12): ')
    student_dob = input('Enter the date of birth of the student (dd-mm-yyyy): ')

    # Check student data
    student_data = (student_name.strip(), student_class.strip(), student_dob.strip()) # Pack the student data into a tuple

    if not is_student_data_correct(student_data):
        print('Check the data you\'ve entered.')
        _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see
        return
        
    # Inserts details to database
    insert_student_query = "INSERT INTO student (full_name, class, dob) VALUES (%s, %s, %s)"
    val = (student_name.strip(), student_class.strip(), student_dob.strip())
    mycursor.execute(insert_student_query, val)
    print(mycursor.rowcount, "record inserted.")

    # Displays the new student ID
    latest_student_id_query = "SELECT MAX(student_id) FROM student;"
    mycursor.execute(latest_student_id_query)
    student_id_result = mycursor.fetchone()
    print('The new student ID is', student_id_result[0])

    mydb.commit() # Saves all changes to database

    _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see

def delete_student(mycursor, mydb):

    all_student_ids = []

    # Accepts student ID from user whose entry needs to be deleted
    student_id_to_delete = input('Enter the ID of student to be deleted: ')

    # Fetches all student IDs for validation
    get_student_ids_query = 'SELECT student_id FROM student;'
    mycursor.execute(get_student_ids_query)
    myresult = mycursor.fetchall()

    # Stores all student IDs in a list
    for x in myresult:
        all_student_ids.append(x[0])


    # Validation of the user entered student ID
    if (not student_id_to_delete.isnumeric()):
        print('Please enter a numeric student ID.')
        _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see
        return
    
    if (int(student_id_to_delete) not in all_student_ids):
        print('Entered student ID doesn\'t exist in the database.')
        _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see
        return

    # Deleting the student with a student ID entered by user
    delete_student_query = 'DELETE FROM student WHERE student_id = ' + student_id_to_delete
    mycursor.execute(delete_student_query)
    print(mycursor.rowcount, "record(s) deleted")

    mydb.commit() # Saves all changes to database

    _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see

# Displays all students from database
def display_all_students(mycursor, mydb):

    # Displays all student data
    latest_student_id_query = "SELECT student_id, full_name, class, dob FROM student;"
    mycursor.execute(latest_student_id_query)
    all_students = mycursor.fetchall()

    print(display_strings.student_details_header, end='') # Displays a nice student details heading. We add an end='' since the student_details_header already has a new line

    for student in all_students:
        
        # Extracting student data from tuple
        student_id = student[0]
        student_full_name = student[1]
        student_class = student[2]
        student_dob = student[3]

        # Prints row of student detail in an organized row
        print('| %4s | %29s | %5s | %11s |' % (student_id, student_full_name, student_class, student_dob))

    print(display_strings.student_details_footer) # Displays a student details footer

    _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see