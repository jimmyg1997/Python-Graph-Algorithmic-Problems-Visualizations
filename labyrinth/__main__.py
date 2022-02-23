"""Entry point for the labyrinth program."""
from typing import List, Tuple
import argparse
import os
import sys

# ~ Our modules
from labyrinth.solve import Solver


class LabyrinthMain():
	"""Main class for the labyrinth program.""" 
	def __init__(self) -> None:
		parsed_args    = self.parse_args(sys.argv[1:])
		
		self.symbols                 = parsed_args.symbols
		self.grid_fn                 = parsed_args.grid_fn
		self.algorithm_generate      = parsed_args.algorithm_generate
		self.dimensions              = parsed_args.dimensions
		self.binary_pct              = parsed_args.binary_pct
		self.algorithm_shortest_path = parsed_args.algorithm_shortest_path # ALGORITHMS[parsed_args.algorithm]

	
	def parse_args(cls, args: list[str]) -> argparse.Namespace:
		"""Return a Namespace containing the program's configuration as parsed from the given arguments."""
		parser = argparse.ArgumentParser(description = "Parse or generate labyrinth and find exit paths using different algorithms")
		# parser.add_argument("-l", "--logs_fn", type = str,  default = "logs.txt", help = "Give the name of the logger file you want to store the result labyrinth") 
		
		parser.add_argument("-s", "--symbols", type = str,  default = "# XEU", 
							help = "Give the 4 symbols in the following order : Wall->Move->Start->End") 

		#*-*-*-*-*-*-* [1.1] Parsing *-*-*-*-*-*-*-*-#

		parser.add_argument("-f", "--grid_fn", type = str,  default = "grid.csv", 
							help = "[Grid][Method#1 Parsing] Give the name of the csv file for the grid") 
		
		#*-*-*-*-*-*-* [1.2] Generation *-*-*-*-*-*-*-*-#

		parser.add_argument("-ag", "--algorithm_generate",  choices = ["binary", "sidewinder"], default = "no", 
							help = "[Grid][Method#2 Generation] The algorithm to generate the grid labyrinth")

		parser.add_argument("-d", "--dimensions", type = str,  default = "10x10", 
							help = "[Grid][Method#2 Generation] Give width / height of the generated grid") 
		
		parser.add_argument("-p", "--binary_pct", type = float,  default = 0.2, 
							help = "[Grid][Method#2 Generation] Give ghe percentage of the biomial geration") 
		
		#*-*-*-*-*-*-* [2] Find path *-*-*-*-*-*-*-*-#
		parser.add_argument("-ap", "--algorithm_shortest_path", choices = ["dfs", "bfs"], default = "dfs", 
							help = "The algorithm to find the path in a labyrinth")

		return parser.parse_args(args)


	def run(self) -> None:
		"""Run the program."""
		symbols    		        = self.symbols
		grid_fn    		        = self.grid_fn
		algorithm_generate      = self.algorithm_generate
		dimensions              = self.dimensions
		binary_pct              = self.binary_pct
		algorithm_shortest_path = self.algorithm_shortest_path
		

		solver = Solver()
		solver.solve(symbols, grid_fn, algorithm_generate, dimensions, binary_pct, algorithm_shortest_path)


def main():
	"""Entry point for the 'labyrinth' program """
	LabyrinthMain().run()


if __name__ == '__main__':
	main()

