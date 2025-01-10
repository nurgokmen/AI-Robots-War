# AI Robots War

AI Robots War is a Python project that simulates a grid-based map where autonomous robots navigate using pathfinding algorithms. The project calculates the shortest paths and evaluates traversal costs between robots using A* Search, **Uniform Cost Search (UCS)**, and **Depth-First Search (DFS)**.

# Features

**_Map Parser_**: Reads a map file (map.txt) and identifies grid details and robot positions.

**_Pathfinding_**: Implements the A* algorithm to find the shortest path between any two points.

**_Graph Construction_**: Builds a graph of robots with the shortest path costs as edges.

**Search Algorithms**:

_Uniform Cost Search (UCS)_ to determine the optimal traversal route for all robots.
_Depth-First Search (DFS)_ for alternative exploration.

# Usage
-Map File (map.txt)_: Create a file that represents the grid map. Robots are represented by A, B, C, etc., and passable cells by 1. Impassable cells are 0.

**Example**:
```
1,1,1,0
1,A,1,1
1,0,1,B
```

**Run the Script**

Execute the script using Python:
```
python astar.py
```
**Output**:

Displays the grid matrix and robot positions.
Calculates and prints shortest paths and costs between robots.
Outputs results of UCS and DFS.

**Example Output**
For a map:
```
1,1,1,0
1,A,1,1
1,0,1,B
```

The output might include:
```
Matrix:
[[1 1 1 0]
 [1 1 1 1]
 [1 0 1 1]]
```
```
Robot Positions: {'A': (1, 1), 'B': (2, 3)}
```
```
Graph with shortest paths:
{'A': {'B': 4}, 'B': {'A': 4}}
```
```
UCS Path and Cost: ['A', 'B', 'A'] 8
DFS Path and Cost: ['A', 'B', 'A'] 8
```
**Requirements**

- Python 3.x
- Required Libraries: numpy

**Install dependencies using**:

```
pip install numpy
```

**Project Structure**

<ins>astar.py</ins>: Main script containing map parsing, A*, UCS, and DFS implementations.
<ins>map.txt</ins>: Input file defining the map layout.

# Algorithms

<ins>A*</ins>:

Heuristic-based algorithm for shortest pathfinding.
Combines cost-to-come (g) and cost-to-go (h) to evaluate paths.

<ins>UCS</ins>:

Explores all nodes with the lowest cumulative cost.
Ensures the optimal solution.

<ins>DFS</ins>:

Explores as deep as possible along each branch before backtracking.

# Future Enhancements
Add support for diagonal movements.
Include graphical visualization of robot paths and map.

# Contributions
Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request.

**License**
This project is open-source and available under the MIT License. See the LICENSE file for details.

