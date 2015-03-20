#!/usr/bin/python3

# Returns an integer index
def to_base(i, j, k, base):
    return base**2 * (i - 1) + base * (j - 1) + (k - 1) + 1

# Returns a 3 tuple (i, j, k)
def from_base_nine(n):
    pass

# Should equal 324
pt = (4, 9, 9)
print (pt)
print (to_base_nine(pt[0], pt[1], pt[2]))
