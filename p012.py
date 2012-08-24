# What is the value of the first triangle number to have over five hundred divisors?

from math import sqrt

def triangular_with_divisors(min_divisors):
  a, b = 0, 1
  while True:
    a = a + b
    b += 1
    divs = 0
    for i in xrange(1, int(sqrt(a))+1):
      if a % i == 0:
        divs += 1
        if i < sqrt(a):
          divs += 1 
          # if a is divisible by i then it's divisible by a/i too
          # eg. 15 is divisible by 1, therefore by 15 also, and by 3, therefore by 5 also
          # but for 49 we shouldn't add 7 twice hence the check i < sqrt(a)
        if divs >= min_divisors:
          return a, b, divs


print triangular_with_divisors(501)