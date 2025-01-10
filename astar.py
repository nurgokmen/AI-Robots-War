import numpy as np
from queue import PriorityQueue
import heapq
import itertools

def getmap(filename):
    grid = []
    robots = {}
    with open(filename, 'r') as file:
        rowi = 0
        for line in file:
            elements = line.strip().split(',')
            row = []
            for coli, value in enumerate(elements):
                if value in 'ABCD':
                    robots[value] = (rowi, coli)
                    row.append(1)
                else:
                    row.append(int(value))
            grid.append(row)
            rowi+= 1
    return np.array(grid), robots

def manhattan(x,y):#one of them is starting point othr is the goal point
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def astar(grid, start, end): #fn is the f(n) and gn is g(n)
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]# directions are considered as up, down right left because the robot can move to all four directions


    inf = float('inf')


    visited = set()
    origin = {} # origin is the first location
    gn = {(r, c): inf for r in range(rows) for c in range(cols)}
    gn[start] = 0
    fn = {(r, c): inf for r in range(rows) for c in range(cols)}
    fn[start] = manhattan(start, end)

    while fn:
        #this line selects the node with the minimum fn
        current = min(fn, key=fn.get)
        if current == end: #checking if the current node is the goal node
            path = []
            while current in origin:
                path.append(current)
                current = origin[current]
            path.append(start)
            return path[::-1] #reversing the path

        del fn[current]
        visited.add(current)

        #exploring neighbors in all four possible directions
        for r, c in directions:
            neighbor = current[0] + r, current[1] + c #getting the neighbors coordinates
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 1:
                tempg = gn[current] + 1
                if tempg < gn.get(neighbor,inf):
                    origin[neighbor] = current #taking this one as the best
                    gn[neighbor] = tempg
                    fn[neighbor] = gn[neighbor] + manhattan(neighbor, end) # since fn=gn + hn

    return []


def construct_graph(robots, matrix):##constructing the graph with the shortest values

    def astar2(matrix, start, end):
        path = astar(matrix, start, end)
        if path:
            return len(path) - 1
        return 0

    graph = {} # created an empty dictionary because we will keep the graph in a dictionary format just to access the distances and robots easier
    robot_keys = list(robots.keys())


    for robot in robot_keys:
        graph[robot] = {}

    #graph is filled with the shortest paths we have found
    #robot1 means the starting robot and robot 2 means the second robot which the starting visited
    for i in range(len(robot_keys)):
        for j in range(i + 1, len(robot_keys)):
            robot1 = robot_keys[i]
            robot2 = robot_keys[j]
            start = robots[robot1]
            end = robots[robot2]


            distance = astar2(matrix, start, end)
            graph[robot1][robot2] = distance
            graph[robot2][robot1] = distance

    return graph


def ucs(graph, start):

    frontier = PriorityQueue()
    frontier.put((0, [start]))  #path taken

    visited = set()
    best_cost = float('inf')
    best_path = None#initialized to none

    while not frontier.empty():
        cost, path = frontier.get()
        current = path[-1]


        if set(path) == set(graph.keys()) and current == start:
            if cost < best_cost:
                best_cost = cost
                best_path = path
            continue

        for next_node, travel_cost in graph[current].items():
            if next_node not in path or (len(path) == len(graph) and next_node == start):
                new_path = path + [next_node]
                new_cost = cost + travel_cost
                frontier.put((new_cost, new_path))

    return best_path, best_cost


def dfs(graph, start, path=None, cost=0):
    #initialize path
    if path is None:
        path = [start]

    current = path[-1]
    #initial setting
    if set(path) == set(graph.keys()) and current == start:
        return path, cost

    #calculte smallest cost and the path recursive
    for next_node, travel_cost in graph[current].items():
        if next_node not in path or (len(path) == len(graph) and next_node == start): #if the graph is not completed continue
            new_path = path + [next_node] #add letter to path
            new_cost = cost + travel_cost #add cost to total cost
            result_path, result_cost = dfs(graph, start, new_path, new_cost) #recursive call
            if result_path:  #if goes back to A starting point
                return result_path, result_cost

    return None, 0

if __name__== "__main__" :

    filename = 'map.txt'
    matrix, robots = getmap(filename)
    print("Matrix:")
    print(matrix)
    print("Robot Positions:", robots)


    all = sorted(list(robots.keys()))


    for i in range(len(all)):
        for j in range(i+ 1, len(all)):
            robot1 = all[i]
            robot2 = all[j]

            start = robots[robot1]
            end = robots[robot2]

            path = astar(matrix, start, end)

            distance = len(path) - 1
            print(f"{robot1},{robot2},{distance}")

    graph = construct_graph(robots, matrix)
    print("Graph with shortest paths:")
    print(graph)

    start_node = 'A'


    ucs_path, ucs_cost = ucs(graph, start_node)
    print("UCS Path and Cost:", ucs_path, ucs_cost)


    dfs_path, dfs_cost = dfs(graph, start_node)
    print("DFS Path and Cost:", dfs_path, dfs_cost)


