#!/bin/python
from math import sqrt
from xmath import to_index

# from xmath import to_index
def print_board(b):
    width = int(sqrt(len(b)))
    height = width
    if (width * height != len(b)):
        print ("Error! Invalid Board")
    print ("Length: ", len(b), width, height)
    for y in range(0, height):
        print ("\n")
        for x in range(0, width):
            print(b[to_index(x, y, width)], end=" ")
    print ("\n")



if __name__ == "__main__":
    print_board("163805070008040065005007008450082039301000040700000000839050000604200590000093081")




