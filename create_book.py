import gspread
from google.oauth2.service_account import Credentials
from number_generator import list_random_numbers
import random

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
bingo_book_sheet = SHEET.worksheet("bingo-book")
# gets the numbers called sheet
numbers_called_sheet = SHEET.worksheet("numbers-called")

def create_bingo_book():
    """generates the numbers for the bingo book then appends them to the bingo book sheet in google sheets"""
    # creates a list of 90 numbers
    book_numbers = list(range(1,91))
    # list of lists of numbers for each row of the bingo book sheet and spaces
    elements_at_index = []

    # Sort the numbers into groups of 10 e.g. 1-10 ,11-20
    grouped_numbers = [book_numbers[i:i+10] for i in range(0, len(book_numbers), 10)]

    # Shuffle the numbers within each group and adds 8 spaces to each group before shuffling
    for group in grouped_numbers:
        empty_strings = [""] * 8
        group.extend(empty_strings)
        random.shuffle(group)

    # Iterate through each index of the list of numbers and creates a new list that match the rows so 
    # first number will be between 1-10 second will be between 11-20 and so on so then first column numbers will be 1-10 second 11-20
    for index in range(18):
       elements_at_index.append([group[index] for group in grouped_numbers])

    # this adds the list of empty strings to match the empty space after every 3 rows in the bingo book
    for index in [3, 7, 11,15,19]:      
        elements_at_index.insert(index,[""] * 7 )
        
    # this appends the rows to the bingo book in google sheets
    bingo_book_sheet.append_rows(elements_at_index)

       
    




        