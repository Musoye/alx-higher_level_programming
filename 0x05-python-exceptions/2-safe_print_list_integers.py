#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """safe print list integers

    Args:
        my_list: the list
        x: the number of element to print

   Return:
       the real number of integer printed
   """
   if my_list is None or x < 0:
       return (0)
   i = 0
   num = 0
   while i < x:
       try:
           print("{:d}".format(my_list[i]), end="")
           i += 1
           num += 1
       except ValueError:
           i += 1
       except IndexError:
           break
    return (num)
