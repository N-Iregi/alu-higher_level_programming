#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    prevvalue = 0
    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    if (not isinstance(roman_string, str)) or if roman_string == None:
        return 0

    for c in roman_string:
        if c not in value:
            return 0
        else:
            currvalue = value[c]

        if currvalue > prevvalue:
            sum += currvalue - 2*prevvalue
        else:
            sum += currvalue
        prevvalue = currvalue

    return sum
