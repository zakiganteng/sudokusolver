#sudokusolver

Documentation

To run our solution, please complete the following steps.
<ol>
  <li>Download the files listed in README.md in your chosen directory</li>
  
  <li>In this directory, create the following documents:
      <ol>
        <li>inputfile.txt (containing a string in the "1..2..3" fomrat defining your puzzle</li>
        <li>outputfile.txt (blank, will contain the solved board)</li>
        <li>minisatexe.exe (or other, if your minisat solver has a different name)</li>
        <li>tmp_out.txt (blank, will contain the created rules)</li>
        <li>tmp_in.txt (blank, will contain the intermediate represenation of the solved board)</li>
      </ol>
  </li>
  
  <li>Open a Python3 interpreter and execute the following command (note: each argument should be a file name):
      sudoku2.py [inputfile] [outputfile] [minisatexe] [tmp_out] [tmp_in]</li>
  
  <li>Open outputfile.txt to read the results of running the SAT solver</li>
  
  <li>That's it!</li>
  
</ol>


  
