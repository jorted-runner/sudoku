"""
Given a chess board having  cells, you need to place N queens on the board in such a way that no queen attacks any other queen.

Input:
The only line of input consists of a single integer denoting N.

Output:
If it is possible to place all the N queens in such a way that no queen attacks another queen, then print "YES" (without quotes) in first line, then print N lines having N integers. The integer in  line and  column will denote the cell  of the board and should be 1 if a queen is placed at  otherwise 0. If there are more than way of placing queens print any of them.

If it is not possible to place all N queens in the desired way, then print "NO" (without quotes).

Constraints:
1 <= N <= 10
"""

def is_attacked(x, y, board, N):
    # Check Row
    if 1 in board[x]:
        return True
    
    # Check Column
    for row in board:
        if row[y] == 1:
            return True
    
    # Check Diagonals
    p = x + 1
    q = y + 1
    # check down right
    while p < N and q < N:
        if board[p][q] == 1:
            return True
        p += 1
        q += 1

    p = x - 1
    q = y + 1
    # check up right
    while p >= 0 and q < N:
        if board[p][q] == 1:
            return True
        p -= 1
        q += 1

    p = x + 1
    q = y - 1
    # check down left
    while p < N and q >= 0:
        if board[p][q] == 1:
            return True
        
        p += 1
        q -= 1

        
    p = x - 1
    q = y - 1
    # check up left
    while p >= 0 and q >= 0:
        if board[p][q] == 1:
            return True
        
        p -= 1
        q -= 1


    return False
    
def N_Queens(board, N, row=0):
    if row == N:
        return True

    for col in range(N):
        if not is_attacked(row, col, board, N):
            board[row][col] = 1
            if N_Queens(board, N, row + 1):
                return True
            board[row][col] = 0

    return False