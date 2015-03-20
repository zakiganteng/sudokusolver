#!/usr/bin/python3

# Returns an integer index
def to_base_nine(i, j, k):
    return 81 * (i - 1) + 9 * (j - 1) + (k - 1) + 1

# Returns a 3 tuple (i, j, k)
def from_base_nine(n):
    pass

# Should equal 324
pt = (4, 9, 9)
print (pt)
print (to_base_nine(pt[0], pt[1], pt[2]))
