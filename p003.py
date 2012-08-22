# What is the largest prime factor of the number 600851475143 ?

num = 600851475143

from math import sqrt, ceil
for i in range(2, int(ceil(sqrt(num)))):
  while num % i == 0 and i < num:
    print num, "/", i, "=", num / i
    num = num / i
  if i >= num: break
      

print num
