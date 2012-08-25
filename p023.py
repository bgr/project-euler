# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def divisors(n):
  from math import sqrt
  divs = [1]
  for i in xrange(2, int(sqrt(n))+1):
    if n % i == 0 and n != i:
      divs.append(i)
      if i < sqrt(n):
        divs.append(n/i)
  return sorted(divs)


abundant_set = {i for i in xrange(1,28124-12) if sum(divisors(i)) > i}

def is_sum_of_abundants(n):
  for i in abundant_set:
    if n-i in abundant_set:
      return True
    if i>n:
      return False
  print 'gone over'
  return False

result = [i for i in xrange(1,28124) if not is_sum_of_abundants(i)]
print sum(result)