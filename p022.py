# What is the total of all the name scores in the file?
# begin by sorting it into alphabetical order. Then working out the 
# alphabetical value for each name, multiply this value by its alphabetical 
# position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, 
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 * 53 = 49714.

data = open('p022_input.txt', 'r').read()
names = sorted([n[1:-1] for n in data.split(',')])

def get_alphabetical_value(str):
  from string import ascii_lowercase
  return sum([ascii_lowercase.index(i)+1 for i in str.lower()])


print sum([get_alphabetical_value(v)*(i+1) for i,v in enumerate(names)])
