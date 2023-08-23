import random
import time
import display_menu

delay_seconds = 2  # Set the delay time in seconds

def list_random_numbers(range_start, range_end, amount):
    # Create a range of numbers from 0 to 100
    number_range = range(range_start, range_end)  

    # Generate a list of unique random numbers
    unique_random_numbers = random.sample(number_range, amount)
    return unique_random_numbers

# list of numbers to be called
number_list = list_random_numbers(1,91,90)

# list of the numbers that have been called
called_numbers_list = []
def call_numbers():
    print("The game is about to start get ready!!!")
    print("The first number is: ")
    
    for number in number_list :
        print(number)
        print("Next we have: ")
        called_numbers_list.append(number) # appends the numbers called to the list
        display_menu.check_state()
        time.sleep(delay_seconds)  # Delay for the specified time            
            
def get_callednumbers_list():
    return called_numbers_list