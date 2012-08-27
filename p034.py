# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from math import factorial

def is_sum_of_digits(num):
  digits_fact = map(factorial, map(int, str(num)))
  return num == sum(digits_fact)

# limit is set to the first value where largest i-digit number is larger
# than maximum sum that can be obtained with factorials of its digits
# (exact limit is actually much lower than this)
limit = [i*factorial(9) for i in range(10) if 10**i-1 > i*factorial(9)][0]
numbers = [i for i in range(3,limit) if is_sum_of_digits(i)]

print 'numbers:', numbers
print 'sum:', sum(numbers)