import display_strings
student_menu_choice_number = ''
# Stores the database cursor
dbcursor = None

def is_student_data_correct(student_data):

    (student_name, student_class, student_dob) = student_data # Unpack tuple student data

    # Checks the length of the student full_name
    if(len(student_name) > 40 or len(student_name) == 0):
        print('Please enter a name with 40 characters. ')
        return False

    if(len(student_class) > 2 or len(student_class) == 0):
        print('Please enter a valid class')
        return False

    if(not student_class.isnumeric()):
        print('Please enter a valid class number')
        return False

    if(len(student_dob) != 10):
        print('Please enter data in the format (dd-mm-yyyy)')
        return False
    
    if(int(student_class) > 12 or int(student_class) == 0):
        print('Enter a class that is from 1 to 12.')
        return False

    return True # The data is correct


# Displays student menu
def student_menu(mycursor):

    dbcursor = mycursor # Initialize database cursor

    print(display_strings.student_menu_text) # Displays student menu
    student_menu_choice_number = input('Enter your choice: ')
    
    if (student_menu_choice_number.strip() == '1'): 
        create_student(dbcursor) # Function to inserts a new student and the details into the database
    elif (student_menu_choice_number.strip() == '2'):
        pass
        #func2()
    else:
        print('Invalid option selected.\n')


# This function inserts a new student and the details into the database
def create_student(mycursor): # The function receives the database cursor parameter

    # Accepts student details from user
    print('Student details\n---------------')
    student_name = input('Enter the student full name (40 characters max): ')
    student_class = input('Enter the class of the student (1,2,...,10): ')
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

    _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see

