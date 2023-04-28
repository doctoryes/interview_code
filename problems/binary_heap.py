
from enum import Enum

## Binary heap - insert & extract minimum value

class HeapType(Enum):
    """
    Enumeration of sorted binary heap types.
    """
    MIN = 1
    MAX = 2

class HeapNode():
    def __init__(self, value):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value

    def __repr__(self):
        return f"HeapNode({self.value})"

class BinaryHeap():

    SPACE_PER_LEVEL = 5

    def __init__(self, type):
        self.root = None
        self.type = type

    def _print_tree(self, node, level):
        if node == None:
            return " " * (level * self.SPACE_PER_LEVEL) + f"--\n"
        s = self._print_tree(node.right, level + 1)
        s += " " * (level * self.SPACE_PER_LEVEL) + str(node.value) + "\n"
        s += self._print_tree(node.left, level + 1)
        return s

    def __str__(self):
        return self._print_tree(self.root, 0)

    def _find_bottom_left_insertion_node(self, node):
        """
        DFS to find bottom-most, left-most node with an empty left/right child.
        """
        if node.left is None:
            return node
        else:
            return self._find_bottom_left_insertion_node(node.left)

        if node.right is None:
            return node
        else:
            return self._find_bottom_left_insertion_node(node.right)

    def _find_insertion_node(self, node):
        """
        BFS to find bottom-most node with an empty left/right child.
        """
        nodes = [node]
        while True:
            curr_node = nodes.pop(0)
            if curr_node.left is None or curr_node.right is None:
                return curr_node
            else:
                nodes.extend((curr_node.left, curr_node.right))

    def _bubble_up(self, node):
        """
        Bubble up a node until it's in the correctly ordered place in the tree.
        1) Compare the node's value with its parent's value.
        2) If in the correct order, stop.
        3) If not, swap the element with its parent and go to 1).
        """
        if node.parent is None:
            return

        if (self.type == HeapType.MIN and node.parent.value > node.value) or \
           (self.type == HeapType.MAX and node.parent.value < node.value):
            # Swap the parent and child nodes.
            tmp = node.parent.value
            node.parent.value = node.value
            node.value = tmp
            self._bubble_up(node.parent)

    def insert(self, value):
        """
        Insertion is O(log n).
        """
        new_node = HeapNode(value)

        if self.root is None:
            # First insertion is a special-case.
            # Insert node as root - then no more work to do.
            self.root = new_node
            return

        # Traverse down the tree to the bottom level to find the left-most open space.
        insert_node = self._find_insertion_node(self.root)
        if insert_node == None:
            # Tree is currently perfect - every inserted node has 0 or 2 children.
            # In other words,
            #     - all leaf nodes are at the same level, and
            #     - that level has the maximum number of nodes
            # So just find the lowest, left-most node.
            insert_node = self._find_bottom_left_insertion_node(self.root)

        new_node.parent = insert_node

        # Always insert in the left position before the right position.
        if insert_node.left is None:
            insert_node.left = new_node
        elif insert_node.right is None:
            insert_node.right = new_node

        self._bubble_up(new_node)

    def remove_top_value(self):
        return None


#print(self.root,self.root.left,self.root.right,self.root.left.left,self.root.left.right,self.root.right.left,self.root.right.right)




