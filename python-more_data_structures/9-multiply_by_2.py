#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict.copy(a_dictionary)
    for i in new_dict:
        new_dict[i] = new_dict[i]*2
    return new_dict
