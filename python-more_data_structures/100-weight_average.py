#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    total_weight_score = 0
    total_weight = 0

    for tup in my_list:
        total_weight_score += tup[0]*tup[1]
        total_weight += tup[1]

    average_weight = total_weight_score/total_weight
    return average_weight
