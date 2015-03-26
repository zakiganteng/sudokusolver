#!/usr/bin/python3

from rules import *
from print_functions import print_board, convert_board
from rule0 import rule0

input_filename = input("Input Filename: ")
base = 9
with open(input_filename, "r") as inf:
    board = convert_board(inf.read())
output_filename = "cnf"
write_string = ""
print (board)

# rule0(base, board)
with open(output_filename, mode="w") as f:
    write_string += rule0(base, board)
    # write_string += rule1(base)
    # write_string += rule2(base)
    # write_string += rule3(base)
    # write_string += rule4(base)
    # write_string += rule5(base)
    f.write(write_string)
