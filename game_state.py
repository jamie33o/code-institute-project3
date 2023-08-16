

class BingoGame:
    def __init__(self):
        self.state = "menu"  # Initial state is "menu"

    def set_state(self, new_state):
        self.state = new_state

    def play(self):
        print("Current state:", self.state)
        
        if self.state == "menu":
            menu()
        elif self.state == "match_single_line":
            print("Now we are looking for a single line")

            self.set_state("match_two_line")

        elif self.state == "matched_single_line":
            print("Congratulations! You matched a line.")

            self.set_state("match_two_line")

        elif self.state == "match_two_line":
            print("Now we are looking for two lines.")


            self.set_state("matched_two_lines")
        elif self.state == "matched_two_lines":
            print("Congratulations! You have matched two lines.")
            self.set_state("match_full_house")

        elif self.state == "match_full_house":
            print("Now we are looking for a full house")


            self.set_state("matched_full_house")
        elif self.state == "matched_full_house":
            print("Congratulations! You have a full house.")

            self.set_state("end")
        elif self.state == "end":
            print("Game over.")
        elif self.state == "break":
        


