#!/usr/bin/python3

from rules import *

base = 9
# output_filename = input("Enter Filename:")
output_filename = "cnf"
write_string = ""
with open(output_filename, mode="w") as f:
    # write_string += every_cell_has_number(base)
    write_string += rule3(base)
    write_string += rule4(base)
    write_string += rule5(base)
    f.write(write_string)
