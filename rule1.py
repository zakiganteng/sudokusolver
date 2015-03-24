# Minimal Encoding
from xmath import to_base
from xmath import to_index

# Every cell contains at least one number
def rule1(base, board):
    rules = []
    count = 0
    for i in range(1, base+1):
        for j in range(1, base+1):
            val = board[to_index(i-1,j-1, base)]
            ors = []
            if val == '0':
                for k in range(1, base+1):
                    ors.append(to_base(i, j, k, base))
                    count += 1
            else:
                ors.append(to_base(i, j, val, base))
                count += 1
            rules.append(ors)
    ret_string = 'p cnf {0} {1}\n'.format(count, len(rules))
    for ors in rules:
        for val in ors:
            ret_string += str(val) + " "
        ret_string += "0\n"
    return ret_string
