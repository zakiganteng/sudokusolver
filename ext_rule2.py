from xmath import to_base

def ext_rule2(base):
    ret_string = 'p cnf {0} {1}\n'.format(base**3, base**2)
    for y in range(1, base+1):
        for z in range(1, base+1):
            for x in range(1, base+1):
                ret_string += str(to_base(x,y,z, base)) + ' '
            ret_string += '0\n'
    return ret_string
