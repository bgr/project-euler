# What is the sum of both diagonals in a 1001 by 1001 spiral?

# trying out tail call optimization (see tailcall.py)
from tailcall import tail_call_optimized

@tail_call_optimized
def sum_diagonals(width, summed=0):
  assert width > 0
  assert width%2 == 1
  if width == 1:
    return summed+1
  # this outer shell start value is inner square's max value + 1
  start_value = (width-2)**2 + 1 
  # values of shell's corners
  lr = start_value + width-2
  ll = lr + width-1
  ul = ll + width-1
  ur = ul + width-1
  return sum_diagonals(width-2, summed + lr + ll + ul + ur)
  

print sum_diagonals(1001)