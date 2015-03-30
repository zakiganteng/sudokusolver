from xmath import to_base
import math

def ext_rule1(base):

    rules = []
    base_sqrt = int(math.sqrt(base))
    for roff in range(0, base_sqrt-1):
        for coff in range(0, base_sqrt-1):
            for k in range(1, base+1):
                for i in range(1, base_sqrt+1):
                    for j in range(1, base_sqrt+1):
                        rules.append(to_base(base_sqrt*roff + i, base_sqrt*coff + j, k, base)
    ret_string = 'p cnf {0} {1}\n'.format(base**3, len(rules))
    for i in rules:
        ret_string += '{0} 0\n'.format(i)
    return ret_string
