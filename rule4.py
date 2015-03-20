from xmath import to_base, from_base

base = 9    
rule4 = []
for k in range(1,10):
    for a in range(3):
        for b in range(3):
            for u in range(1,4):
                for v in range(1,3):
                    for w in range(v+1, 4):
                        rules.append((-to_base(3*a + u, 3*b + v, k, base), -to_base(3*a+u, 3*b+w, k, base)))
                        
print('p cnf {0} {1}'.format(base**3, len(rules)))
for (i, j) in rule4:
    print('{0} {1}'.format(i,j))