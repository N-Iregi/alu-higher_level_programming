#!/usr/bin/python3
# 4-print_hexa.py

"""Print numbers 0 to 98 in decimal and hexadecimal."""
for number in range(0, 99):
    print("{:d} = 0x{:x}".format(number, number))
