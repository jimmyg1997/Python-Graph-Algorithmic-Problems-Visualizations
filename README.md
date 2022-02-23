# 🌐 Python-Graph-Algorithmic-Problems-Visualizations


## Getting Started
The package is not currently available on PyPI or any other Python package repository. The easiest way to install it is to clone the GitHub repository and install it from source.

### Prerequisites
* [Python 3.7](https://www.python.org/downloads/) or newer
* [Git](https://git-scm.com/)


## Concept and Contents

This is a project that explores algorithmic graph theory by visiting some of the **graph algorithmic problems** and offer some **visual solutions**. The main goal is to systematically present essnetial key examples that highlight efficients algorithms. Most of the key techniques from these algorithms have already found applications in optimization, machine learning and statistics.
 
### AGENDA

| Real Example | Problem Solved | Algorithms Used|
|:-:|:-:|:-:|
| Labyrinth | Shortest Path (undirected, unweighted) | Grid Generation (binary, sidewinder) / Shortest Path (bfs, dfs)|




## Usage

At any time, you can use the `-h` or `--help` flags to see a summary of options that the program accepts.

```
$ maze -h
usage: __main__.py [-h] [-s SYMBOLS] [-f GRID_FN] [-ag {binary,sidewinder}] [-d DIMENSIONS] [-p BINARY_PCT] [-ap {dfs,bfs}]

Parse or generate labyrinth and find exit paths using different algorithms

optional arguments:
  -h, --help            show this help message and exit
  
  -s SYMBOLS, --symbols SYMBOLS
                        Give the 4 symbols in the following order : Wall->Move->Start->End
                        
  -f GRID_FN, --grid_fn GRID_FN
                        [Grid][Method#1 Parsing] Give the name of the csv file for the grid
                        
  -ag {binary,sidewinder}, --algorithm_generate {binary,sidewinder}
                        [Grid][Method#2 Generation] The algorithm to generate the grid labyrinth
                        
  -d DIMENSIONS, --dimensions DIMENSIONS
                        [Grid][Method#2 Generation] Give width / height of the generated grid
                        
  -p BINARY_PCT, --binary_pct BINARY_PCT
                        [Grid][Method#2 Generation] Give ghe percentage of the biomial geration
                        
  -ap {dfs,bfs}, --algorithm_shortest_path {dfs,bfs}
                        The algorithm to find the path in a labyrinth
```
