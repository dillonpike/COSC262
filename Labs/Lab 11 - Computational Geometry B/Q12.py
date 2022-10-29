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
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """The square of the length"""
        return self.dot(self)

    def __getitem__(self, axis):
        return self.x if axis == 0 else self.y

    def __repr__(self):
        """String representation of self"""
        return "({}, {})".format(self.x, self.y)
    
    def in_square(self, centre, size):
        """True iff this point (warning, not a vector!) lies within or on the
           bottom or left boundary of the square defined by centre and size."""
        bottom_left = Vec(centre.x - size / 2, centre.y - size / 2)
        top_right = Vec(centre.x + size / 2, centre.y + size / 2)
        return bottom_left.x <= self.x < top_right.x and bottom_left.y <= self.y < top_right.y
    
        

class QuadTree:
    """A QuadTree class for COSC262.
       Richard Lobb, May 2019
    """
    MAX_DEPTH = 20
    def __init__(self, points, centre, size, depth=0, max_leaf_points=2):
        self.centre = centre
        self.size = size
        self.depth = depth
        self.max_leaf_points = max_leaf_points
        self.children = []
        self.points = [p for p in points if p.in_square(centre, size)]
        if len(self.points) > max_leaf_points and depth < self.MAX_DEPTH:
            self.is_leaf = False
            for i in range(4):
                child_centre = Vec(centre.x + (-1) ** ((i >> 1 & 1) + 1) * size / 4, 
                                   centre.y + (-1) ** ((i & 1) + 1) * size / 4)
                child_size = size / 2
                child = QuadTree(self.points, child_centre, child_size, depth + 1, max_leaf_points)
                self.children.append(child)
        else:
            self.is_leaf = True

    def plot(self, axes):
        """Plot the dividing axes of this node and
           (recursively) all children"""
        if self.is_leaf:
            axes.plot([p.x for p in self.points], [p.y for p in self.points], 'bo')
        else:
            axes.plot([self.centre.x - self.size / 2, self.centre.x + self.size / 2],
                      [self.centre.y, self.centre.y], '-', color='gray')
            axes.plot([self.centre.x, self.centre.x],
                      [self.centre.y - self.size / 2, self.centre.y + self.size / 2],
                      '-', color='gray')
            for child in self.children:
                child.plot(axes)
        axes.set_aspect(1)
                
    def __repr__(self, depth=0):
        """String representation with children indented"""
        indent = 2 * self.depth * ' '
        if self.is_leaf:
            return indent + "Leaf({}, {}, {})".format(self.centre, self.size, self.points)
        else:
            s = indent + "Node({}, {}, [\n".format(self.centre, self.size)
            for child in self.children:
                s += child.__repr__(depth + 1) + ',\n'
            s += indent + '])'
            return s

import matplotlib.pyplot as plt
'''
points = [(1, 1), (99, 1), (1, 99), (99, 99), (49, 49), (51, 49), (49, 51), (51, 51)]
vecs = [Vec(*p) for p in points]
tree = QuadTree(vecs, Vec(50, 50), 100, max_leaf_points=1)
print(tree)

# Plot the tree, for debugging only
axes = plt.axes()
tree.plot(axes)
axes.set_xlim(0, 100)
axes.set_ylim(0, 100)
plt.show()
'''

points = [(1, 1), (99, 1), (1, 99), (99, 99),
         (49, 49), (51, 49), (49, 51), (51, 51),
         (60, 60), (70, 70), (80, 80), (90, 90)]
vecs = [Vec(*p) for p in points]
tree = QuadTree(vecs, Vec(50, 50), 100, max_leaf_points=1)
print(tree)

# Plot the tree, for debugging only
axes = plt.axes()
tree.plot(axes)
axes.set_xlim(0, 100)
axes.set_ylim(0, 100)
plt.show()

'''
points = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
          (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
          (3, 1), (3, 2), (3, 3), (3, 4), (3, 5)]
vecs = [Vec(*p) for p in points]
tree = QuadTree(vecs, Vec(10000000000/2, 10000000000/2), 10000000000, max_leaf_points=1)
print(tree)

# Plot the tree, for debugging only
axes = plt.axes()
tree.plot(axes)
axes.set_xlim(0, 10000000000)
axes.set_ylim(0, 10000000000)
plt.show()
'''