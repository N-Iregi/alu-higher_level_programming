#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    len_list = len(sys.argv)

    if len_list != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    try:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
    except ValueError:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = sys.argv[2]
    if operator == '+':
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
    elif operator == '-':
        print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
    elif operator == '*':
        print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
    elif operator == '/':
        print("{} {} {} = {}".format(a, operator, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
