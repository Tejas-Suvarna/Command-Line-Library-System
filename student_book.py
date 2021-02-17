import display_strings

dbcursor = None # Stores the database cursor
db = None # Stores the database connection

def issue_book_to_student(mycursor, mydb):
    
    # Initialize database variables
    dbcursor = mycursor 
    db = mydb

    student_id = input('Enter student ID: ')
    book_id = input('Enter book ID: ')

    # Checks if student has a pending book
    student_book_pending_query = "SELECT * FROM student_book_issue WHERE student_id=%s AND return_date IS NULL;"
    val = (student_id,)
    mycursor.execute(student_book_pending_query, val)
    print(mycursor.rowcount)
    if (mycursor.rowcount != 0):
        print('Student already has a book pending to be returned.')
        _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see
        return

    # Checks if book is available
    check_book_availability_query = "SELECT * FROM student_book_issue WHERE book_id=%s AND return_date IS NULL;"
    val = (book_id,)
    mycursor.execute(check_book_availability_query, val)
    print(mycursor.rowcount)
    if (mycursor.rowcount != 0):
        print('The book is taken by another user.')
        _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see
        return

    # Inserts details to database
    insert_student_book_issue_query = "INSERT INTO student_book_issue (student_id, book_id, issue_date) VALUES (%s, %s, CURDATE())"
    val = (student_id, book_id)
    mycursor.execute(insert_student_book_issue_query, val)
    print(mycursor.rowcount, "record inserted.")

    mydb.commit() # Saves all changes to database

    _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see


def returning_book(mycursor, mydb):

    # Initialize database variables
    dbcursor = mycursor 
    db = mydb

    student_id = input('Enter student ID: ')
    book_id = input('Enter book ID: ')

    # Check if student_id book_id pair exists
    student_book_id_query = "SELECT 1 FROM student_book_issue WHERE student_id=%s AND book_id=%s return_date IS NULL "
    val = (student_id, book_id)
    mycursor.execute(student_book_id_query, val)
    if (mycursor.rowcount != 0):
        print('Incorrect student ID or book ID. No such combination found.')
        return

    # Adds return date to the entry
    update_student_book_issue_query = "UPDATE student_book_issue SET return_date=CURDATE() WHERE student_id=%s AND book_id=%s return_date IS NULL;"
    val = (student_id, book_id)
    mycursor.execute(update_student_book_issue_query, val)
    print(mycursor.rowcount, "record inserted.")

    mydb.commit() # Saves all changes to database

    _ = input(display_strings.hit_enter_text) # This helps to persist the output for the user to see


