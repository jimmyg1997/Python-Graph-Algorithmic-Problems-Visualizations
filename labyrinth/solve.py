"""Solve labyrinth using a depth-first search algorithm."""
from collections import defaultdict
from typing      import List, Tuple

# ~ Our modules
from labyrinth.graph import Graph
from labyrinth.grid  import Grid
from labyrinth.cell  import Cell

import labyrinth.utils as utils


class Solver() : 
	def __init__(self) -> None:
		"""Initialize a MazeSolver."""
		self.grid_cells = None
		self.grid       = Grid()
		self.graph      = Graph()
		self.src        = Cell()
		self.dest       = Cell()

		self.path       = []

	def construct_grid_symbols(self, symbols : str = "# XE") -> None : 

		symbols = list(symbols)

		symbol_wall 	 = symbols[0]
		symbol_move 	 = symbols[1]
		symbol_src  	 = symbols[2]
		symbol_dest 	 = symbols[3]


		self.grid.set_symbols(symbol_wall, symbol_move, symbol_src, symbol_dest)


	def construct_grid_dimensions(self, dimensions : str = "10x10") -> Tuple[int,int] :


		dims   = dimensions.split("x")
		height = int(dims[0])
		width  = int(dims[1])

		self.grid.set_dimensions(height,width)

		return (height, width)



	def construct_grid_and_graph(self,  
								 algorithm_generate : str = "binary", 
								 grid_fn            : str = "data.csv", 
								 dimensions         : str = "10x10",
								 p                  : float = 0.1) :
		"""Construct and return the (1) grid (2) the graph representing all junctions in the labyrinth."""

		utils.pprint(utils.MESSAGES["step1"])


		if algorithm_generate == "no" : 

			self.grid.load_grid_from_file(utils.data_dir + grid_fn)

		else : 

			height, width = self.construct_grid_dimensions(dimensions)
			self.grid.load_generated_grid(algorithm_generate, width, height, p)


		# elif algorithm_generate == "binary": 

		self.grid.process_grid()

		self.grid_cells = self.grid.grid_cells
		self.graph      = self.grid.graph
		self.src        = self.grid.src
		self.dest       = self.grid.dest

		self.grid.visualize_grid(grid = self.grid.grid)




	def find_graph_path(self, algorithm : str = "bfs") -> None :
		""" Calculate graph path by using the algorithm given """

		utils.pprint(utils.MESSAGES["step2"])

		src  = self.src 
		dest = self.dest


		if algorithm == "dfs"  :

			self.path = self.graph.depth_first_search(src, dest)

		elif algorithm == "bfs" : 

			self.path = self.graph.breadth_first_search(src, dest)



	def visualize_grid_path(self) -> None :
		""" Visualize the path on the given grid """

		utils.pprint(utils.MESSAGES["step3"])

		self.grid.visualize_grid_path(grid = self.grid.grid, path = self.path)




	def solve(self, 
			  symbols                 : str = "# SE", 
			  grid_fn                 : str = "data.csv", 
			  algorithm_generate      : str = "binary", 
			  dimensions              : str = "10x10", 
			  p                       : float = 0.1 ,  
			  algorithm_shortest_path : str = "bfs") -> None: 

		self.construct_grid_symbols(symbols)
		self.construct_grid_and_graph(algorithm_generate, grid_fn, dimensions, p)
		self.find_graph_path(algorithm_shortest_path)
		self.visualize_grid_path()
















