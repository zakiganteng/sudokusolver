from xmath import to_base

# Evan Wilde
def rule3(base):
    rules = []
    for j in range(1, base+1):
        for k in range(1, base+1):
            for i in range(1, base):
                for l in range(j + 1, base+1):
                    rules.append((-to_base(i, j, k, base), -to_base(l, j, k,
                        base)))
    ret_string = 'p cnf {0} {1}\n'.format(base**3, len(rules))
    for (i, j) in rules:
        ret_string += '{0} {1} 0\n'.format(i, j)
    return ret_string

