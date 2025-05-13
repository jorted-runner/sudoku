chess_board = [[0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],]

def print_board():
    for i in range(8):
        for j in range(8):
            print(chess_board[i][j], end=" ")

        print("\n")

def get_possibilities(x, y):
    pos_x = (2, 1, 2, 1, -2, -1, -2, -1)
    pos_y = (1, 2, -1, -2, 1, 2, -1, -2)
    possibilities = []
    for i in range(8):
        if x + pos_x[i] >= 0 and x + pos_x[i] <=7 and y + pos_y[i] >= 0 and y + pos_y[i] <= 7 and chess_board[x + pos_x[i]][y + pos_y[i]] == 0:
            possibilities.append([x + pos_x[i], y + pos_y[i]])

    return possibilities

def place_knight(x, y, num):
    chess_board[x][y] = num

def solve(x, y):
    if x >= 0 and x <= 7 and y >= 0 and y <= 7:
        place_knight(x, y, 1)
        counter = 2
        for i in range(63):
            possibilities = get_possibilities(x, y)
            minimum = possibilities[0]
            for pos in possibilities:
                if len(get_possibilities(pos[0], pos[1])) <= len(get_possibilities(minimum[0], minimum[1])):
                    minimum = pos
            x = minimum[0]
            y = minimum[1]
            place_knight(x, y, counter)
            counter += 1
        print_board()
    else:
        print("Invalid Starting Position")

solve(7, 7)
