import sql_connection # File used to establish connection with the SQL database
import display_strings  # Contains string variables with multiline text

import student
import book

exit_status = False # Flag indicating if user chose to exit

print(display_strings.welcome_message) # Displays the ASCII pattern text - "Library system"

# A continous while loop prompting user choice (number) for the main menu option
# The loop stops when user chooses to exit the program
while(exit_status == False):

    print(display_strings.main_menu_text) # Prints the main menu options text
    menu_choice_number = input('Enter your choice: ').strip() # Stores the user choice, strip() removes left and right spaces.

    if (menu_choice_number == '1'): 
        pass

    elif (menu_choice_number == '2'):
        pass

    elif (menu_choice_number == '3'):
        pass

    elif (menu_choice_number == '4'):
        pass

    elif (menu_choice_number == '5'):
        book.book_menu(sql_connection.mycursor, sql_connection.mydb) # We pass the database related variables to the book module

    elif (menu_choice_number == '6'):
        student.student_menu(sql_connection.mycursor, sql_connection.mydb) # We pass the database related variables to the student module

    elif (menu_choice_number == '7'):

        sql_connection.mydb.commit() # Saves all changes to database
        print('\nThank you. Have a great day :)\n')
        exit_status = True

    elif (menu_choice_number == '8'):
        pass

    else :
        print('Invalid option selected.')
        print('Please enter a valid number from the options.')
        print('*********************************************')


exit(0) # Successfully completed the program
