import time
from number_generator import list_random_numbers
from email_sender import send_email
import gspread
from google.oauth2.service_account import Credentials

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



delay_seconds = 2  # Set the delay time in seconds
repeat_count = 5   # Sets the number of times to repeat the function call

# list of numbers to be called
number_list = list_random_numbers(1,91,5)

# list of the numbers that have been called
called_numbers_list = []

def main():
    """ main fuction calls the number calls function in a for loop until all the numbers are called"""
    send_email()
    print("Welcome to MEGA BINGO the game is about to start get ready!!!")
    print("The first number is: ")
    for number in number_list :
        number_calls(number)  # Call the function
        time.sleep(delay_seconds)  # Delay for the specified time
        called_numbers_list.append(number)

def number_calls(number_called):
    """prints the next number to the terminal"""
    print(number_called)
    if len(called_numbers_list) == 4:
        print("Game over!!")    
    else:
        print("Next we have: ")



main()

