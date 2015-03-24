#!/bin/python
from math import sqrt
from xmath import to_index
import re

# from xmath import to_index
def print_board(b):
    width = int(sqrt(len(b)))
    height = width
    if (width * height != len(b)):
        print ("Error! Invalid Board")
    for y in range(0, height):
        for x in range(0, width):
            print(b[to_index(x, y, width)], end=" ")
        print ("\n")

def convert_board(b_original):
    b_original = b_original.strip()
    return re.sub("[^0-9]", "0", b_original)




if __name__ == "__main__":
    b = "1638.5.7..*8040065005007008450082039301000040700000000839050000604200590000093081"
    print_board(b)
    print()
    print_board(convert_board(b))




