# Sudoku Solver
Reducing SAT to Sudoku

Evan Wilde | Sebastien Guillemot | Shayla Redlin | Laura Grondahl<br>
University of Victoria | CSC 320 | Spring 2015<br>
Professor: Bruce Kapron

## Submitted Documents
   Filename         | Description
   ---------------- | ------------------------------------------------------------------------------
   sudoku.py        | Solves Sudoku using the minimal encoding described in `Sudoku-as-SAT.pdf`
   sudoku_ext.py    | Solved Sudoku using the extended encoding described in `CMU_Sudoku-as-SAT.pdf`
   docs/Sudoku_As_SAT.pdf        | The results of our work
   tests/puzzles/   | Directory containing all of the test puzzles
   print_functions.py   | Contains custom print functions (for "pretty printing") imported by our sudoku solvers
   xmath.py         | Contains custom math functions imported by our sudoku solvers


## Usage
### Requirements
    - python3
    - minisat executable

[**minisat**](http://minisat.se/MiniSat.html) donwload page

### Execution

`python3 <inputfile> <outputfile> <minisat_executable> <tmp_out> <tmp_in>`

    - inputfile contains the unsolved board
    - outputfile will contain the solved board
    - minisat_executable is the path to the minisat executable
    - tmp_out is the generated rules for the sat solver
    - tmp_in is the output from the sat solver to be converted back to a sudoku board
