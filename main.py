import time # Used for the sleep function while exiting the program

import sql_connection
import display_strings # Contains string variables with multiline text

import student
import book


menu_choice_number = '' # The user choice in the main menu
exit_status = False # Flag indicating if user chose to exit

print(display_strings.welcome_message) # Displays the ASCII pattern text - "Library system"

# A continous while loop prompting user choice (number) for the main menu option
# The loop stops when user chooses to exit the program
while(exit_status == False):

    print(display_strings.main_menu_text) # Prints the main menu options text
    menu_choice_number = input('Enter your choice: ') # Stores the user choice

    if (menu_choice_number.strip() == '1'): 
        pass
        #func1()

    elif (menu_choice_number.strip() == '2'):
        pass
        #func2()

    elif (menu_choice_number.strip() == '3'):
        pass
        #func3()

    elif (menu_choice_number.strip() == '4'):
        pass
        #func4()

    elif (menu_choice_number.strip() == '5'):
        book.book_menu(sql_connection.mycursor, sql_connection.mydb)

    elif (menu_choice_number.strip() == '6'):
        student.student_menu(sql_connection.mycursor, sql_connection.mydb)

    elif (menu_choice_number.strip() == '7'):
        sql_connection.mydb.commit() # Saves all changes to database
        print('\nThank you. Have a great day :)\n')
        time.sleep(3) # This gives a 3 second lag and stops the program from directly exiting so that the user can see the thank you message
        exit_status = True

    elif (menu_choice_number.strip() == '8'):
        pass
        #func7()

    else :
        print('Invalid option selected.')
        print('Please enter a valid number from the options.')
        print('*********************************************')


exit(0) # Successfully completed the program
