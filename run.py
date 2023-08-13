import time
from number_generator import list_random_numbers
from email_sender import send_email



delay_seconds = 2  # Set the delay time in seconds
repeat_count = 5   # Sets the number of times to repeat the function call

# list of numbers to be called
number_list = list_random_numbers(1,91,5)

# list of the numbers that have been called
called_numbers_list = []

def main():
    """ main fuction calls the number calls function in a for loop until all the numbers are called"""
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

