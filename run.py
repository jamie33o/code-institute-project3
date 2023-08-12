# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import time
from number_generator import list_random_numbers
delay_seconds = 2  # Set the delay time in seconds
repeat_count = 5   # Sets the number of times to repeat the function call

number_list = list_random_numbers(1,91,90)

def main():
    print("Welcome to MEGA BINGO the game is about to start get ready!!!")
    print("The first number is: ")
    for i in number_list :
        number_calls(number_list[i])  # Call the function
        time.sleep(delay_seconds)  # Delay for the specified time



def number_calls(number_called):
    print(number_called)
    print("Next we have: ")


    
main()
