# Find the maximum sum travelling from the top of the triangle to the base.

def pairwise(iterable):
  "s -> (s0,s1), (s1,s2), (s2, s3), ..."
  from itertools import tee, izip
  a, b = tee(iterable)
  next(b, None)
  return izip(a, b)

import fileinput
lines = [map(int, l.split()) for l in fileinput.input('p018_input.txt')] # also p067_input.txt

for i in reversed(range(1, len(lines))): # go from the bottom line
  for j,(a,b) in enumerate(pairwise(lines[i])): # go through line in pairs (0,1),(1,2),(2,3)...
    lines[i-1][j] += max(a,b) # add pair's larger value to the element above
    
print max(lines[0])