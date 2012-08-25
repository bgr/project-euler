# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# see http://en.wikipedia.org/wiki/Factorial_number_system

def to_factoriadic(n):
  "convert number in base 10 to factorial base"
  res = 0
  i = 1
  while True:
    d, r = divmod(n, i)
    res = r*pow(10,i-1) + res
    n = d
    i += 1
    if d==0: break
  return res
  
def from_factoriadic(f, step=1):
  "convert number in factorial base to base 10"
  d, r = divmod(f, 10)
  if d==0:
    return f
  else:
    return from_factoriadic(d, step+1)*step + r

def permutate(lst, factoriadic):
  lst = lst[:]
  res = []
  indices = [int(i) for i in str(factoriadic)]
  if len(indices) < len(lst): # pad with zeroes
    indices = [0]*(len(lst)-len(indices)) + indices
  for i in indices:
    res.append(lst[i])
    del lst[i]
  return res
  
# test
assert from_factoriadic(341010) == 463
assert to_factoriadic(463) == 341010
assert from_factoriadic(4041000) == 2982
assert to_factoriadic(2982) == 4041000
assert permutate(['A','B','C','D','E','F','G'], 1403110) == ['B','F','A','G','D','E','C']
assert permutate([0,1,2], to_factoriadic(0)) == [0,1,2]
assert permutate([0,1,2], to_factoriadic(3)) == [1,2,0]
assert permutate([0,1,2], to_factoriadic(5)) == [2,1,0]

result = permutate(range(10), to_factoriadic(999999))
print reduce(lambda a,b: str(a)+str(b), result)