#strom = ['A', ['B', ['D'], ['E', ['F'], ['G']]], ['C']]
class Node:
	def __init__(self, key, children: list) -> None:
		self.key = key
		self.children = children

	def __repr__(self) -> str:
		return f'{self.key}'

class Tree:
	def __init__(self) -> None:
		self.root = Node(0, [None, None])

	def insert(self, key):
		pass

	def dfs(self, key):
		#Depth First Search
		pass

	def bfs(self, key):
		#Breadth First Search
		pass
