# What is the first term in the Fibonacci sequence to contain 1000 digits?

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

  
f1 = '0'
f2 = '1'
i = 1
while len(f2) < 1000:
  f1, f2 = f2, bigAdd(f2,f1)
  i += 1

print i