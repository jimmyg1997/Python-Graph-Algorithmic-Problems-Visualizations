# 🌐 Python-Graph-Algorithmic-Problems-Visualizations


## 1. Getting Started
The package is not currently available on PyPI or any other Python package repository. The easiest way to install it is to clone the GitHub repository and install it from source.

### Prerequisites
* [Python 3.7](https://www.python.org/downloads/) or newer
* [Git](https://git-scm.com/)
* [Make](https://www.gnu.org/software/make/)



### Installation Instructions
Run the following commands in a shell (a UNIX-like environment is assumed):

```
$ git clone git@github.com:jimmyg1997/Python-Graph-Algorithmic-Problems-Visualizations/
$ cd Python-Graph-Algorithmic-Problems-Visualizations/
$ make install
```
The package does not have any dependencies besides Python itself. If you wish to sandbox your installation inside a virtual environment, you may choose to use [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) or a similar utility to do so.

When successfully installed, the following programs will be available and placed on your `PATH`. See the Usage section below for details about how to use these programs.

* **labyrinth**






## 2. Concept and Contents

This is a project that explores algorithmic graph theory by visiting some of known **graph algorithmic problems** and **visual solutions**. The main goal is to systematically present essnetial **key examples** that highlight efficients algorithms in a visual representation. Most of the key techniques from these algorithms have already found applications in optimization, machine learning and statistics.
 
### Agenda

| | Program | Problem Solved | Algorithms Used|
|:-:|:-:|:-:|:-:|
| **#1** | Labyrinth | Shortest Path (undirected, unweighted) |• **Grid Generation** : {binary, sidewinder}</br> • **Shortest Path** : {bfs, dfs}|


## 3. Usage

At any time, you can use the `-h` or `--help` flags to see a summary of options that the program accepts.

### Program #1 - Labyrinth
```
$ labyrinth -h
usage:labyrinth [-h] [-s SYMBOLS] [-f GRID_FN] [-ag {binary,sidewinder}] [-d DIMENSIONS] [-p BINARY_PCT] [-ap {dfs,bfs}]

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

Typical usage is `labyrinth -ag <algorithm_generation> -d <dimensions>`, where `<algorithm_generation>` can be `binary`, `sidewinder` and `<dimensions>` is a string like 10x10 describing the dimensions of the maze to generate (width x height). The program will generate a random maze of the given size and print an ASCII representation of the maze to the console

*Example*
```
labyrinth -s "# 𝐗𝐄" -ag binary -d 6x6 -p 0.9 -ap bfs
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
|    ✅ 𝘀𝘁𝗲𝗽 𝟭 : Constructing (1) Grid (2) Graph      |
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
|    ✅ 𝘀𝘁𝗲𝗽 𝟮 : Find shortest path (undirected, unweighted)      |
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
|    ✅ 𝘀𝘁𝗲𝗽 𝟯 : Visualize shortest path if existing      |
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
 #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
 #                    ⇣  ⇠  ⇠  ⇠  ⇠  ⇠  ⇠  ⇠  ⇠  ⇠  #
 #     #  #     #  #  ⇣  #  #     #  #     #  #  ⇡  #
 #     #  #     #  #  ⇣  #  #     #  #     #  #  ⇡  #
 #     #  #     #  #  ⇣  #  #     #  #     #  #  ⇡  𝐗
 #     #  #     #  #  ⇣  #  #     #  #     #  #     #
 #     #  #     #  #  ⇣  #  #     #  #     #  #     #
 #     #  #     #  #  ⇣  #  #     #  #     #  #     #
 #     #  #  #  #  #  ⇣  #  #     #  #     #  #     #
 #     #  #  #  #  #  ⇣  #  #     #  #     #  #     #
 #     #  #  ⇣  ⇠  ⇠  ⇠  #  #     #  #     #  #     #
 #  #  #  #  ⇣  #  #     #  #     #  #     #  #     #
 #  #  #  #  ⇣  #  #     #  #     #  #     #  #     #
 #  ⇣  ⇠  ⇠  ⇠  #  #     #  #     #  #     #  #     #
 #  ⇣  #  #     #  #     #  #     #  #     #  #     #
 𝐄  ⇠  #  #     #  #     #  #     #  #     #  #     #
 #     #  #     #  #     #  #     #  #     #  #     #
 #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

```

## 4. References

This project owes a massive debt of gratitude to the following resources : 

### Program #1 - Labyrinth
* Maze Grid Generation
  1. [Series of articles on maze generation](https://weblog.jamisbuck.org/2011/2/7/maze-generation-algorithm-recap) featured on [Jamis Buck's blog](https://weblog.jamisbuck.org/). The step-by-step breakdown of various algorithms, along with simple diagrams and animations showing how the algorithms work, were invaluable in creating my own adaptations of these algorithms. 
  2. [Wikipedia - Maze Generation](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
  3. [Pymazes Github repo](https://github.com/antigones/pymazes)
 * Maze Shortest path
   1. The [article on maze-solving algorithms](https://kidscodecs.com/maze-solving-algorithms/) on the website of Beanz magazine also came in handy for understanding the concept of the "junction graph" and using tree traversal to solve mazes.
   2. [Wikipedia - Maze Solving Algorithm](https://en.wikipedia.org/wiki/Maze_solving_algorithm)

