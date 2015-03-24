# Minimal Encoding
from xmath import to_base
from xmath import to_index

# Every cell contains at least one number
def rule1(base, board):
    rules = []
    for i in range(1, base+1):
        for j in range(1, base+1):
            val = board[to_index(i,j, base)]
            if val == '0':
                for k in range(1, base+1):
                    rules.append(-to_base(i, j, k, base))
            else:
                rules.append(-to_base(i, j, val, base))
    ret_string = 'p cnf {0} {1}\n'.format(base**3, len(rules))
    for i in rules:
        ret_string += '{0} 0\n'.format(i)
    return ret_string