# Discover all the fractions with an unorthodox cancelling method and find the value of the denominator.

def bad_cancel(n,d):
  ln = map(int, str(n))
  ld = map(int, str(d))
  for i in reversed(range(len(ln))):
    if ln[i] in ld:
      del ld[ld.index(ln[i])]
      del ln[i]
  r = lambda a,b: a*10+b
  if not ln: ln = [1]
  if not ld: ld = [1]
  return reduce(r, ln), reduce(r, ld)


assert bad_cancel(49, 98) == (4, 8)
assert bad_cancel(50, 30) == (5, 3)
assert bad_cancel(71289, 69241782) == (1, 642)
assert bad_cancel(69241782, 69241782) == (1, 1)
assert bad_cancel(69241782, 71289) == (624, 1)
assert bad_cancel(123, 456) == (123, 456)

def test(a,b):
  ca,cb = bad_cancel(a,b)
  if (a%10==0 and b%10==0) or (ca==a or cb==b) or cb == 0:
    return False
  return float(ca)/cb == float(a)/b
  
fracts = [bad_cancel(a,b) for a in range(10,100) for b in range(a+1,100) if test(a,b)]
result = reduce(lambda a,b: (a[0]*b[0], a[1]*b[1]), fracts)

from fractions import gcd
print result[1]/gcd(*result)