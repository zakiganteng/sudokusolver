# Returns an integer index
def to_base(i, j, k, base):
    return base*base * (i - 1) + base * (j - 1) + (k - 1) + 1

# Returns a 3 tuple (i, j, k)
def from_base(n, base):
    n = n - 1
    k = n % base + 1
    j = int(((n - (k - 1)) / base) % base + 1)
    i = int(((n - (k - 1)) - base * (j - 1))/ (base * base)) + 1
    return (i, j, k)
