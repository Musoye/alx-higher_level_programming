#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """replace the elment in a list

    Args:
        my_list: the list
        idx: the index
        element: the element to put at that index

    Returns:
        the new list with modified element if found
        else return null if idx < 0 or > list
    """
    if (idx < 0 or idx > (len(my_list) - 1)):
        return (my_list)
    my_list[idx] = element
    return (my_list)
