#!/bin/python
from math import sqrt
from xmath import to_index
import re

def print_board(b):
    width = int(sqrt(len(b)))
    height = width
    sub_width = int(sqrt(width))
    print (sub_width)
    if (width * height != len(b)):
        print ("Error! Invalid Board")
    for y in range(0, height):
        if y % sub_width == 0 and y > 0:
            print ("\n", end="")
            for x in range(0, width * 2):
                if (x/2) % sub_width == 0 and x > 0:
                    print ("-+", end = "")
                else:
                    print ("-", end="")
        print ("\n", end="")

        for x in range(0, width):
            if x % sub_width == 0 and x > 0:
                print ("| ", end = "")
            print(b[to_index(x, y, width)], end=" ")

def output_board(b):
    width = int(sqrt(len(b)))
    height = width
    ret_str = ""
    if (width * height != len(b)):
        print ("Error! Invalid Board")
        return ""
    for y in range(0, height):
        for x in range(0, width):
            ret_str += b[to_index(x, y, width)] + " "
        ret_str += "\n"
    return ret_str


def convert_board(b_original):
    b_original = b_original.replace("\n", "")
    b_original = b_original.replace("\t", "")
    b_original = b_original.replace(" ", "")
    b_original = re.sub(" \n", "", b_original)
    return re.sub("[^0-9]", "0", b_original)


if __name__ == "__main__":
    b = "1638.5.7..*8040065005007008450082039301000040700000000839050000604200590000093081"
    print_board(b)
    print()
    print_board(convert_board(b))




