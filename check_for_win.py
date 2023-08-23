
def check_matching_row(numbers_called,bingo_book,amount_to_win):
    """checks the called numbers against each row in the users bingo book and returns true if amount of rows to win in a box of 3 rows match"""

    winning_row_count = 0
    indices_to_skip = [0, 4, 8, 12,16,20]
    if len(numbers_called) >= 5*amount_to_win:

        for index, row in enumerate(bingo_book):
            if index in indices_to_skip or index == 0:   # skip row with id
                winning_row_count = 0 # set winning row count back to 0 after every 3 rows lines need to be matched in a box of 3
            else:
                numbers_in_mixed_list = [item for item in row if isinstance(item, int)]
                match = all(number in numbers_called for number in numbers_in_mixed_list)
                
                if match:
                    print(numbers_in_mixed_list)
                    winning_row_count += 1

            if amount_to_win == winning_row_count:
                return True
            

