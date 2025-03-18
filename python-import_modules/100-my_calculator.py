#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    arg_list = sys.argv[1:]
    len_list = len(arg_list)

    if len_list != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(arg_list[0])
    operator = arg_list[1]
    b = int(arg_list[2])
    if arg_list[1] == '+':
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
    elif arg_list[1] == '-':
        print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
    elif arg_list[1] == '*':
        print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
    elif arg_list[1] == '/':
        print("{} {} {} = {}".format(a, operator, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
