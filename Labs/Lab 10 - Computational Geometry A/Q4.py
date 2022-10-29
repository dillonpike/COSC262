class Vec:
    """A simple vector in 2D. Also used as a position vector for points"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)
        
    def dot(self, other):
        return self.x * other.x + self.y * other.y
        
    def lensq(self):
        return self.dot(self)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
        
        
def signed_area(a, b, c):
    """Twice the area of the triangle abc.
       Positive if abc are in counter clockwise order.
       Zero if a, b, c are colinear.
       Otherwise negative.
    """
    p = b - a
    q = c - a
    return p.x * q.y - q.x * p.y

def is_on_segment(p, a, b):
    """Returns True if and only if the point p lies somewhere on the line 
       segment from a to b, including at either end.
    """
    return signed_area(p, a, b) == 0 and (p - a).lensq() <= (a - b).lensq() \
           and (p - b).lensq() <= (a - b).lensq()

a = Vec(1000, 2000)
b = Vec(0, 0)
p = Vec(500, 1000)
print(is_on_segment(p, a, b))

a = Vec(0, 0)
b = Vec(1000, 2000)
point_tuples = [
    (-1, -1),
    (-1, -2),
    (-1000, -2000),
    (0, 0),
    (1, 2),
    (500, 1000),
    (500, 1001),
    (500, 999),
    (1000, 2000),
    (1001, 2001),
    (1001, 2002),
    (2000, 4000)]
points = [Vec(p[0], p[1]) for p in point_tuples]
for p in points:
    print(p, is_on_segment(p, a, b))