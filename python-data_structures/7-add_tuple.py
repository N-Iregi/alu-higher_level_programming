#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_b = len(tuple_b)
    len_a = len(tuple_a)

    if len_a == 0:
        a1 = 0
        a2 = 0
    elif len_a == 1:
        a1 = tuple_a[0]
        a2 = 0
    elif len_a >= 2:
        a1 = tuple_a[0]
        a2 = tuple_a[1]

    if len_b == 0:
        b1 = 0
        b2 = 0
    elif len_b == 1:
        b1 = tuple_b[0]
        b2 = 0
    elif len_b >= 2:
        b1 = tuple_b[0]
        b2 = tuple_b[1]

    return (a1 + b1, a2 + b2)
