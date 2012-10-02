# For any positive integer n, the nth weak Goodstein sequence {g1, g2, g3, ...}
# is defined as:
#
#   g_1 = n
#   for k > 1, g_k is obtained by writing g_k-1 in base k,
#   interpreting it as a base k + 1 number, and subtracting 1.
#
# The sequence terminates when gk becomes 0.
#
# For example, the 6th weak Goodstein sequence is {6, 11, 17, 25, ...}:
#   g1 = 6.
#   g2 = 11 since 6 = 110 base 2, 110 base 3 = 12, and 12 - 1 = 11.
#   g3 = 17 since 11 = 102 base 3, 102 base 4 = 18, and 18 - 1 = 17.
#   g4 = 25 since 17 = 101 base 4, 101 base 5 = 26, and 26 - 1 = 25.
#   and so on.
#
#  It can be shown that every weak Goodstein sequence terminates.
#
#  Let G(n) be the number of nonzero elements in the nth weak Goodstein sequence.
#  It can be verified that G(2) = 3, G(4) = 21 and G(6) = 381.
#  It can also be verified that Sum(G(n)) = 2517 for 1 <= n < 8.
#
#  Find the last 9 digits of Sum(G(n)) for 1 <= n < 16


def int_to_base(n, b):
    # returns list of digits, least significant digit is at position 0
    assert n >= 0
    assert b > 1
    if n == 0:
        return [0]

    res = []
    while n>0:
        n, r = divmod(n,b)
        res += [r]
    return res

# Solution details:
#
# for Goodstein sequence see http://en.wikipedia.org/wiki/Goodstein%27s_theorem 
# (note that this is not the weak version, but the calculation of length is similar)
#
# for the "f" function see http://en.wikipedia.org/wiki/Large_numbers
# and video series (parts 5-10) http://www.youtube.com/watch?v=4-mDIuPI8Rk


import sys
sys.setrecursionlimit(2500) # unpacking powers of "f" goes deep

Mod = int(1e9) # since solution requires only last 9 digits

def f(n,k,p=1):
    "fast-growing hierarchy function"
    assert n > 0
    assert k >= 0
    assert p > 0
    # uncomment to see the expansion of "f" function
    #print "f_%s%s(%s)" % (k, ("^%s" % p) if p>1 else "", n)
    if p > 1: # unpack, f^3(n) = f(f(f(n)))
        return f(f(n,k,p-1),k,1)
    if k==0: # f_0(n) = n + 1
        return (n + 1) % Mod
    # handling k==1 does not seem to improve speed
    #if k==1: # f_1(n) = f_0^n(n) = f_0(f_0(...(f_0(n)))) n times
    #    return (n*2) % Mod
    #
    # handling of k==2 is a must because of modulo pow operations
    if k==2: # f_2(n) = f_1^n(n) = 2*2*2*...*2*n = (2^n)*n 
        return (pow(2,n,Mod)*n % Mod)
    # else if k > 0:
    return f(n,k-1,n) # f_k+1(n) = f_k^n(n)


# to calculate the length of a sequence for number n
# represent n in base 2, and for every 1 digit recursively
# apply the "f" function, with k equal to power of 2 for that digit
# and the initial value being 3, and finally subtract 3
# e.g. 5 = 101 = 2^2 + 2^0 -> G(5) = f_2(f_0(3)) - 3

def goodstein_length(n):
    "returns length (mod 1e9) of Goodstein sequence for seed n"
    fval = 3
    for i,b in enumerate(int_to_base(n,2)):
        if b==1:
            fval = f(fval,i)
    return fval - 3

lengths = [goodstein_length(i) for i in range(1,16)]
for i,l in enumerate(lengths): print "G(%s) = %s (mod %s)" % (i+1, l, Mod)
print "Problem solution: %s" % (sum(lengths) % Mod)
