from xmath import to_base
import math

def rule4(base):
    rules = []
    for k in range(1, base+1):
        for a in range(math.sqrt(base)):
            for b in range(math.sqrt(base)):
                for u in range(1, 4):
                    for v in range(1, 3):
                        for w in range(v+1, 4):
                            rules.append((-to_base(3*a + u, 3*b + v, k, base),
                                          -to_base(3*a+u, 3*b+w, k, base)))
    ret_string = 'p cnf {0} {1}\n'.format(base**3, len(rules))
    for (i, j) in rules:
        ret_string += '{0} {1} 0\n'.format(i, j)
    return ret_string