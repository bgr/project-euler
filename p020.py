# Find the sum of the digits in the number 100!

# easy solution using bigint support
fact = reduce(lambda a,b: a*b, range(1,101))
print reduce(lambda a,b: int(a)+int(b), str(fact))

# hard solution using string as bigint
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
  
fact = '1'
for i in range(2,101):
  temp_fact = fact
  for _ in range(i-1):
    fact = bigAdd(fact,temp_fact)
  
print reduce(lambda a,b: int(a)+int(b), str(fact))