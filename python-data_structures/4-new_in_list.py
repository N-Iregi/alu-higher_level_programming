#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listcopy = my_list[:]

    if idx < 0:
        return listcopy
    elif idx > len(my_list):
        return listcopy
    else:
        listcopy[idx] = element
        return listcopy
