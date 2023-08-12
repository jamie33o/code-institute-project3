import random

def list_random_numbers(range_start, range_end, amount):
    # Create a range of numbers from 0 to 100
    number_range = range(range_start, range_end)  

    # Generate a list of unique random numbers
    unique_random_numbers = random.sample(number_range, amount)
    return unique_random_numbers