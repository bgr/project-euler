# How many circular primes are there below one million?

from primes import generate_primes

primes = set(generate_primes(1000000))

def is_circular(n):
  assert n in primes
  rotations = len(str(n)) - 1
  for _ in range(rotations):
    n,r = divmod(n,10)
    n = r*10**rotations + n
    if not n in primes:
      return False
  return True
  
circular = [i for i in primes if is_circular(i)]
print len(circular)