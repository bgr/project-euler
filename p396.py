

def int_to_base(n, b):
    # returns list of digits
    assert n >= 0
    assert b > 1
    if n == 0:
        return [0]

    res = []
    while n>0:
        n, r = divmod(n,b)
        res += [r]
    return res


def base_to_int(ls, b):
    assert len(ls) > 0
    assert b > 1
    n = 0
    for i,d in enumerate(ls):
        n += d * (b**i)
    return n

def decrement(ls,base):
    "ls[0] is least significant digit, eg. number 6 in base 2 is [0,1,1]"
    assert ls[-1] > 0 # most significant digit must never be 0
    if len(ls) == 1: # borrowing from most significant digit
        if ls[0] == 1:
            return []
        else:
            return [ls[0]-1]
    if ls[0] > 0: # can decrement without borrowing
        return [ls[0]-1] + ls[1:] # decrement and append the rest of the list
    else: # borrow from someone
        return [base-1] + decrement(ls[1:], base)


def goodstein_length(n):
    base = 2
    ls = int_to_base(n, base)
    while len(ls) > 1:
        base += ls[0] + 1
        ls[0] = 0
        ls = decrement(ls,base)
    base += ls[0] - 2
    return base

def goodstein(n):
    assert n > 0
    k = 1
    res = []
    while n != 0:
        res += [n]
        k += 1
        t = int_to_base(n, k) 
        n = base_to_int(t, k+1) - 1
    return res

assert len(goodstein(2)) == 3
assert len(goodstein(4)) == 21
assert len(goodstein(6)) == 381
assert len(goodstein(7)) == 2045
assert sum([len(goodstein(i)) for i in range(1,8)]) == 2517
assert goodstein_length(2) == 3
assert goodstein_length(4) == 21
assert goodstein_length(6) == 381
assert goodstein_length(7) == 2045
assert sum([goodstein_length(i) for i in range(1,8)]) == 2517

#for i in range(1,8): print goodstein_length(i)
#print goodstein(4)
print goodstein_length(7)
#lengths = [len(goodstein(i)) for i in range(1,16)]
#print lengths
