#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """print integer in list

    Args:
        my_list: the list to print from

    Returns:
        NULL
    """
    for i in my_list:
        print("{:d}".format(i))
