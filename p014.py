# Find the longest sequence using a starting number under one million.
# The following iterative sequence is defined for the set of positive integers:
# n  n/2 (n is even)
# n  3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 13  40  20  10  5  16  8  4  2  1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.

def get_chain(n):
  chain = [n]
  while n>1:
    if n%2==0:
      n = n/2
    else:
      n = 3*n + 1
    chain.append(n)
  return chain
  
max_chain_length = 0
max_num = 0
chain = []
for i in reversed(range(1000000)):
  chain = get_chain(i)
  if len(chain) > max_chain_length:
    max_chain_length = len(chain)
    max_num = i
    print i, len(chain)
    
print max_num, max_chain_length