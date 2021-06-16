keys = []
children = []
parent = None
data = None

node1 = [keys, children, parent, data]

KEYS_INDEX = 0
CHILDREN_INDEX = 1
PARENT_INDEX = 2

def make_node(keys, children = None):
	node = [keys, children, None]
	if children is not None:
		for child in children:
			child[PARENT_INDEX] = node
	return node

def get_keys(node):
	return node[KEYS_INDEX]

def get_children(node):
	return node[CHILDREN_INDEX]

def get_parent(node):
	return node[PARENT_INDEX]

def is_leaf(node):
	return node[CHILDREN_INDEX] is None

def is_root(node):
	return node[PARENT_INDEX] is None

def get_n(node):
	return len(node[KEYS_INDEX])

def set_keys(node, keys):
	node[KEYS_INDEX] = keys

def set_children(node, children):
	if node[CHILDREN_INDEX] is not None:
		for child in node[CHILDREN_INDEX]:
			child[PARENT_INDEX] = None

	node[CHILDREN_INDEX] = children

	if children is not None:
		for child in children:
			child[PARENT_INDEX] = node


"""
# Vytvoření:
node1 = make_node([1, 3])
node2 = make_node([6])
node3 = make_node([12, 15, 16])

node4 = make_node([5, 10], [node1, node2, node3])

# Je rodič správný?
children = get_children(node4)
child1 = children[0]
parent1 = get_parent(child1)
parent1 is node4

# Nastavení klíčů:
set_keys(node4, [4, 10])

# Nastavení dětí:
node5 = make_node([13, 17])
set_children(node4, [node1, node2, node5])
children = get_children(node4)
child3 = children[2]
get_parent(child3)
"""