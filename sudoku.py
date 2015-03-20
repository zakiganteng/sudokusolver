#!/usr/bin/python3

from rules import rule4, every_cell_has_number

base = 9
output_filename = input("Enter Filename:")
with open(output_filename, mode="w") as f:
    write_string = every_cell_has_number(base)
    write_string += rule4(base)
    f.write(write_string)
