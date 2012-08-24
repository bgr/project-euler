# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.

from itertools import izip_longest

units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
decades = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
magnitudes = ['','thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion']

def grouper(n, iterable, fillvalue=None):
  "Collect data into fixed-length chunks or blocks"
  # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
  args = [iter(iterable)] * n
  return izip_longest(fillvalue=fillvalue, *args)

def num_to_words(n):
  if n == 0:
    return 'zero'
  
  words = ''
  if n<0:
    words = 'minus '
  
  sn = str(abs(n))
  # pad with zeroes so it can be split into chunks of 3 digit numbers
  pad_length = -len(sn) % 3 + len(sn)
  padded = sn.rjust(pad_length, '0')
  chunks = [int(''.join(i)) for i in grouper(3, padded)]
  
  for m,c in enumerate(chunks):
    h,rest = divmod(c,100)
    d,u = divmod(rest, 10)
    
    if m>0: # isn't the last chunk
      if m==len(chunks)-1 and h==0 and rest > 0:
        words += ' and ' # eg. "one thousand_and_two"
      else:
        words += ' ' # add only space, eg. "one thousand_three hundred and two"
    
    if h: # has hundreds
      words += units[h] + ' hundred ' + ('and ' if rest else '')
    if rest >= 20: # numbers 20-99
      words += decades[d] + ('-' + units[u] if u else '')
    elif rest > 0: # numbers 1-20
      words += units[rest]
    
    if m < len(chunks)-1: # should append order of magnitude
      words += ' ' + magnitudes[len(chunks)-m-1]
    
  return words

# test
# for i in range(-200,4500,17): print i, num_to_words(i)
# print num_to_words(17237987654001)

from string import ascii_lowercase
lowercase_only = lambda a: a in ascii_lowercase
lengths = [len(filter(lowercase_only, num_to_words(i))) for i in range(1,1001)]
print sum(lengths)