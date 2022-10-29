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

def is_strictly_convex(vertices):
    """Takes a list of three or more points, each of type Vec as in the lecture 
       notes, and returns True if and only if the vertices, taken in the given 
       order, define a strictly-convex counter-clockwise polygon, otherwise False.
    """
    n = len(vertices)
    for i in range(n):
        if not is_ccw(vertices[i%n], vertices[(i+1)%n], vertices[(i+2)%n]):
            return False
    return True

verts = [
    (0, 0),
    (100, 0),
    (100, 100),
    (0, 100)]
points = [Vec(v[0], v[1]) for v in verts]
print(is_strictly_convex(points))

verts = [
    (0, 0),
    (0, 100),
    (100, 100),
    (100, 0)]
points = [Vec(v[0], v[1]) for v in verts]
print(is_strictly_convex(points))

verts = [
    (0, 0),
    (100, 0),
    (100, 100),
    (90, 10)]
points = [Vec(v[0], v[1]) for v in verts]
print(is_strictly_convex(points))

verts = [
    (0, 0),
    (50, 0),
    (100, 0),
    (100, 100),
    (90, 10)]
points = [Vec(v[0], v[1]) for v in verts]
print(is_strictly_convex(points))