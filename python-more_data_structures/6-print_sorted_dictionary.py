#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_of_keys = sorted(a_dictionary)
    for i in range(len(list_of_keys)):
        print(f"{list_of_keys[i]}: {a_dictionary[list_of_keys[i]]}")
