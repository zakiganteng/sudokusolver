# Minimal Encoding
from xmath import to_base


# Every cell contains at least one number
def every_cell_has_number(base):
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

# Rule 2
def rule2(base):
    rule = "c Each number appears at most once in every row\n"
    variables = base**3
    clauses = 0
    rule_clauses = ""
    
    for i in range(1,base):
        for k in range(1, base):
            for j in range(1, base-1):
                for l in range(j+1, base):
                    x = to_base(i,j,k,base)
                    y = to_base(i,l,k,base)
                    rule_clauses += "-{0} -{1} 0\n".format(x, y)
                    clauses +=1
                    
    rule += "p cnf {0} {1}".format(variables, clauses)
    rule += rule_clauses
    return rule
