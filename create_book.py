"""this module is for working with google sheets it has functions for creating the bingo book and searching the worksheets """

from email_sender import send_email
import random
from create_pdf import bingo_book_to_pdf
from google_sheets import generate_new_id,store_book_numbers


def create_bingo_book(email):
    """generates the rows of numbers for the bingo book then appends them to the bingo book sheet in google sheets 
    and then creates_pdf.py turns the numbers to pdf bingo book and email_sender send it as attachment to the user"""
    # creates a list of 90 numbers
    book_numbers = list(range(1,91))
    # list of lists of numbers for each row of the bingo book sheet and spaces
    book_rows_list = []
    store_book = []

    id = generate_new_id()
    
    # Sort the numbers into groups of 10 e.g. 1-10 ,11-20
    grouped_numbers = [book_numbers[i:i+10] for i in range(0, len(book_numbers), 10)]
    # Shuffle the numbers within each group 
    for group in grouped_numbers:
        random.shuffle(group)
    # Iterate through each index of the list of numbers and creates a new list that match the rows so 
    # first number will be between 1-10 second will be between 11-20 and so on so then first column numbers will be 1-10 second 11-20
    for index in range(10):
        row = [group[index] for group in grouped_numbers if index < len(group)]
        book_rows_list.append(row)

    # this block of code adds 4 spaces to to each row by randomly taking 
    # 4 numbers and creates a new list from the numbers that are replaced
    # then it is added back on to the old list this is so the columns of numbers stay in position e.g, 10's,20's,30's
    replacement_string = ""
    new_book_rows_list = []
    for row in book_rows_list:# loops trough each row and replaces number not in numbers to replace with an empty string
        numbers_to_replace = random.sample(row, 4)
        new_row = [replacement_string if num not in numbers_to_replace else num for num in row]
        new_book_rows_list.append(new_row)

        for index in range(len(row)):
            if row[index] in numbers_to_replace:
                row[index] = replacement_string  # Replace the original number with a space
        
    book_rows_list.extend([row for row in new_book_rows_list])

   # Remove the last two rows and store their content
    extra_rows = book_rows_list[-2:]  # Take the last two rows
    book_rows_list = book_rows_list[:-2]  # Remove the last two row

    # Distribute the numbers from extra rows to rows before them
    for extra_row in extra_rows:
        for index, num in enumerate(extra_row):
            if not isinstance(num,int):
                continue
            for group in reversed(book_rows_list):
                number_count = sum(isinstance(item, int) for item in group)
                if number_count == 5:
                    continue
                if group[index] == "":
                    group[index] = num
                    break
    # adds the book id to first row
    book_rows_list.insert(0,[id])

    # this adds the list of empty strings to match the merged rows after every 3 rows in the bingo book
    for index in [4, 8, 12,16,20]:      
        book_rows_list.insert(index,[""] * 7)

    store_book = turn_lists_to_string(book_rows_list)

    # Insert book to google sheets row
    store_book_numbers(store_book)

    # adds the name and book id to first row
    book_rows_list[0][0] = f"Mega Bingo\nBook ID: {id}"

    # crete pdf from the numbers
    pdf_buffer = bingo_book_to_pdf(book_rows_list)
    #send the pdf to user in email
    send_email(email,"bingobook.pdf", pdf_buffer)

       
def convert_string_to_list(input_list):
# Reverting the string-represented rows back to lists
    output_list = []

    for string_row in input_list:
        split_row = string_row.split(',')  # Split the string into individual elements
        row_as_list = list(map(lambda element: element if element == "" else int(element), split_row)) 

        output_list.append(row_as_list)  # Append the list to the book_rows_list
    return output_list



def turn_lists_to_string(input_list):
    output_list = []
    for row in input_list:
            joined_row = ','.join(map(str, row))  # turn each list in the list of lists to a string
            output_list.append(joined_row)  # Append the string to the store_book list
    return output_list