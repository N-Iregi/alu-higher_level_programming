#!/usr/bin/python3
# 6-print_comb3.py
"""Print all possible different combinations of two digits in ascending order.
The two digits must be different - 01 and 10 are considered identical.
The two digits must be separated by a comma followed by a space."""
for i in range(10):
    for j in range(i + 1, 10):
        print("{}{}".format(i, j), end=', ' if i != 8 or j != 9 else "\n")
