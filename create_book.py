"""this module is for working with google sheets it has functions for creating the bingo book and searching the worksheets """
import gspread
from google.oauth2.service_account import Credentials
from email_sender import send_email
import random
from create_pdf import bingo_book_to_pdf
# sets what im authorized to use with google cloud services
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# get the credentials from the config var
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# open the google sheets for mega bingo
SHEET = GSPREAD_CLIENT.open("mega-bingo")

# get the bingo book sheet
bingo_book_sheet = SHEET.worksheet("bingo-books")
# gets the numbers called sheet
numbers_called_sheet = SHEET.worksheet("numbers-called")

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
    bingo_book_sheet.insert_row(store_book)

    # adds the name and book id to first row
    book_rows_list[0][0] = f"Mega Bingo\nBook ID: {id}"


    pdf_buffer = bingo_book_to_pdf(book_rows_list)
    send_email(email,"bingobook.pdf", pdf_buffer)

       
def generate_new_id():
    """generates a new id by searching the ids in google sheets and finding the last id and adding one to it"""
    all_new_ids = bingo_book_sheet.col_values(1)
    last_id = 0
    new_id = 1
    for id in all_new_ids:
        id =  int(id)  
        if id > last_id:
            new_id = id + 1
        last_id = id
    return new_id


def search_woksheet():
    
    search_number = 123

    
    matching_cells = bingo_book_sheet.findall(str(search_number), in_column=1)

    for cell in matching_cells:
        print("Found at:", cell.address, "book:",bingo_book_sheet.row_values(cell.row))