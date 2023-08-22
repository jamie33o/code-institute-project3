import display_menu
from check_for_win import *
import number_generator
from google_sheets import search_woksheet
from create_book import convert_string_to_list
from google_sheets import search_woksheet
class BingoGame:
    def __init__(self):
        self.state = "menu"  # Initial state is "menu"

    def set_state(self, new_state):
        """sets the state the game is in"""
        self.state = new_state

    def play(self):
        """changes the functionality of the game based on the state e.g. looking for single line, double line, full house,break or play"""
        called_numbers = number_generator.get_callednumbers_list()
        user_bingo_book = []
        if self.state == "menu":
            display_menu.menu()
        elif self.state =="play":
            print("Please enter your book id to start the game")
            book_id = input("Book ID:\n")
            user_bingo_book = convert_string_to_list(search_woksheet(book_id))   
            self.set_state("calling_numbers")
            self.play()
        elif self.state == "calling_numbers":
            print("First we are looking for a single line")
            self.set_state("match_single_line")
            # start calling th numbers
            number_generator.call_numbers()
        elif self.state == "match_single_line":
            # check for single line
            if check_for_sinlge_line(called_numbers,user_bingo_book) or len(called_numbers) == 20:
                self.set_state("matched_single_line")
        elif self.state == "matched_single_line":
            # notify user they matched a single line and then pause calling numbers with input till user is ready
            print("Congratulations! You matched a line.")
            input("Press enter to continue: ")
            print("Now we are looking for two lines.")
            self.set_state("match_two_line")
        elif self.state == "match_two_line":
            # check for 2 lines
            if check_for_two_lines(called_numbers,user_bingo_book) or len(called_numbers) == 40:
                self.set_state("matched_two_lines")
        elif self.state == "matched_two_lines":
            # notify user they have matched two lines
            print("Congratulations! You have matched two lines.")
            input("Press enter to continue: ")
            print("Now we are looking for a Full House.")
            self.set_state("match_full_house")
        elif self.state == "match_full_house":
            # check for full house
            if check_for_fullhouse(called_numbers,user_bingo_book) or len(called_numbers) == 87:
                self.set_state("matched_full_house")
        elif self.state == "matched_full_house":
            # notify user has matched full house
            print("Congratulations! You have a full house.")
            input("Press enter to continue: ")
            self.set_state("end")
        elif self.state == "end":
            # notify user game is over
            print("Game over.")
            input("Press enter to go to menu: ")
            self.set_state("menu")
        elif self.state == "break":
            # lets the user take break after 50 numbers are called
            print("We will take a short brake now")
            # pause the number calls loop 
            input("Press enter to continue")
        
