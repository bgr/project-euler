# Find the first ten digits of the sum of one-hundred 50-digit numbers.

import fileinput

nums = [l.strip() for l in fileinput.input("p013_input.txt")]

# easy solution
bigsum = sum([int(n) for n in nums])
print bigsum
print str(bigsum)[0:10]

#hard solution
def bigAdd(n1, n2):
  if len(n1) < len(n2):
    n1 = n1.zfill(len(n2))
  elif len(n2) < len(n1):
    n2 = n2.zfill(len(n1))
  result = ''
  carry = 0
  for d in reversed(range(len(n1))):
    t = int(n1[d]) + int(n2[d]) + carry
    carry = 1 if t > 9 else 0
    result = str(t % 10) + result
  if carry != 0:
    result = '1' + result
  return result
  

bigsum = reduce(lambda a,b: bigAdd(a,b), nums)
print bigsum
print bigsum[0:10]
