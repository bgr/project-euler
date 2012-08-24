# Evaluate the sum of all the amicable numbers under 10000.
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are 
# an amicable pair and each of a and b are called amicable numbers.
# 
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

def divisors(n):
  from math import sqrt
  divs = [1]
  for i in xrange(2, int(sqrt(n))+1):
    if n % i == 0 and n != i:
      divs.append(i)
      if i < sqrt(n):
        divs.append(n/i)
  return sorted(divs)

divisor_sums = {}

for i in range(10001):
  divisor_sums[i] = sum(divisors(i))

amicable = {}
for k,v in divisor_sums.iteritems():
  if k!=v and v in divisor_sums and divisor_sums[v]==k:
    amicable[k] = None
    
print sum(amicable.iterkeys())