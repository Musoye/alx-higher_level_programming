#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """list division  length

    Args:
        my_list_1: the first list
        my_list_2: the seond list
        list_length: the list length they want us to talk about

    Returns:
        return the new list
    """
    new_list = []
    for i in (0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            result = 0
            print("wrong type")
            continue
        except ZeroDivisionError:
            result = 0
            print("division by 0")
            continue
        except IndexError:
            result = 0
            print("out of range")
            continue
        finally:
            new_list.append(result)
    return (new_list)
