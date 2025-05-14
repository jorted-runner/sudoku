def print_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=" ")

        print("\n")

def get_possibilities(x, y, board):
    pos_x = (2, 1, 2, 1, -2, -1, -2, -1)
    pos_y = (1, 2, -1, -2, 1, 2, -1, -2)
    possibilities = []
    for i in range(8):
        if x + pos_x[i] >= 0 and x + pos_x[i] <= len(board) - 1 and y + pos_y[i] >= 0 and y + pos_y[i] <= len(board) - 1 and board[x + pos_x[i]][y + pos_y[i]] == 0:
            possibilities.append([x + pos_x[i], y + pos_y[i]])

    return possibilities

def place_knight(x, y, num, board):
    board[x][y] = num

def solve(x, y, board):
    if x >= 0 and x <= len(board) -1 and y >= 0 and y <= len(board) -1:
        place_knight(x, y, 1, board)
        counter = 2
        for i in range((len(board) * len(board)) - 1):
            possibilities = get_possibilities(x, y, board)
            if not possibilities:
                print(f"No valid moves from ({x}, {y}) at step {counter}")
                break
            minimum = possibilities[0]
            for pos in possibilities:
                if len(get_possibilities(pos[0], pos[1], board)) <= len(get_possibilities(minimum[0], minimum[1], board)):
                    minimum = pos
            x = minimum[0]
            y = minimum[1]
            place_knight(x, y, counter, board)
            counter += 1
        if counter == (len(board) * len(board)) + 1:
            print_board(board)
            print("Full tour completed!")
        else:
            print("Tour incomplete.")
    else:
        print("Invalid Starting Position")
