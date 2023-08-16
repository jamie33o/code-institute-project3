

def check_for_sinlge_line(numbers_called, bingo_book):
    if len(numbers_called) >= 5:
        for row in bingo_book:
            if all(number in numbers_called for number in row):
                return True
            else:
                return False