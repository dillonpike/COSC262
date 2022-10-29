from math import sqrt
    
class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Vector addition"""
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Vector subtraction"""
        return Vec(self.x - other.x, self.y - other.y)

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """The square of the length"""
        return self.dot(self)
    
    def __repr__(self):
        return f"Vec({self.x}, {self.y})"
    
    
def slow_solution(points):
    soln = (points[0], points[1])
    d = (points[0] - points[1]).lensq()
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = (points[i] - points[j]).lensq()
            if dist < d:
                soln = (points[i], points[j])
                d = dist
    return soln


def closest_pair(points_in):
    """Return the two closest points in the given point set.
       Precondition: points has a length >= 2.
       The return value is a tuple of two points of type Vec, sorted by
       their x values and then, if they are equal, their y values.
    """
    points = sorted(points_in, key=lambda p: (p.x, p.y))
    solution = (points[0], points[1])      # Current best point pair
    d = sqrt((points[1] - points[0]).lensq())   # Current best point-pair distance

    # Construct the frontier list, which is kept sorted by y
    # **** Insert some code here to create the initial frontier list with
    # **** the first two elements of the sorted point list.
    frontier = [points[0], points[1]]

    # Now sweep the line across the point set, starting the points[2]
    i = 2
    while d > 0 and i < len(points):
        p = points[i]
        # Remove points that no longer belong in the frontier
        # **** Insert code here
        j = 0
        while j < len(frontier):
            if sqrt((frontier[j] - p).lensq()) > d:
                j += 1
            else:
                break
        frontier = frontier[j:]
        
        # A full implementation would now check only frontier points with a y-value
        # within +/- d of p.y to see if any give a closer point pair. But for this
        # implementation which is using a simple Python list, you can just check
        # all frontier points.
        # *** Insert code here.
        for point in frontier:
            if sqrt((point - p).lensq()) < d:
                solution = (point, p)
                d = sqrt((point - p).lensq())
        
        frontier.append(p)
        i += 1
        
    return tuple(sorted(solution, key=lambda p: (p.x, p.y)))

point_tuples = [(45, 10), (20, 10), (55, 20),
    (35, 0), (0, 0), (10, 10), (30, 10),
    (35, 5), (10, -10), (20, -10)]
points = [Vec(*p) for p in point_tuples]
print(closest_pair(points))

from random import random, seed
N = 10000
SIZE = 1000000
seed(12345)
points = [Vec(int(SIZE * random()), int(SIZE * random())) for _ in range(N)]
print(closest_pair(points))