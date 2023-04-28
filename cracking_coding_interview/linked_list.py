

class Node():
	def __init__(self, data, next):
		self.data = data
		self.next = next


class SingleLinkedList():
	def __init__(self):
		self.head = None

	def size(self):
		size = 0
		curr = self.head
		while curr:
			size += 1
			curr = curr.next
		return size

	def append(self, data):
		new = Node(data, None)
		last = self.head
		while last and last.next:
			last = last.next
		if last:
			last.next = new
		else:
			# Empty list - add new head node.
			self.head = new

	def delete(self, data, all=False):
		"""
		Deletes first node set to value equal to data.
		If all is True, deletes *all* nodes set to value equal to data.
		"""
		last = None
		curr = self.head
		while curr:
			if curr.data == data:
				# Delete this node.
				if last:
					last.next = curr.next
				else:
					# This node is the first one.
					self.head = curr.next
				if not all:
					break
			last = curr
			curr = curr.next

		




