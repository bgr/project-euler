
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

# see http://en.wikipedia.org/wiki/Lehmer_code

def lehmer_indices(f, pad_to_length=0):
  "returns array with permutation indices when passed a factoriadic number"
  idx = map(int, str(f))
  for i in range(len(idx)):
    for j in range(i+1, len(idx)):
      if idx[i] < idx[j] and idx[j]>0:
        idx[j] -= 1
  if len(idx) < pad_to_length:
    idx = [0]*(pad_to_length-len(idx)) + idx
  return idx

def permutate(lst,indices):
  lst = lst[:]
  res = []
  #if len(lst) > len(indices):
  #  res = lst[:len(indices)]
  for i in indices:
    res.append(lst[i])
    del lst[i]
  return res
  
# test
assert from_factoriadic(341010) == 463
assert to_factoriadic(463) == 341010
assert from_factoriadic(4041000) == 2982
assert to_factoriadic(2982) == 4041000
assert lehmer_indices(1506342) == [1,4,0,3,1,1,0]
assert lehmer_indices(1506342,7) == [1,4,0,3,1,1,0]
assert permutate(['A','B','C','D','E','F','G'], [1,4,0,3,1,1,0]) == ['B','F','A','G','D','E','C']

lst  = range(10)
perm = 1000000
fact = to_factoriadic(perm)
idx  = lehmer_indices(fact,len(lst))
res  = permutate(lst,idx)
print '%s is %s when permutated with indices %s (perm=%s, factoriadic=%s)' % (lst, res, idx, perm, fact)
print 'result: %s' % reduce(lambda a,b: str(a)+str(b), res)

#result = permutate(range(10), lehmer_indices(to_factoriadic(1000000),10))
#print reduce(lambda a,b: str(a)+str(b), result)