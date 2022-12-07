#!/usr/bin/python3
def number_keys(a_dictionary):
    """return the number of keys

    Args:
        a_dictionary: the dictionary

    Returns:
        the numbers of the key
    """
    if a_dictionary == {}:
        return  (0)
    return (len(list(a_dictionary)))
