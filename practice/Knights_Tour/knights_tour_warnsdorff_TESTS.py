from knights_tour_warnsdorff import solve


def test_knights_tour():
    for size in [5, 6, 7, 8]:
        print(f"Testing board size {size}x{size}")
        board = [[0 for _ in range(size)] for _ in range(size)]
        solve(0, 0, board)
        print("\n")


if __name__ == "__main__":
    test_knights_tour()
