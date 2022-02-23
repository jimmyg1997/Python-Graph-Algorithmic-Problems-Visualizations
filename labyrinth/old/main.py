#################################
##      Import Libraries       ##
#################################
import numpy as np              # linear algebra
import pandas as pd             # data processing, CSV file I/O ﴾e.g. pd.read_csv﴿
import sys
import random
import os
import warnings
import argparse
import logging
import joblib
import sys
from collections import defaultdict
from collections import deque
from functools import reduce
from IPython.display import Markdown, display
from pathlib import Path


#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
#                  UTILITY FUNCTIONS            #
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#

def initialize_logger() : 

	logs_fn = self.args.logs_fn

	with open(logs_fn, 'w'):
		logging.basicConfig(filename = logs_fn, level = logging.INFO, format = '%(message)s')



class Vertex() :
	def __init__(self, id = 0, x = 0, y = 0) :
		self.id = id
		self.x  = x 
		self.y  = y

	def get_arguments(self) : 
		return (self.x, self.y, self.id)




class Labyrinth() : 

	def __init__(self) :

		self.notgo_cells  = ["#"]
		self.go_cells     = [" ", "X", "E"] 

		self.maze          = None
		self.src           = None
		self.dest    	   = None
		self.vertices 	   = {}
		self.edges   	   = defaultdict(list)

		self.num_vertices  = 0
		self.num_edges     = 0


	#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
	#       1. Initializations &  Data Parsing      #
	#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#

	def parse_arguments(self) : 
		parser = argparse.ArgumentParser()
		parser.add_argument("--data_fn", type = str,  default = "data.csv", help = "Give the name of the csv file") 
		parser.add_argument("--logs_fn", type = str,  default = "logs.txt", help = "Give the name of the logger file") 
		
		self.args = parser.parse_args()


	def initialize_logger(self) : 

		logs_fn = self.args.logs_fn

		with open(logs_fn, 'w'):
			logging.basicConfig(filename = logs_fn, level = logging.INFO, format = '%(message)s')


	def load_labyrinth_file(self) : 

		data_fn = self.args.data_fn

		maze = pd.read_csv(data_fn, header = None)
		maze = maze.fillna(" ")

		logging.info(maze)

		self.maze  = maze.values.tolist()
		self.nrows = len(maze)
		self.ncols = len(maze[0])



	def load_labyrinth_graph(self) : 

		nrows, ncols = self.nrows, self.ncols
		maze         = self.maze

		for i in range(nrows) : 
			for j in range(ncols) : 

				node1 = Vertex(id = self.num_vertices, x = i, y = j)  


				if self.check_if_go(node1) : 

					node1 = self.add_vertex(node1)


					## 2.1 Check [i,j] -> [i, j+1]

					try : 

						node2 = Vertex(id = self.num_vertices, x = i, y = j + 1)  
						node2 = self.add_vertex(node2)
						self.add_edge(node1, node2)

					except Exception as e : pass


					## 2.2 Check [i,j] -> [i+1, j]
					try : 
						node2 = Vertex(id = self.num_vertices, x = i + 1, y = j)  
						node2 = self.add_vertex(node2)
						self.add_edge(node1, node2)

					except Exception as e : pass

					## 2.3 Check [i,j] -> [i, j-1]
					try : 
						node2 = Vertex(id = self.num_vertices, x = i, y = j - 1)  
						node2 = self.add_vertex(node2)
						self.add_edge(node1, node2)

					except Exception as e : pass

					## 2.4 Check [i,j] -> [i-1, j]
					try : 

						node2 = Vertex(id = self.num_vertices, x = i - 1, y = j)  
						node2 = self.add_vertex(node2)
						self.add_edge(node1, node2)

					except Exception as e : pass

					# print(self.vertices)

	def check_if_go(self, v) : 

		return True if self.maze[v.x][v.y] in self.go_cells else False

	#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
	#             2. Vetices Operations             #
	#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#

	def add_vertex(self, v) :
		"""
			Parameters
			----------
			v : Object of `Vertex` class

			Returns
			--------
			Object of `Vertex` class
		"""

		if self.check_if_go(v) : 


			if not self.contains_vertex(v) :

				self.vertices[(v.x, v.y)] = v
				self.num_vertices += 1
			
				if self.maze[v.x][v.y] == "X"   : self.src  = v
				elif self.maze[v.x][v.y] == "E" : self.dest = v


				self.show_vertex_message(v)

				return v 

			else : 


				return self.vertices[(v.x, v.y)]


	def contains_vertex(self, v) : 
		"""
			Parameters
			----------
			[*] v : Object of `Vertex` class

			Returns
			--------
			bool 
		"""

		if (v.x, v.y) in self.vertices : return True
		else                  		   : return False

	def show_vertex_message(self, vertex) :
		x, y, id = vertex.get_arguments()

		logging.info("⛰️[NODE udpate] Node (({},{}),ID={}) is added.".format(x, y, id ))
	

	def vertex_set(self):

		logging.info("\n")
		logging.info("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
		logging.info("|         Nodes List⬇️        |")
		logging.info("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

		for _, v in self.vertices.items() : 
			logging.info(" Node (({}, {}), {})".format(v.x, v.y, v.id))
		

	#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
	#               3. Edges Operations             #
	#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#

	def add_edge(self, u, v) :
		"""
			Usage
			-----
			[*] edges : dict of lists
						eg. {"0" : ["1", "5"], "1" : ["5", "6"], ... }

			Notes
			-----
			[*] We first check if v, u vertices exist and then if the edge (u,v) already exists 
		"""

		if self.contains_vertex(v) and self.contains_vertex(u) and not self.contains_edge(u,v) and not self.contains_loop(u,v) : 

			# self.edges_coords[(u.x, u.y)] += [ u ]
			# self.edges_coords[(v.x, v.y)] += [ v ]

			self.edges[u] += [ v ] 
			self.edges[v] += [ u ]	
			self.num_edges   += 2

			self.show_edge_message(u,v)


	def contains_loop(self, u,v) : 

		return True if u.id == v.id else False

	def contains_edge(self, u,v) :

		edge_u_v = v.id in list(x.id for x in  self.edges[u])
		edge_v_u = u.id in list(x.id for x in  self.edges[v])

		return True if edge_u_v or edge_v_u else False


	def show_edge_message(self, vertex1 , vertex2) : 

		x1, y1, id1 = vertex1.get_arguments()
		x2, y2, id2 = vertex2.get_arguments()

		logging.info("🪢[EDGE update] Edges between Nodes (({},{}),ID={})↔️(({},{}),ID={}) were added.".format(x1,y1,id1, x2,y2,id2 ))



	def neighbors(self, v) :

		neighbors = self.edges[v]

		return neighbors


	def degree(self, v) : 
		neighbors = self.neighbors(v)
		return len(neighbors)


	#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
	#             4. DFS ; Find path (s-t)          #
	#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#



class Solver() : 

	def __init__(self) : 

		## 
		self.path  = []



	def findPath_util(self, graph, src, dest, visited, path) : 


		# 1. Mark the current node as discovered
		visited[src.id] = True

		# 2. Include the current node in the path
		path.append(src)

		# 3. If destination vertex is found

		if src.id == dest.id : return True


		# 4. Do this for every neighbor (src, i)
		for neighbor in graph.neighbors(src) : 
			if not visited[neighbor.id] : 
				# 4.1 Return true if the destination is found
				if self.findPath_util(graph, neighbor, dest, visited, path):
					return True

		# 5. Backtrack : Remove the current node from the path
		path.pop()

		# 6. Returns false if destination vertex is not reachable from src
		return False
 

	def findPath(self, graph, src, dest) : 

		## CONFIGURATION
		visited = [False] * graph.num_vertices
		path    = deque()

		# 1. Find path
		isPath = self.findPath_util(graph, src, dest, visited, path)
		self.findPath_logging(isPath, src, dest, path)

		self.path = path


	def findPath_logging(self, isPath = True, src = None, dest = None, path = []) : 

		if isPath : 

			path_decoded = [v.get_arguments() for v in path]
			path_decoded = [((v[0], v[1]), v[2]) for v in path_decoded]

			logging.info("\n")
			logging.info("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
			logging.info("|   (DFS) Complete Path ⬇️ IDs : (({},{}),ID={}) - (({},{}),ID={})  |".format(src.x, src.y, src.id, dest.x ,dest.y, dest.id))
			logging.info("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
			

			for v in path_decoded :
				logging.info(v)

		else : 

			logging.info("Path between (({},{}), {}) - (({},{}),{}) does NOT exist. Result = None".format(src.x, src.y, src.id, dest.x ,dest.y, dest.id))
			logging.info(None)


	def printPathOnGraph(self, graph, path, src, dest) : 
		"""
			⬇️ ⬆️ ➡️ ⬅️
		"""

		maze   = graph.maze
		path = list(path)

		prev_v = path[1]
		for v in path[2: ] : 

			i , j  = v.x, v.y 
			ii, jj = prev_v.x , prev_v.y

			if (i, j) == (ii + 1, jj)  : maze[ii][jj] = "⬇"
			if (i, j) == (ii , jj + 1) : maze[ii][jj] = "⮕"
			if (i, j) == (ii - 1, jj)  : maze[ii][jj] = "⬆"
			if (i, j) == (ii, jj - 1)  : maze[ii][jj] = "⬅"

			prev_v = v

		

		maze = pd.DataFrame(maze)
		print(maze)



if __name__ == '__main__':

	labyrinth = Labyrinth()
	labyrinth.parse_arguments()
	labyrinth.initialize_logger()
	labyrinth.load_labyrinth_file()
	labyrinth.load_labyrinth_graph()
	labyrinth.vertex_set()

	labyrinth_solver = Solver()
	labyrinth_solver.findPath(graph = labyrinth, src = labyrinth.src, dest = labyrinth.dest)
	labyrinth_solver.printPathOnGraph(graph = labyrinth, path = labyrinth_solver.path, src = labyrinth.src, dest = labyrinth.dest)

	














