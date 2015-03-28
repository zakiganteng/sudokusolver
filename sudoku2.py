#!/usr/bin/python3

# -------------------------------------------------------------------
# sudoku2.py
#
# sudoku2
#
# Evan Wilde            <etcwilde@uvic.ca>
# Sebastien Guillemot
# Shayla Redlin
# Laura Grondahl
#
# Mar 27 2015
#
# -------------------------------------------------------------------

# Yes, I am aware that this file is ugly, but it is closer to working than we
# were before...
# Doesn't check the within the box -- rule 5
# Resulting board is transposed. we need to flip it back
# Shayla and I were running into this a little before

from print_functions import print_board, convert_board, output_board
from math import sqrt
from xmath import to_base, from_base, to_index
from subprocess import call

import argparse
parser = argparse.ArgumentParser(description="Solve a sudoku puzzle")
parser.add_argument('inputfile', type=argparse.FileType('r'))
parser.add_argument('outputfile', type=argparse.FileType('w'))
parser.add_argument('minisatexe')
parser.add_argument('tmp_out', type=argparse.FileType('w'))
parser.add_argument('tmp_in')

args = parser.parse_args()
# print(args.inputfile.read())

board = convert_board(args.inputfile.read())
print ("Input board: ")
print_board(board)


# -----------------------------------------
# CONVERT TO DIMACS
# -----------------------------------------


# These are the same, but in case for some reason they are not, I want them
# here
size = int(sqrt(len(board)))
numbers = size

# The number of individual possibilities
variables = size * size * numbers
dimacs_output = ""
clauses = 0

print ("Variables: ", variables)


print ("Board requirements: ")
dimacs_output += "c the board requirements\n"
for j in range(0, size):
    for i in range(0, size):
        value = int(board[to_index(i, j, size)])
        if value != 0:
            print (value)
            value = to_base(i + 1, j + 1, value, size)
            clauses += 1
            dimacs_output += "{0} 0\n".format(value)



dimacs_output += "c at least one number per entry\n"
for i in range(1, size + 1):
    for j in range (1, size + 1):
        for k in range ( 1, numbers + 1):
            dimacs_output += "{0} ".format(to_base(i, j, k, size))
        dimacs_output += "0\n"
        clauses += 1

dimacs_output += "c Row constraint\n"
for i in range(1, size + 1):
    for j in range(1, size + 1):
        for k in range(1, numbers + 1):
            for j_s in range(j + 1, numbers + 1):
                dimacs_output += "-{0} -{1} 0\n".format(
                        to_base(i, j, k, size), to_base(i, j_s, k, size))
                clauses += 1

dimacs_output += "c Column constraint\n"
for i in range(1, size + 1):
    for j in range(1, size + 1):
        for k in range(1, numbers + 1):
            for i_s in range(i + 1, numbers + 1):
                dimacs_output += "-{0} -{1} 0\n".format(to_base(i, j, k, size),
                        to_base(i_s, j, k, size))
                clauses += 1

dimacs_output += "c 3x3 block constrain\n"

sq = int(sqrt(size))
for k in range(1, size + 1):
    for a in range(sq):
        for b in range(sq):
            for u in range(1, sq+1):
                for v in range(1, sq):
                    for w in range(v + 1, sq + 1):
                        dimacs_output += "-{0} -{1} 0\n".format(
                                to_base(sq*a + u, sq*b + v, k, size),
                                to_base(sq*a + u, sq*b + w, k, size))
                        clauses += 1
for k in range(1, size + 1):
    for a in range(sq):
        for b in range(sq):
            for u in range(1, sq):
                for v in range(1, sq+1):
                    for w in range(u + 1, sq+1):
                        for t in range(1, sq+1):
                            dimacs_output += "-{0} -{1} 0\n".format(
                                    to_base(sq*a+u, sq*b+v, k, size),
                                    to_base(sq*a+w, sq*b+t, k, size))
                            clauses += 1


dimacs_output = "p cnf {0} {1}\n".format(variables, clauses) + dimacs_output

# Write to file
args.tmp_out.write(dimacs_output)


# -----------------------------------------
# Run minisat
# -----------------------------------------
print ("Running Minisat")
call([args.minisatexe, args.tmp_out.name, args.tmp_in])

# -----------------------------------------
# Load solved board
# -----------------------------------------

with open(args.tmp_in, "r") as f_in:
    solved_board = f_in.read()

print ("Solved board:")

# -----------------------------------------
# CONVERT SOLVED BOARD
# -----------------------------------------

# Clean solved board
solved_board = solved_board.split()
sb = ""
for s in solved_board:
    try:
        l = int(s)
        if l > 0:
            (i, j, k) = from_base(l, size)
            sb += str(k)
    except:
        print ("yeah...")



args.outputfile.write(output_board(sb))



