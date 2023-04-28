
from linked_list import SingleLinkedList


def setup_list():
	x = SingleLinkedList()
	x.append(4)
	x.append([66,77,88])
	x.append({'color': 'blue', 'length': 9})
	return x	

def test_append():
	x = setup_list()
	assert(x.size() == 3)

def test_delete_first():
	x = setup_list()
	x.delete(4)	
	assert(x.size() == 2)

def test_delete_last():
	x = setup_list()
	x.delete({'color': 'blue', 'length': 9})
	assert(x.size() == 2)
