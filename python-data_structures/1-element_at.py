#!/usr/bin/python3
def element_at(my_list, idx):
    '''retrieves an element from a list like in C'''
    if idx < 0:
        return none
    elif idx > len(my_list):
        return none
    else:
        return my_list[idx]
