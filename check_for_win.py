

def check_for_sinlge_line(numbers_called, bingo_book):
    """checks the called numbers against each row in the users bingo book and returns true if any single row matches"""
    if len(numbers_called) >= 5:
        for row in bingo_book:
            if all(number in numbers_called for number in row):
                return True
            else:
                return False
            
def check_for_two_lines(numbers_called, bingo_book):
     """checks the called numbers against each row in the users bingo book and returns true if two rows in a block of 3 match"""
     winning_row_count = 0
     winning_row_index = 0
     if len(numbers_called) >= 10:
        for index, row in enumerate(bingo_book):
            if all(number in numbers_called for number in row):
                winning_row_count += 1

                if winning_row_count == 2 and index - winning_row_index < 3:
                    return True
                
                winning_row_index = index

def check_for_fullhouse(numbers_called, bingo_book):
    """checks the called numbers against each row in the users bingo book and returns true if 3 rows in a row match"""
    winning_row_count = 0
    full_house_counter =0
    if len(numbers_called) >= 15:
        for row in bingo_book:
            if full_house_counter == 3:
                full_house_counter =0
            if all(number in numbers_called for number in row):
                winning_row_count += 1

                if winning_row_count == 3 and full_house_counter == 2:
                    print("win")
            full_house_counter += 1
                
            