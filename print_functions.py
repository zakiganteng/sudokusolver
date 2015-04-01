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
            print ()
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
    b_original = b_original.replace("\n", "") # Do the cleaning thing
    b_original = b_original.replace("\t", "")
    b_original = b_original.replace(" ", "")
    b_original = re.sub(" \n", "", b_original)
    b_original = re.sub("[^0-9a-zA-Z]", "0", b_original)
    ret_list = []
    for char in b_original:
        ret_list.append(int(char, 32))
    return ret_list

if __name__ == "__main__":
    b = "e4...a.....519d8\
        .2.....b.dec..5.\
        .8..76....b...3c\
        .9.a...87..3..f.\
        9...e...37fd.c.1\
        ...f...a.e5..d..\
        ...c...fa.....7.\
        d7b....9..c..4.0\
        ..84d9.c....ab.3\
        ...9.5.768......\
        ..d...4..a......\
        ..f26.b0......e.\
        .e.7c35..4.1d..6\
        .fa.....2.6..1..\
        .......6....0e8f\
        8.c6a..........9"
    print_board(b)
    print()
    print_board(convert_board(b))




