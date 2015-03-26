from xmath import to_base
import math

def rule4(base):
    rules = []
    sq = int(math.sqrt(base))
    for k in range(1, base+1):
        for a in range(sq):
            for b in range(sq):
                for u in range(1, sq+1):
                    for v in range(1, sq):
                        for w in range(v+1, sq+1):
                            rules.append((-to_base(sq*a + u, sq*b + v, k, base),
                                          -to_base(sq*a+u, sq*b+w, k, base)))
    ret_string = 'p cnf {0} {1}\n'.format(base**3, len(rules))
    for (i, j) in rules:
        ret_string += '{0} {1} 0\n'.format(i, j)
    return ret_string
