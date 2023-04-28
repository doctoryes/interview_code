
# Given a sorted (increasing order) array with unique integer elements, write an algorithm
# to create a binary search tree with minimal height.


class TreeNode():
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def children_full(self):
		"""
		Returns True if both child slots are filled, otherwise False.
		"""
		return not (self.left == None or self.right == None)


class BinaryTree():
	def _init_(self):
		self.root = None

	def _find_insert_node():
		"""
		Returns the first node with an empty child, searching left-to-right on bottom tree level.
		"""
		curr_level = [self.root]

		node = None
		while len(curr_level):
			node = curr_level.pop(0)
			# Keep track of the left-most node in the level.
			if not first_node_in_level:
				first_node_in_level = node
			if not node.children_full:
				# Found the lowest node with an empty child slot.
				return node
			curr_level.append(node.left)
			curr_level.append(node.right)
		# If exited loop without returning, then binary tree is fully complete.
		# Return the last node visited.
		return node


	def insert(self, value):
		"""
		Insert the value into the binary search tree - keep the binary tree complete.
		"""
		# Insert the new node in the bottom-most position, looking left-to-right on the bottom tree level.
		# Breadth-first search to find first node with empty left/right child.
		node_to_insert_child = _find_insert_node(self.root)

		new_node = TreeNode(value)
		if not node_to_insert_child.right:
			node_to_insert_child.right = new_node
		elif not node_to_insert_child.left:
			node_to_insert_child.left = new_node

		# While new child is less than parent, swap child with parent.
		
