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

from print_functions import convert_board, output_board, base10toN
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

board = convert_board(args.inputfile.read())

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

print ("Generating Board Requirements...")

dimacs_output += "c the board requirements\n"
for j in range(0, size):
    for i in range(0, size):
        value = int(board[to_index(i, j, size)])
        if value != 0:
            value = to_base(i + 1, j + 1, value, size)
            clauses += 1
            dimacs_output += "{0} 0\n".format(value)

dimacs_output += "c at least one number per entry\n"
for i in range(1, size + 1):
    for j in range(1, size + 1):
        for k in range(1, numbers + 1):
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
                                                        to_base(i_s, j, k, size)
                                                        )
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

# ext rule 1
dimacs_output += 'c There is at most one number in each entry\n'
for x in range(1, size+1):
    for y in range(1, size+1):
        for z in range(1, numbers):
            for i in range(z+1, size+1):
                dimacs_output += '{0} {1} 0\n'.format(-to_base(x, y, z, size),
                                                      -to_base(x, y, i, size))
                clauses += 1

# ext rule 2
dimacs_output += 'c Each number appears at least once in each row\n'
for y in range(1, size+1):
    for z in range(1, size+1):
        for x in range(1, size+1):
            dimacs_output += str(to_base(x, y, z, size)) + ' '
        dimacs_output += '0\n'
        clauses += 1

# ext rule 3
dimacs_output += 'c Each number appears at least once in each column\n'
for x in range(1, size+1):
    for z in range(1, size+1):
        for y in range(1, size+1):
            dimacs_output += str(to_base(x, y, z, size)) + ' '
        dimacs_output += '0\n'
        clauses += 1

# ext rule 4
dimacs_output += 'c Each number appears at least once in each box\n'
for roff in range(0, sq):
    for coff in range(0, sq):
        for k in range(1, size+1):
            for i in range(1, sq+1):
                for j in range(1, sq+1):
                    dimacs_output += '{0} '.format(to_base(sq*roff + i,
                                                           sq * coff + j, k,
                                                           size))
            dimacs_output += '0\n'
            clauses += 1

dimacs_output = "p cnf {0} {1}\n".format(variables, clauses) + dimacs_output

# Write to file
args.tmp_out.write(dimacs_output)
args.tmp_out.close()


# -----------------------------------------
# Run minisat
# -----------------------------------------
print ("Running SAT solver")
try:
    call([args.minisatexe, args.tmp_out.name, args.tmp_in])
except OSError:
    print ("Fatal Error: Could not run", args.minisatexe)
    exit(1)

# -----------------------------------------
# Load solved board
# -----------------------------------------

with open(args.tmp_in, "r") as f_in:
    solved_board = f_in.read()

# -----------------------------------------
# CONVERT SOLVED BOARD
# -----------------------------------------

# Clean solved board
solved_board = solved_board.split()
if (solved_board[0] != "SAT"):
    print ("Unsolvable puzzle")
    exit(0)
# Remove "SAT"
solved_board.pop(0)

# convert to string
sb = ""
for s in solved_board:
    try:
        l = int(s)
        if l > 0:
            (i, j, k) = from_base(l, size)
            sb += base10toN(k, 36)
    except:
        pass

# rebuild the solved board non-transpose
fixed = ""
for i in range(0, size):
    for j in range(0, size):
        fixed += sb[to_index(i, j, size)]
args.outputfile.write(output_board(fixed))
