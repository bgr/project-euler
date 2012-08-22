# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def genFib(limit):
  p1 = 0
  p2 = 1
  while p1+p2 < limit:
    p1, p2 = p2, p1+p2    
    yield p2
    

fibs = [i for i in genFib(4000000)]

evenfibs = filter(lambda x: x%2==0, fibs)

print sum(evenfibs)
