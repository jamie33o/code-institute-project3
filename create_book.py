import gspread
from google.oauth2.service_account import Credentials
from number_generator import list_random_numbers
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("mega-bingo")

bingo_book_sheet = SHEET.worksheet("bingo-book")

numbers_called_sheet = SHEET.worksheet("numbers-called")

def create_bingo_book():
    book_numbers = list(range(1,91))
    elements_at_index = []

    # Sort the numbers into groups of 10 
    grouped_numbers = [book_numbers[i:i+10] for i in range(0, len(book_numbers), 10)]
    # Shuffle the numbers within each group
    for group in grouped_numbers:
        group.append(["","","",""])
        random.shuffle(group)
    # Iterate through each index of the groups
    for index in range(14):
        elements_at_index.append([group[index] for group in grouped_numbers])

    # Insert data into columns
    for i in range(1, 19):
        if i == 4 or i == 8 or i == 12 or i == 16:
            empty_row = ["","",""]
            bingo_book_sheet.append_row(empty_row)

        data_to_insert = []
        random_spaces = []

      
            random_integer = random.randint(1, 10)
            
            if random_integer >= 5 and len(random_spaces) != 4:
                data_to_insert.append(" ")
                random_spaces.append(" ")
            elif book_numbers[j] in range(j * 10, j*10 + 10):
                data_to_insert.append(book_numbers[j])
                book_numbers.pop(j)
            print(book_numbers[j])
            
            if len(data_to_insert) == 8:
                bingo_book_sheet.append_row(data_to_insert)
                break

    




        