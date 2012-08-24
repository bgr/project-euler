# Find the maximum sum travelling from the top of the triangle to the base.

import fileinput

lines = [map(int, l.split()) for l in fileinput.input('p018_input.txt')] # also p067_input.txt
lines += [[0] * (len(lines[-1])+1)] # add one empty line at the bottom

# for l in lines: print l


# annotate lines with additional value to track sums
# line elements are now tuples (original_value, best_sum_value)
lines = [map(lambda a: (a, 0), l) for l in lines]

# for l in lines: print l

def get_best_sum(top, bottom):
  "returns top list annotated with values of best sum choice from bottom list"
  ret = []
  for i,(tl,tr) in enumerate(top):
    # choose element below that has larger sum
    better = max(tl+bottom[i][1], tl+bottom[i+1][1])
    ret.append((tl, better)) # append the annotated tuple
  ret.append((top[-1][0], top[-1][0]+bottom[-1][1])) # append missing final element
  return ret


for i in reversed( range(1, len(lines)) ): # go from bottom and fill in best sums
  lines[i-1] = get_best_sum(lines[i-1], lines[i])
  
print max(lines[0], key=lambda tup: tup[1])[1] # print max sum in the top line