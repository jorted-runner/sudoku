"""
Given a square grid of N x N with 0s and 1s where 1 represents an open cell and 0 a blocked one, find a path from the top-left cell to the bottom-right cell, moving only right or down.

Input:
The first line contains the integer N.
The next N lines contain N integers (0 or 1) each.

Output:
Print "YES" and the N x N path matrix showing the route using 1s.
If no path exists, print "NO".

Constraints:
1 <= N <= 10
"""

# Check Down
def check_down(maze, x, y):
    if not y <= len(maze) - 1:
        return False
    elif maze[x][y] == 1:
        return True

# Check Right
def check_right(maze, x, y):
    if not x <= len(maze) - 1:
        return False
    elif maze[x][y] == 1:
        return True

def solve_maze(maze, x=0, y=0, path_matrix=None):
    if path_matrix is None:
        path_matrix = [[0 for _ in range(len(maze))] for _ in range(len(maze))]

    # If out of bounds or blocked
    if x >= len(maze) or y >= len(maze) or maze[x][y] == 0:
        return False

    # Mark current cell
    path_matrix[x][y] = 1

    # If goal reached
    if x == len(maze) - 1 and y == len(maze) - 1:
        print("YES")
        for row in path_matrix:
            print(' '.join(map(str, row)))
        return True

    # Explore right
    if solve_maze(maze, x + 1, y, path_matrix):
        return True

    # Explore down
    if solve_maze(maze, x, y + 1, path_matrix):
        return True

    path_matrix[x][y] = 0
    return False
            
def start_maze(maze):
    if not solve_maze(maze):
        print("NO")




    
