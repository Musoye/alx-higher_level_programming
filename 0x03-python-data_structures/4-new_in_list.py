#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """replace element in list without modifying the org list

    Args:
        my_list: the list
        idx: the index
        element: the element to modify

    Returns:
        new_list or org_list if idx < 0 or
        out of range
    """
    if (idx < 0 or idx > (len(my_list) - 1)):
        return (my_list.copy())
    new_list = my_list.copy()
    new_list[idx] = element
    return (new_list)
