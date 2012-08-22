# What is the smallest number divisible by each of the numbers 1 to 20?

divisors = [11,13,7,4,17,9,19,20]

print reduce(lambda a,b: a*b, divisors)
