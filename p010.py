# Calculate the sum of all the primes below two million.

def genPrimes(limit):
  sieveTable = [True for n in range(2,limit)]
  for i,stillValid in enumerate(sieveTable):
    if stillValid:
      jumpStep = i+2 # numbers are offset by 2 
      j = i+jumpStep
      while j<len(sieveTable):
        sieveTable[j] = False
        j+=jumpStep
      yield i+2


primes = [i for i in genPrimes(2000000)]

print sum(primes)
