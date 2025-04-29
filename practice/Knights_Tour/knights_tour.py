"""
Knight's Tour
Given an N x N chessboard, place a knight on the board such that it visits every square exactly once.

Input:
A single integer N.

Output:
Print "YES" followed by the board with move numbers from 1 to N*N.
If a full tour is not possible, print "NO".

Constraints:
5 <= N <= 8
"""

def knights_tour(N, x=0, y=0, visited=None):
    if visited is None:
        visited = []

    if len(visited) == N*N:
        return True
    
    if not (0 <= x < N) or not (0 <= y < N):
        return False
    
    if (x,y) in visited:
        return False
    
    visited.append((x,y))

    if knights_tour(N, x+2, y+1, visited):
        return True
    if knights_tour(N, x+2, y-1, visited):
        return True
    if knights_tour(N, x-2, y+1, visited):
        return True
    if knights_tour(N, x-2, y-1, visited):
        return True
    if knights_tour(N, x+1, y+2, visited):
        return True
    if knights_tour(N, x+1, y-2, visited):
        return True
    if knights_tour(N, x-1, y+2, visited):
        return True
    if knights_tour(N, x-1, y-2, visited):
        return True
    
    visited.pop()
    return False

def place_knights(N):
    if not knights_tour(N):
        return False
    else:
        return True