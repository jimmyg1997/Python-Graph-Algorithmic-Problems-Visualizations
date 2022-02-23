"""Object-oriented representation of the mathematical concept of a graph."""
from typing 	 import Callable, Dict, Generic, Optional, Set, Tuple, TypeVar, Deque, List
from collections import defaultdict, deque
from queue 		 import SimpleQueue as Queue
import pandas as pd


# ~ Our modules
import labyrinth.utils as utils



T = TypeVar('T')


class Graph():
	"""Class representing a graph."""

	def __init__(self, ) -> None:

		self._adj = {}


	@property
	def vertex_set(self) -> Set[T]:
		"""Return a set of all vertices in this graph."""
		return set(self._adj.keys())


	@property
	def edge_set(self) -> Set[Tuple[T,T]]:
		"""Return a set of all edges in this graph."""
		edges = set()

		for v in self._adj.keys() : 
			neighbors = self.neighbors(v)

			for n in neighbors : 
				if (v,n) not in edges : 
					edges.add((v, n))
		return edges


	#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
	#                Graph Construction             #
	#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#


	def add_vertex(self, v : T) -> None : 
		"""Add the given vertex to this graph."""

		if not self.has_vertex(v) and self.is_valid_vertex(v) : 
			self._adj[v] = set()

		return 

	def has_vertex(self, v : T) -> bool : 
		"""Return a boolean indicating whether a vertex exists in the Graph"""

		return True if v in self._adj else False


	def is_valid_vertex(self, v : T) -> bool:

		return True if v.id != -1 else False



	def neighbors(self, v : T) ->  Set[T]:
		"""Return a set of all neighbors of the given vertex."""

		return self._adj[v] 


	#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
	#             2. Edges Operations               #
	#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#

	def add_edge(self, v : T, u : T) -> None : 
		"""Add an edge between the given vertices to this graph."""

		if self.has_vertex(u) and self.has_vertex(v) and not self.has_edge(v, u) : 
			self._adj[v].add(u)
			self._adj[u].add(v)

		return 

	def has_edge(self, v : T, u : T) -> bool : 
		"""Return a boolean indicating whether an edge exists between the given vertices in this graph."""
		return True if (u in self._adj[v] or v in self._adj[u]) else False



	#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
	#                 Graph Algorithms              #
	#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#

	def _dfs_util(self, src : T, dest : T, visited : Dict[T, bool], path : Set[T]) -> bool :
		""" Return a boolean indicating whether a path exists between the given vertices (s,t)"""

		# 1. Mark the current vertex as discovered
		visited[src] = True

		# 2. Include the current node in the path
		path.append(src)


		# 3. If destination vertex is found
		if src == dest : return True

		# 4. Do this for every neighbor (src, i)
		for n in self.neighbors(src) : 
			if not visited[n] : 
				# 4.1 Return true if the destination is found
				if self._dfs_util(n, dest, visited, path):
					return True

		# 5. Backtrack : Remove the current node from the path
		path.pop()

		# 6. Returns false if destination vertex is not reachable from src
		return False


	def depth_first_search(self, src : T, dest : T) -> Deque[T]: 

		visited = defaultdict(bool)
		path    = deque()
		isPath  = self._dfs_util(src, dest, visited, path)

		return path



	def _bfs_util(self, src : T, dest : T, visited : Dict[T, bool], ancestors : Dict[T, None], q : Queue[T]) -> None :

		# 1. Mark the current vertex as discovered
		visited[src] = True
		# 2. Include the current node in the path
		q.put(src)
		# 3. If destination vertex is found
		if src == dest : return True

		# 4. Do this for every neighbor (src, i)

		while not q.empty() : 

			v = q.get()

			for n in self.neighbors(v) : 
				if not visited[n] : 
					# 4.1 Return true if the destination is found
					q.put(n)
					visited[n]   = True
					ancestors[n] = v


	def breadth_first_search(self, src : T, dest : T) -> Queue[T]:  

		visited   = defaultdict(bool)
		ancestors = defaultdict(None)
		q         = Queue()

		self._bfs_util(src, dest, visited, ancestors, q)


		try 				  : path = self.build_path(src, dest, ancestors)
		except Exception as e : path = []


		return path

	def build_path(self, src : T, dest : T, ancestors : Dict[T, T]) -> List[T] : 
		it   = dest
		path = [ dest ]

		while it != src : 
			ancestor = ancestors[it]
			path.append(ancestor) 
			it = ancestor 

		return list(reversed(path))


	#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
	#           Visualizations Algorithms           #
	#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#

	





