

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


#lengths = [len(goodstein(i)) for i in range(1,16)]
#print lengths
