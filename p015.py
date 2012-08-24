# Starting in the top left corner in a 20 by 20 grid, how many routes are there to the bottom right corner?

def pascal_triangle(n):
  t = [1]
  for _ in range(n):
    t = [sum(i) for i in zip([0]+t, t+[0])] 
    # zips [0, 1, 2, 1] with [1, 2, 1, 0] to get [(0, 1), (1, 2), (2, 1), (1, 0)]
    # and then sums to get next triangle element: [1, 3, 3, 1]
  return t

grid_width = 20
n_steps = (grid_width+1)*2 - 2  # +1 is required because they're sneaky bastards :)

print max(pascal_triangle(n_steps))