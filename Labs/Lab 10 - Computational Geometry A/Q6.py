class Vec:
    """A simple vector in 2D. Also use for points (position vector)"""
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
        
        
def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise"""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
    # May want to throw an exception if area == 0
    return area > 0 

def intersecting(a, b, c, d):
    """Returns True if the line segment from a to b intersects the line
       segment from c to d, otherwise False.
    """
    return is_ccw(a, b, c) != is_ccw(a, b, d) and \
           is_ccw(c, d, a) != is_ccw(c, d, b)

a = Vec(0, 0)
b = Vec(100, 0)
c = Vec(101, 1)
d = Vec(101, -1)
print(intersecting(a, b, c, d))

a = Vec(0, 0)
b = Vec(100, 0)
c = Vec(99, 1)
d = Vec(99, -1)
print(intersecting(a, b, c, d))