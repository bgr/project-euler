# Find the product of the coefficients, a and b, for the quadratic 
# expression that produces the maximum number of primes for 
# consecutive values of n, starting with n = 0.
#
# Euler published the remarkable quadratic formula:
# n² + n + 41
# 
# It turns out that the formula will produce 40 primes 
# for the consecutive values n = 0 to 39. 
# However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
# and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.
# Using computers, the incredible formula n² - 79n + 1601 was discovered,
# which produces 80 primes for the consecutive values n = 0 to 79. 
# The product of the coefficients, -79 and 1601, is -126479.
# 
# Considering quadratics of the form:
# n² + an + b, where |a| < 1000 and |b| < 1000
# where |n| is the modulus/absolute value of n, e.g. |11| = 11 and |4| = 4

def get_primes(limit):
  from math import sqrt
  sieveTable = [True for n in range(2,limit)]
  for i in range(2, int(sqrt(limit))+1):
    if sieveTable[i-2]: # numbers are offset by 2
      for j in range(i*i-2, limit-2, i):
        sieveTable[j] = False
  return [i+2 for i,v in enumerate(sieveTable) if v]


primes = set(get_primes(1000000))

def quadratic_produce_primes(a, b):
  produced = []
  n = 0
  while True:
    next = (n*n + a*n + b)
    if next not in primes:
      return produced
    produced.append(next)
    n += 1
    
assert len(quadratic_produce_primes(1,41)) == 40
assert len(quadratic_produce_primes(-79,1601)) == 80

max_produced = 0
max_a, max_b = None, None
for a in range(-999, 1000):
  for b in range(-999, 1000):
    p = quadratic_produce_primes(a,b)
    if len(p) > max_produced:
      max_produced = len(p)
      max_a, max_b = a, b
      
print 'n^2 + %s*n + %s produces %s primes' % (max_a, max_b, max_produced)
print 'product of coefficients is %s' % (max_a * max_b)