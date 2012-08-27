# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# Identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

import itertools
perms = itertools.permutations(range(1,10))

products = set()

r = lambda a,b: 10*a+b

for p in perms:
  for i in range(1,7):
    for j in range(i+1,8):
      a = reduce(r, p[:i])
      b = reduce(r, p[i:j]) 
      c = reduce(r, p[j:])
      if a*b==c:
        print '%s x %s = %s' % (a,b,c)
        products.add(c)

print 'sum of products:', sum(products)