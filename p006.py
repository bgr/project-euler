# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

squares = map(lambda n: n*n, range(101))
sums = sum(range(101))
print sums**2 - sum(squares)
