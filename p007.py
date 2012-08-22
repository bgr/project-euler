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

# I used the code from p010.py
# code below works but it's much slower
#def genPrimes(limit):
#  sieveTable = []
#  while True:
#    candidate = len(sieveTable) + 2
#    if candidate >= limit:
#      break
#    
#    isPrime = True
#    for i,stillValid in enumerate(sieveTable):
#      if stillValid:
#        p = i+2 # numbers in sieveTable are index + 2
#        if candidate % p == 0:
#          isPrime = False
#          break
#    
#    sieveTable.append(isPrime)
#    if isPrime: yield candidate


i, limit = 0, 10001
primes = genPrimes(200000)

while i<limit-1:
  primes.next()
  i+=1

print primes.next()
