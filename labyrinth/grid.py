"""Classes for creating and working with grids"""
from typing 		 import Callable, Dict, Generic, Optional, Set, Tuple, TypeVar, Deque, List
from IPython.display import Markdown, display

import pandas as pd
import numpy as np
import random


# ~ Our modules
from labyrinth.graph  import Graph
from labyrinth.cell   import Cell

import labyrinth.utils as utils


class Grid() : 
	def __init__(self, width: int = 10, height: int = 10) -> None:
		"""Initialize a Grid."""
		self._width  = width
		self._height = height

		self._symbols    = {}
		self._graph      = Graph()
		self._grid       = []
		self._grid_cells = {}

		self._src  = Cell()
		self._dest = Cell()


	@property
	def width(self) -> int:
		"""Return the width (number of columns) of the grid."""
		return self._width


	@property
	def height(self) -> int:
		"""Return the height (number of rows) of the grid."""
		return self._height


	@property
	def symbols(self) -> Dict[str, str] : 

		"""Return the symbols of the grid """
		return self._symbols

	@property
	def src(self) -> Cell : 

		"""Return the `source` cell of the grid """
		return self._src

	@property
	def dest(self) -> Cell : 

		"""Return the `destination` cell of the grid """
		return self._dest


	@property
	def graph(self) -> Graph:
		"""Return the graph representation underlying this grid."""
		return self._graph


	@property
	def grid(self) -> List[List[str]]:
		"""Return the graph representation underlying this grid."""
		return self._grid


	@property
	def grid_cells(self) : #-> Dict[tuple(int,int), Cell]:
		"""Return the graph representation underlying this grid."""
		return self._grid_cells


	def set_symbols(self, wall : str = "#", move : str = " ", src : str = "X", dest : str = "E") -> None : 

		self._symbols["wall"] 	   = wall
		self._symbols["move"] 	   = move
		self._symbols["src"]  	   = src
		self._symbols["dest"] 	   = dest


	def set_dimensions(self, height : int = 10, width : int = 10) -> None : 

		self._height = height
		self._width  = width



	def load_grid_from_file(self, grid_fn) : 
		"""Parse grid from given .csv file"""
		self._grid = pd.read_csv(grid_fn, header = None)
		self._grid = self._grid.fillna(" ")
		self._grid = self._grid.values.tolist()


	def load_generated_grid(self,  algorithm_generate : str = "binary", 
								   width  : int = 10 , 
								   height : int = 10, 
								   p      : float = 0.1 ) -> None: 
		"""https://python.plainenglish.io/maze-generation-algorithms-with-matrices-in-python-i-33bc69aacbc4"""

		n = 1
		grid = np.random.binomial(n,p, size = (width, height))


		# -------------------------------------------------------------------------------- #
		# 1.fix first row and last column to avoid digging outside the maze external borders
		first_row = grid[0]
		first_row[first_row == 1] = 0
		grid[0] = first_row

		for idx in range(1, height):
			grid[idx, height - 1] = 1


		# -------------------------------------------------------------------------------- #
		# 2. generates a square maze (size*size) with the binary tree technique

		if algorithm_generate == "binary"       : grid = self.load_binary_grid(grid, width, height)
		elif algorithm_generate == "sidewinder" : grid = self.load_sidewinder_grid(grid, width, height)

		# -------------------------------------------------------------------------------- #
		# 3. Set a (src) and a (dst)
		i, j   = self.construct_start_end_indices(width, height)
		ii, jj = self.construct_start_end_indices(width, height)




		grid[i, j]   = self._symbols["src"]
		grid[ii, jj] = self._symbols["dest"]


		self._grid = grid


	def construct_start_end_indices(self, width  : int = 10 , height : int = 10) : 

		i = np.random.randint(0, width * 3)
		j = np.random.randint(1, height * 3 - 1) if (i == 0 or i == width * 3 - 1) else np.random.choice([0, height * 3 - 1])

		return i, j


	def load_binary_grid(self, grid : np.ndarray, width  : int = 10 , height : int = 10) -> np.ndarray :

		output_grid    = np.empty([width * 3, height * 3],dtype = str)
		output_grid[:] = '#'

		i, j = 0, 0


		while i < width:
			w = i * 3 + 1

			while j < height:
				k = j*3 + 1

				toss             = grid[i,j]
				output_grid[w,k] = self._symbols["move"]

				if toss == 0 and k + 2 < height * 3:
					output_grid[w, k + 1] = self._symbols["move"]
					output_grid[w, k + 2] = self._symbols["move"]


				if toss == 1 and w - 2 >=0:
					output_grid[w - 1, k] = self._symbols["move"]
					output_grid[w - 2, k] = self._symbols["move"]

				j += 1
			i += 1
			j = 0

		return output_grid



	def load_sidewinder_grid(self, grid : np.ndarray, width  : int = 10 , height : int = 10) -> np.ndarray :

		output_grid    = np.empty([width * 3, height * 3],dtype = str)
		output_grid[:] = '#'

		i, j = 0, 0


		while i < width:
			previous_l = []
			w = i * 3 + 1

			while j < height:
				k = j*3 + 1

				toss             = self._grid[i,j]
				output_grid[w,k] = self._symbols["move"]

				if toss == 0 and k + 2 < height * 3:

					output_grid[w, k + 1] = self._symbols["move"]
					output_grid[w, k + 2] = self._symbols["move"]
					previous_l.append(j)

				if toss == 1:
					# it's impossible to carve outside after preprocessing look back, choose a random cell
					if self._grid[i,j-1] == 0:
					# reaching from 0 mandatory to be sure that previous_l has at least one element
					# if we are coming from a list of previous cells, choose one and...
						r = rd.choice(previous_l)
						k = r * 3 + 1

					# ...just carve north
					# this just carve north if this is the first element of the row (1 element loop)
					output_grid[w - 1,k] = self._symbols["move"]
					output_grid[w - 2,k] = self._symbols["move"]
					previous_l           = []

				j += 1
			i += 1
			j = 0

		return output_grid
 

	def process_grid(self) -> None : 

		self._height = len(self._grid)
		self._width  = len(self._grid[0])

		for row in range(self._width): 
			for col in range(self._height) : 
				
				"""Enumeration of the directions allowed for movement within a grid.
				N = (-1, 0)
				S = (+1, 0)
				E = (0, +1)
				W = (0, -1)

				"""

				cell1  = self.add_cell_and_vertex(row, col)
				cell2S = self.add_cell_and_vertex(row + 1, col)
				cell2N = self.add_cell_and_vertex(row - 1, col)
				cell2E = self.add_cell_and_vertex(row, col + 1)
				cell2W = self.add_cell_and_vertex(row, col - 1)


				self._graph.add_edge(cell1, cell2S)
				self._graph.add_edge(cell1, cell2N)
				self._graph.add_edge(cell1, cell2E)
				self._graph.add_edge(cell1, cell2W)



	def check_valid_grid_coords(self,  row : int, col : int) -> bool :
		"""Check #1 : True if this coords (row, col) are inside the dimensions of the grid """
		return False if row < 0 or row >= self._width or col < 0 or col >= self._height else True

	def check_already_cell(self, row : int, col : int) -> bool :
		"""Check #2 : Returns True if this (row, col) is already a cell of the grid"""
		return True if (row, col) in self.grid_cells else False


	def add_cell_and_vertex(self, row : int, col : int) -> Cell :

		if not self.check_valid_grid_coords(row,col) : return None

		if self.check_already_cell(row, col) : return self.grid_cells[(row,col)]

		"""Add the given cell to this grid. Add the cell as vertex in graph if it is not a wall """

		cell_idx = (row * self._width) + col
		coords   = (row, col, cell_idx)
		cell     = Cell(*coords)

		# 1. add cell to the grid

		self.add_cell(cell) 

		# 2. check if cell is (source, destination)

		self.add_cell_src(cell, row, col)
		self.add_cell_dest(cell, row, col)

		# 3. add cell to the graph as vertex if not a wall

		if self._grid[row][col] != self._symbols["wall"] : 

			self._graph.add_vertex(cell)

		else : 

			coords = (-1, -1, -1)
			cell = Cell(*coords)

		return cell
				

	def add_cell(self, cell : Cell) -> None  :
		"""Add the given cell to this grid."""

		coordinates = cell.coordinates
		self._grid_cells[coordinates] = cell


	def add_cell_src(self, cell : Cell, row : int, col : int) -> None: 
		"""Check (and set) if the given cell if the `source` cell and"""
		if self._grid[row][col] == self._symbols["src"] :  self._src = cell

	def add_cell_dest(self, cell : Cell,  row : int, col : int) -> None: 
		"""Check (and set) if the given cell if the `destinatin` cell"""

		if self._grid[row][col] == self._symbols["dest"] :  self._dest = cell



	#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-#
	# 		       VISUALIZATIONS              #
	#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-#

	def visualize_grid(self, grid : List[List[str]]) :
		"""Visualize `grid` list of lists"""
		utils.pprint_list(grid)


	def visualize_grid_path(self, grid : List[List[str]], path : List[Cell]) -> None : 
		"""
			⬇️ ⬆️ ➡️ ⬅️
		"""

		if path  == [] :
			msg = "𝑵𝑶 𝑷𝑨𝑻𝑯"
			utils.pprint(msg) 
			return 

		else : 

			prev_v = path[1]
			for v in path[2: ] : 

				i , j  = v.x, v.y 
				ii, jj = prev_v.x , prev_v.y

				if (i, j) == (ii + 1, jj)  : grid[ii][jj] = "⬇"
				if (i, j) == (ii , jj + 1) : grid[ii][jj] = "⮕"
				if (i, j) == (ii - 1, jj)  : grid[ii][jj] = "⬆"
				if (i, j) == (ii, jj - 1)  : grid[ii][jj] = "⬅"

				prev_v = v

			self.visualize_grid(grid)



	
	





