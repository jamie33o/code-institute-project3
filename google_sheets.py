import gspread
from google.oauth2.service_account import Credentials

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


def store_book_numbers(book):
     # Insert book to google sheets row
    bingo_book_sheet.insert_row(book)

def store_numbers_called():
    numbers_called_sheet.insert_rows(numbers_called_sheet)

def search_woksheet(book_id):
    """search the google sheet by id's in the first column"""
    matching_cell = bingo_book_sheet.find(str(book_id), in_column=1)
    found_bingo_book = bingo_book_sheet.row_values(matching_cell.row)
    return found_bingo_book


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