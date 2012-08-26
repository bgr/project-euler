# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def divider(n,d):
  """
  returns tuple (integer part, decimal fraction part, cycle start index, cycle length)
  cycle start index value will be None if there is no cycle
  """
  whole, n = divmod(n,d)
  fraction = 0
  prev_remainders = []
  while True:
    q, n = divmod(n,d)
    fraction = fraction*10 + q
    if n == 0:
      return (whole, fraction, None, 0)
    elif n in prev_remainders:
      ci = prev_remainders.index(n)
      return (whole, fraction, ci, len(prev_remainders)-ci)
    else:
      prev_remainders.append(n)
      n *= 10

results = [ (divider(1, dv)[3], dv) for dv in range(1,1000) ] # tuples (cycle length, divisor)
print max(results)[1] # looks up by cycle length, prints divisor