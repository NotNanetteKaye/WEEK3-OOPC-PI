# Happy Numbers: https://en.wikipedia.org/wiki/Happy_number
# A happy number is a number defined by the following process: starting with any positive integer, 
# replace the number by the sum of the squares of its digits, 
# and repeat the process until the number equals 1. An example of a happy number is 19
# Write a method that determines if a number is happy or sad.

import math

def happy_numbers(positive_integer):
    seen = set()
    happy_number = 1
    square_sum = 0
    while positive_integer not in seen:
        seen.add(positive_integer)
        while positive_integer > 0:
            square_sum += (positive_integer%10)*(positive_integer%10)
            positive_integer = math.floor(positive_integer/10)
        if square_sum == happy_number:
            print(f'{positive_integer} is a happy number!')
        else:
            positive_integer = square_sum
    print(f'{positive_integer} is a sad number')
    return False

positive_integer = int(input('\nPlease enter a positive number: '))
happy_numbers(positive_integer)