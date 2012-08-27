from math import sqrt

def generate_primes(limit):
  sieveTable = [True for n in range(2,limit)]
  for i in range(2, int(sqrt(limit))+1):
    if sieveTable[i-2]: # numbers are offset by 2
      for j in range(i*i-2, limit-2, i):
        sieveTable[j] = False
  return [i+2 for i,v in enumerate(sieveTable) if v]