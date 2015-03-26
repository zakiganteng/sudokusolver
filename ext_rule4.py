from xmath import to_base
import math

def ext_rule1(base):

    note: THIS DOESN'T WORK
        the first variable is an OR not an AND
    rules = []
    base_sqrt = int(math.sqrt(base))
    for z in range(1, base+1):
        for i in range(0, base_sqrt):
            for j in range(0, base_sqrt):
                for x in range(1, base_sqrt+1):
                    for y in range(1, base_sqrt+1):
                        rules.append(to_base(base_sqrt*i+x, base_sqrt*j + y, z, base)
    ret_string = 'p cnf {0} {1}\n'.format(base**3, len(rules))
    for i in rules:
        ret_string += '{0} 0\n'.format(i)
    return ret_string
