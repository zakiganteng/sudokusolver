from xmath import to_base

def ext_rule1(base):
    rules = []
    for x in range(1, base+1):
        for y in range(1, base+1):
            for z in range(1, base):
                for i in range(z+1, base+1):
                    rules.append((-to_base(x,y,z,base), -to_base(x,y,i, base)))
    ret_string = 'p cnf {0} {1}\n'.format(base**3, len(rules))
    for (i, j) in rules:
        ret_string += '{0} {1} 0\n'.format(i, j)
    return ret_string
