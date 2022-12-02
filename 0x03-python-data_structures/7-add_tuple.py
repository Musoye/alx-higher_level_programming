#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """add two tuple and returna tuple

    Args:
        tuple_a: the first tuple
        tuple_b: the second tuple

    Returns:
        the resulr of sum of two first  elment of
        each tuple
    """
    a = tuple_a[0] if tuple_a[0] != '' else 0
    if len(tuple_a) == 1:
        b = 0
    else:
        b = tuple_a[1] if tuple_a[1] != '' else 0
    if len(tuple_b) <= 1:
        d = 0
    else:
        d = tuple_b[1] if tuple_b[1] != '' else 0
    if len(tuple_b) <= 0:
        c = 0
        d = 0
    else:
        c = tuple_b[0] if tuple_b[0] != '' else 0
    result = a + c, b + d
    return (result)
