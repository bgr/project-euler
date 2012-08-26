# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def is_sum_of_digits(num, power):
  if num == 0 or num == 1: # exceptions by definition
    return False
  digits_powered = map(lambda a: int(a)**power, str(num))
  return num == sum(digits_powered)
  
assert is_sum_of_digits(1634,4)
assert is_sum_of_digits(8208,4)
assert is_sum_of_digits(9474,4)
assert not is_sum_of_digits(1635,4)
assert not is_sum_of_digits(8207,4)
assert not is_sum_of_digits(9473,4)
assert not is_sum_of_digits(2,4)
assert not is_sum_of_digits(1,4)
assert not is_sum_of_digits(0,4)

# limit is the first value where largest i-digit number is larger
# than maximum sum that can be obtained with powered digits
limit = [i*(9**5) for i in range(10) if 10**i-1 > i*9**5][0]
numbers = [i for i in range(limit) if is_sum_of_digits(i,5)]
print 'numbers:', numbers
print 'sum:', sum(numbers)