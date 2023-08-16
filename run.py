import time
from number_generator import list_random_numbers
from create_book import create_bingo_book,convert_string_to_list
from google_sheets import search_woksheet

delay_seconds = 2  # Set the delay time in seconds
repeat_count = 5   # Sets the number of times to repeat the function call

# list of numbers to be called
number_list = list_random_numbers(1,91,5)

# list of the numbers that have been called
called_numbers_list = []

def main():
    """ main fuction calls the number calls function in a for loop until all the numbers are called"""

    print("Welcome to MEGA BINGO option menu please choose an option")
    print("Option 1. Type 1 to get your bingo book")
    print("Option 2. Type 2 if you havent received you bingo book")
    print("Option 3. Type 3 to get the number's called during your game emailed to you")
    print("Option 5. Type 5 if you have your book and want to start the game")
    print("Option 6. Type 6 If your playing with friends or have more than one bingo book")
    print("Option 7. Quit")
    
    choice = input("Enter your choice: \n")
    
    if choice == "1":
        print("You selected Option 1")
        print("To get your bingo book please enter your email address \n if you want more than one then type the the amount of book's you want max 3 \n")
        amount = int(input("Enter amount: \n"))
        user_email = input("Enter your email: \n")
        print(f"Email you entered is: {user_email}")
        try_again = input("Is this correct type Y for yes and N for No Y/N?")
        if try_again == "N" or try_again == "n":
            user_email = input("Please Enter your email again: \n")
        if amount > 0:
            for _ in amount:
                print("If you are getting a book for a friend and want to send it to there email enter there email otherwise ")
                next_email = input("Enter friend's email: \n")
                if next_email != "":
                    user_email = next_email
                    print(f"Email you entered is: {user_email}")
                    try_again = input("Is this correct type Y for yes and N for No Y/N?")
                    if try_again == "N" or try_again == "n":
                        user_email = input("Please Enter your email again: \n")
                create_bingo_book(user_email)
        else:
            create_bingo_book(user_email)
            print("Please check your email to get your bingo book")
                
    elif choice == "2":
        print("You selected Option 2")
        print("We are sorry you didn't receive your book")

    elif choice == "3":
        print("You selected Option 3")
    elif choice == "4":
        print("You selected Option 4")
    elif choice == "5":
        print("You selected Option 5")
        print("Please enter your book id to start the game")
        book_id = input("Book ID: /n")
        user_bingo_book = convert_string_to_list(search_woksheet(book_id))
        start_game(user_bingo_book)
    elif choice == "6":
        print("You selected Option 6")
    elif choice == "7":
        print("Goodbye!")
    else:
        print("Invalid choice")
    
    #create_bingo_book("giftsforyou83@gmail.com")
    

def start_game(user_bingo_book):
    print("Welcome to MEGA BINGO the game is about to start get ready!!!")
    print("The first number is: ")
    for number in number_list :
        number_calls(number)  # Call the number calls function
        time.sleep(delay_seconds)  # Delay for the specified time
        called_numbers_list.append(number) # appends the numbers called to the list 



        for row in user_bingo_book:
            if 

def number_calls(number_called):
    """prints the next number to the terminal"""
    print(number_called)
    if len(called_numbers_list) == 100:
        print("Game over!!")    
    elif len(called_numbers_list) :
        print("Next we have: ")


main()

