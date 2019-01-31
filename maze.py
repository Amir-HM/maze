# make random matrix with walls and free spaces
import random, pprint

def make_maze(size, lvl, st):
    # make a matrix with random ints
    matrix = [[random.randint(0,10) for row in range(size)] for col in range(size)]
    # loop through the matrix
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            # if element is > lvl = a free space
            if matrix[row][col] > lvl:
                matrix[row][col] = '.' # . = free space
                # else element is a wall
            else:
                matrix[row][col] = '|'
    return matrix
# call our function to make a Maze
maze = make_maze(10, 2, [0,0])
# pprint.pprint(maze)
# print(maze[0][1])
 
matrix[0][0] = "S"
matrix[-1][-1] = "E"
# find all edges for node N
def find_edges(matrix, node):
    x,y = node
    edges = []
    length = len(matrix)
    for x,y in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y - 1), (x - 1, y + 1):
        if 0 <= x < length and 0 <= y < length:
            # check if matrix[x][y] is a free space
            if matrix[x][y] == '.':
                edges.append([x, y])
    return edges
# print(find_edges(maze, [0,0]))


def bfs(maze, node):
    stack = [[node]]
    explored = []
    goal = [len(maze)-1, len(maze)-1]
    while stack:
        # FIFO
        path = stack.pop(-1)
        node = path[-1]
        # check if we have searched path before
        if node not in explored:
            explored.append(node)
            # layer one connections to node
            edges = find_edges(maze, node)
            for edge in edges:
                new_path = list(path)
                new_path.append(edge)
                stack.append(new_path)
                if edge == goal:
                    for x,y in new_path:
                        maze[x][y] = 'X'
                    return maze
    return ('no path found')
pprint.pprint(bfs(maze, (0,0)))
