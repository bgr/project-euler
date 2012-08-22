# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(str):
  for i in range(len(str) / 2 + 1):
    if str[i] != str[-i-1]:
      return False
  return True

palindromes = []

for i in reversed(range(100,1000)):
  for j in reversed(range(100,1000)):
    if isPalindrome(str(i*j)):
      palindromes.append((i*j,i,j))
      
print sorted(palindromes)[-1]
