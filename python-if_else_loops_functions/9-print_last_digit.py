#!/usr/bin/python3
# 9-print_last_digit.py


def print_last_digit(number):
    """Print the last digit of a number and return it."""
    num = abs(number) % 10
    print(num, end='')
    return num
