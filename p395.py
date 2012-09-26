# see http://projecteuler.net/problem=395
# see the images of the fractal: p395_extremes.jpg and p395_full.jpg (recursion level 13)

class Matrix:
    # Matrix form:
    # | a c tx |
    # | b d ty |
    # | 0 0 1  |

    def __init__(self,a=1,b=0,c=0,d=1,tx=0,ty=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.tx = tx
        self.ty = ty

    def to_list(self):
        return [[self.a,self.c,self.tx],[self.b,self.d,self.ty],[0,0,1]]

    def mult(self, mx):
        A = self.to_list()
        B = mx.to_list()
        C = [[0,0,0],[0,0,0]]

        for row in range(2):
            for col in range(3):
                C[row][col] = 0
                for el in range(3):
                    C[row][col] += A[row][el]*B[el][col]
                    
        return Matrix(C[0][0],C[1][0],C[0][1],C[1][1],C[0][2],C[1][2])

    def __str__(self):
        return "| a:%s b:%s c:%s d:%s tx:%s ty:%s |" % (self.a, self.b, self.c, self.d, self.tx, self.ty)

    def __repr__(self):
        return self.__str__()


import collections
_Point = collections.namedtuple('Point',['x','y'])
_Square = collections.namedtuple('Square', ['bl','br','tl','tr','matrix'])

def Point(x,y,matrix=None):
    matrix = matrix or Matrix()
    transform = matrix.mult(Matrix(tx=x, ty=y))
    x = transform.tx
    y = transform.ty
    return _Point(x,y)

def Square(matrix=None):
    m = matrix or Matrix()
    bl, br, tl, tr = (Point(0,0,m), Point(1,0,m), Point(0,1,m), Point(1,1,m))
    return _Square(bl,br,tl,tr,m)

def print_square(sq):
    for p in sq[:-1]: print "%s,%s" % p



def grow(square): # grow two squares out of the given square
    rotate_left = Matrix(.8, .6, -.6, .8)
    rotate_right = Matrix(.6, -.8, .8, .6)

    scale_left = Matrix(.8, 0, 0, .8)
    scale_right = Matrix(.6, 0, 0, .6)

    def make_matrix(matrices):
        return reduce(lambda a,b: a.mult(b), matrices)

    mx_left = make_matrix([square.matrix, Matrix(ty=1), rotate_left, scale_left])

    mx_right = make_matrix([square.matrix, Matrix(tx=1, ty=1), rotate_right, scale_right, Matrix(tx=-1)])

    return (Square(mx_left), Square(mx_right))



#def recgrow(sq,reclevel=2):
#    if reclevel:
#        l,r = grow(sq)
#        print_square(l)
#        print_square(r)
#        recgrow(l,reclevel-1)
#        recgrow(r,reclevel-1)

#print_square(Square())
#recgrow(Square(),13)


eps = 1e-21

def reach_out(sq, comparator, axis):
    frontier = 0
    while True:
        l,r = grow(sq)
        #print_square(l)
        #print_square(r)
        sq, new_frontier = comparator(l, r, axis)
        diff = new_frontier - frontier
        frontier = new_frontier
        #print frontier, diff
        if abs(diff) < eps:
            break
    return frontier

comp_min = lambda a,b,axis: (a, a.tr[axis]) if a.tr[axis] <= b.tl[axis] else (b, b.tl[axis])
comp_max = lambda a,b,axis: (a, a.tr[axis]) if a.tr[axis] >= b.tl[axis] else (b, b.tl[axis])

sq = Square()
#print_square(sq)
min_x = reach_out(sq, comp_min, 0) # 0 is 'x' axis, 1 is 'y' axis
min_y = reach_out(grow(sq)[0], comp_min, 1) # have to steer left to choose correct branch
max_x = reach_out(sq, comp_max, 0)
max_y = reach_out(sq, comp_max, 1)

print "Area is %s" % ((max_x-min_x)*(max_y-min_y))
