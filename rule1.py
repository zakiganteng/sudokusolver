# Minimal Encoding
from xmath import to_base
from xmath import to_index

# Every cell contains at least one number
def rule1(base):
    rules = []
    rule = ""
    clauses = 0
    for i in range(1, base+1):
        for j in range(1, base + 1):
            for k in range(1, base + 1):
                rule += "{0} ".format(to_base(i, j, k, base))
            rule += "0\n"
            clauses += 1
            rules.append(rule)
    ret_string = "p cnf {0} {1}\n".format(base * base * base, clauses)
    ret_string += rule
    return ret_string
