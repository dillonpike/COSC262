"""An incomplete Huffman Coding module, for use in COSC262.
   Richard Lobb, April 2021.
   Completed by Dillon Pike, 2 May 2021.
"""
import re
from heapq import *

HAS_GRAPHVIZ = True
try:
    from graphviz import Graph
except ModuleNotFoundError:
    HAS_GRAPHVIZ = False

class Node:
    """Represents an internal node in a Huffman tree. It has a frequency count,
       minimum character in the tree, and left and right subtrees, assumed to be
       the '0' and '1' children respectively. The frequency count of the node
       is the sum of the children counts and its minimum character (min_char)
       is the minimum of the children min_chars.
    """
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.count = left.count + right.count
        self.min_char = min(left.min_char, right.min_char)

    def __repr__(self, level=0):
        return ((2 * level) * ' ' + f"Node({self.count},\n" +
            self.left.__repr__(level + 1) + ',\n' +
            self.right.__repr__(level + 1) + ')')

    def is_leaf(self):
        return False

    def plot(self, graph):
        """Plot the tree rooted at self on the given graphviz graph object.
           For graphviz node ids, we use the object ids, converted to strings.
        """
        graph.node(str(id(self)), str(self.count)) # Draw this node
        if self.left is not None:
            # Draw the left subtree
            self.left.plot(graph)
            graph.edge(str(id(self)), str(id(self.left)), '0')
        if self.right is not None:
            # Draw the right subtree
            self.right.plot(graph)
            graph.edge(str(id(self)), str(id(self.right)), '1')
            
    def __lt__(self, other):
        if self.count == other.count:
            return self.min_char < other.min_char
        else:
            return self.count < other.count    


class Leaf:
    """A leaf node in a Huffman encoding tree. Contains a character and its
       frequency count.
    """
    def __init__(self, count, char):
        self.count = count
        self.char = char
        self.min_char = char

    def __repr__(self, level=0):
        return (level * 2) * ' ' + f"Leaf({self.count}, '{self.char}')"

    def is_leaf(self):
        return True

    def plot(self, graph):
        """Plot this leaf on the given graphviz graph object."""
        label = f"{self.count},{self.char}"
        graph.node(str(id(self)), label) # Add this leaf to the graph
        
    def __lt__(self, other):
        if self.count == other.count:
            return self.min_char < other.min_char
        else:
            return self.count < other.count


class HuffmanTree:
    """Operations on an entire Huffman coding tree.
    """
    def __init__(self, root=None):
        """Initialise the tree, given its root. If root is None,
           the tree should then be built using one of the build methods.
        """
        self.root = root
        
    def create_mapping(self):
        """Creates a mapping of binary strings for each leaf."""
        self.mapping = {}
        self._create_mapping(self.root, '')
        
    def _create_mapping(self, current, string):
        if current.is_leaf():
            self.mapping[current.char] = string
        else:
            self._create_mapping(current.left, string+'0')
            self._create_mapping(current.right, string+'1')
        
    def encode(self, text):
        """Return the binary string of '0' and '1' characters that encodes the
           given string text using this tree.
        """
        self.create_mapping()
        binary = ''
        for char in text:
            binary += self.mapping[char]
        return binary
        
    def decode(self, binary):
        """Return the text string that corresponds the given binary string of
           0s and 1s
        """
        text = ''
        node = self.root
        for bit in binary:
            if bit == '0':
                node = node.left
            else:
                node = node.right
            if node.is_leaf():
                text += node.char
                node = self.root        
        return text

    def plot(self):
        """Plot the tree using graphviz, rendering to a PNG image and
           displaying it using the default viewer.
        """
        if HAS_GRAPHVIZ:
            g = Graph()
            self.root.plot(g)
            g.render('tree', format='png', view=True)
        else:
            print("graphviz is not installed. Call to plot() aborted.")

    def __repr__(self):
        """A string representation of self, delegated to the root's repr method"""
        return repr(self.root)

    def build_from_freqs(self, freqs):
        """Define self to be the Huffman tree for encoding a set of characters,
           given a map from character to frequency.
        """
        self.root = None
        heap = []
        for char, freq in freqs.items():
            heappush(heap, Leaf(freq, char))
        while len(heap) > 1:
            left = heappop(heap)
            right = heappop(heap)
            heappush(heap, Node(left, right))
        self.root = heappop(heap)

    def build_from_string(self, s):
        """Convert the string representation of a Huffman tree, as generated
           by its __str__ method, back into a tree (self). There are no syntax
           checks on s so it had better be valid!
        """
        s = s.replace('\n', '')  # Delete newlines
        s = re.sub(r'Node\(\d+,', 'Node(', s)
        self.root = eval(s)


def main():
    """ Demonstrate defining a Huffman tree from its string representation and
        printing and plotting it (if plotting is enabled on your machine).
    """
    tree = HuffmanTree()
    tree_string = """Node(42,
      Node(17,
        Leaf(8, 'b'),
        Leaf(9, 'a')),
      Node(25,
        Node(10,
          Node(5,
            Leaf(2, 'f'),
            Leaf(3, 'd')),
          Leaf(5, 'e')),
        Leaf(15, 'c')))
    """
    tree.build_from_string(tree_string)
    #print(tree)
    #tree.plot()
    
    # Or you can build the tree directly
    tree2 = HuffmanTree(Node(
      Node(
        Leaf(8, 'b'),
        Leaf(9, 'a')),
      Node(
        Node(
          Node(
            Leaf(2, 'f'),
            Leaf(3, 'd')),
          Leaf(5, 'e')),
        Leaf(15, 'c'))))
    #print(tree2)
    #tree2.plot()
    
    print(tree2.decode('0110011100'))
    print(tree.encode('adcb'))
    
    # The example from the notes
    freqs = {'a': 9,
             'b': 8,
             'c': 15,
             'd': 3,
             'e': 5,
             'f': 2}
    tree = HuffmanTree()
    tree.build_from_freqs(freqs)
    print(tree)    
    
main()