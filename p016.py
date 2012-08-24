# What is the sum of the digits of the number 2^1000 ?

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
  
num = '1'
for i in range(1000):
  num = bigAdd(num, num)
  
print reduce(lambda a,b: int(a)+int(b), num)