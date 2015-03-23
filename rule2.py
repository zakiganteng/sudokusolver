# Minimal Encoding
from xmath import to_base

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
