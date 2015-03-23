# Minimal Encoding
from xmath import to_base

# Every cell contains at least one number
def rule1(base):
    rule = "c Every cell contains at least one number\n"
    variables = base**3
    clauses = base**2
    rule += "p cnf {0} {1}\n".format(variables, clauses)
    clause = ""
    for i in range(1, base):
        for j in range(1, base):
            for k in range(1, base):
                variable = to_base(i, j, k, base)
                clause += "{0} ".format(variable)
            rule += clause
            rule += "0\n"
    return rule