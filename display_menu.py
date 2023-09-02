from create_book import create_bingo_book,convert_string_to_list
from google_sheets import search_woksheet
from game_state import BingoGame
from number_generator import call_numbers
   
game_state = BingoGame()

def menu():

    print("****Option menu please choose an option*****")
    print("Option 1. Type 1 to get your bingo book")
    print("Option 2. Type 2 if you havent received you bingo book")
    print("Option 3. Type 3 to get the number's called during your game emailed to you")
    print("Option 5. Type 5 if you have your book and want to start the game")
    print("Option 6. Type 6 If your playing with friends or have more than one bingo book")
    print("Option 7. Quit")

    choice = input("Enter your choice: \n")

    if choice == "1":
        print("You selected Option 1")
        print("To get your bingo book please enter your email address")
        user_email = input("Enter your email: \n")

        print("if you want more than one then type the the amount of book's you want max 3")
        amount = int(input("Enter amount: \n"))
        
        print(f"The Email you entered is: {user_email}")
        try_again = input("Is this correct type Y for yes and N for No Y/N?")
        if try_again == "N" or try_again == "n":
            user_email = input("Please Enter your email again: \n")
        if amount > 1:
            for _ in range(amount):
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
            game_state.set_state("menu")
            game_state.play()
    elif choice == "2":
        print("You selected Option 2")
        print("We are sorry you didn't receive your book")

    elif choice == "3":
        print("You selected Option 3")
    elif choice == "4":
        print("You selected Option 4")
    elif choice == "5":
        print("You selected Option 5")            
        game_state.set_state("play")
        game_state.play()
    elif choice == "6":
        print("You selected Option 6")
    elif choice == "7":
        print("Goodbye!")
    else:
        print("Invalid choice")

def check_state():
    game_state.play()