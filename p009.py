# Find the only Pythagorean triplet, {a, b, c}, for which a + b + c = 1000.

from math import sqrt

for a in range(500):
  for b in range(500):
    c = sqrt(a**2+b**2)
    if a + b + c == 1000:
      print a, b, int(c), int(a*b*c)
