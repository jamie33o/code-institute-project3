"""this module is for working with google sheets it has functions for creating the bingo book and searching the worksheets """

from email_sender import send_email
import random
from create_pdf import bingo_book_to_pdf
from google_sheets import generate_new_id,store_book_numbers


def create_bingo_book(email):
    """generates the numbers for the bingo book then appends them to the bingo book sheet in google sheets 
    and then creates_pdf.py turns the numbers to pdf bingo book and email_sender send it as attachment to the user"""
    # creates a list of 90 numbers
    book_numbers = list(range(1,91))
    # list of lists of numbers for each row of the bingo book sheet and spaces
    book_rows_list = []
    store_book = []

    id = generate_new_id()
    
    # Sort the numbers into groups of 10 e.g. 1-10 ,11-20
    grouped_numbers = [book_numbers[i:i+10] for i in range(0, len(book_numbers), 10)]

    # Shuffle the numbers within each group and adds 8 spaces to each group before shuffling
    for group in grouped_numbers:
        empty_strings = [""] * 8
        group.extend(empty_strings)
        random.shuffle(group)
    
    # adds the book id to first row
    book_rows_list.insert(0,[id])

    # Iterate through each index of the list of numbers and creates a new list that match the rows so 
    # first number will be between 1-10 second will be between 11-20 and so on so then first column numbers will be 1-10 second 11-20
    for index in range(18):
       book_rows_list.append([group[index] for group in grouped_numbers])

    # this adds the list of empty strings to match the merged rows after every 3 rows in the bingo book
    for index in [4, 8, 12,16,20]:      
        book_rows_list.insert(index,[""] * 7)

    for row in book_rows_list:
        joined_row = ','.join(map(str, row))  # turn each list in the list of lists to a string
        store_book.append(joined_row)  # Append the string to the store_book list

    # Insert book to google sheets row
    store_book_numbers(store_book)

    # adds the name and book id to first row
    book_rows_list[0][0] = f"Mega Bingo\nBook ID: {id}"

    # crete pdf from the numbers
    pdf_buffer = bingo_book_to_pdf(book_rows_list)
    #send the pdf to user in email
    send_email(email,"bingobook.pdf", pdf_buffer)

       



