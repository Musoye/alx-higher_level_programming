#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        str[i] = chr(ord(str[i])-32)
    return (str)
