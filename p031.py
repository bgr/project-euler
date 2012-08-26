# How many different ways can £2 be made using any number of coins?
# Available coins: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

def combinations(target, values):
  # values = sorted(values)
  n = 0
  for i,val in enumerate(values):
    for times in range(1,target/val+1):
      if val*times > target:
        continue
      if val*times == target:
        n += 1
      n += combinations(target-val*times, values[i+1:])
  return n

  
print combinations(200, [1,2,5,10,20,50,100,200])