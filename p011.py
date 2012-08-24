# What is the greatest product of four adjacent numbers on the same straight line in the 20 by 20 grid?

import fileinput

grid = []

for line in fileinput.input("p011_input.txt"):
  ints = [int(s) for s in line.split()]
  grid.append(ints)

  
def find_max_product(grid, hdir, vdir, length):
  assert len(grid) > 0
  for l in grid: 
    assert len(l) == len(grid)
  assert hdir == 0 or hdir == 1
  assert vdir == -1 or vdir == 0 or vdir == 1
  assert length <= len(grid)
  
  size = len(grid)
  hsteps = size if hdir == 0 else size-length # will go 20 or 16 steps depending on the direction
  vsteps = size if vdir == 0 else size-length
  vstart = length-1 if vdir == -1 else 0 # don't start from first row if direction is up-right
  
  maxprod = 0
  for v in range(vstart, vstart+vsteps):
    for h in range(0, hsteps):
      prod = 1
      for l in range (0, length): # go l steps from the starting coordinates h,v
        prod *= grid[v+l*vdir][h+l*hdir]
      if prod > maxprod:
        maxprod = prod
  return maxprod

  
down      = find_max_product(grid, 0, 1, 4)
downright = find_max_product(grid, 1, 1, 4)
right     = find_max_product(grid, 1, 0, 4)
upright   = find_max_product(grid, 1, -1, 4)

print max([down, downright, right, upright])