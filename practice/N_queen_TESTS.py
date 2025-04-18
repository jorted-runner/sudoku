import pytest
from N_queen import N_Queens

def test_n_queens_valid_output():
    for N in range(1, 11):
        board = [[0 for _ in range(N)] for _ in range(N)]
        result = N_Queens(board, N)
        if N in [2, 3]:
            assert not result, f"N={N} should be impossible"
        else:
            assert result, f"N={N} should be possible"
            # Ensure exactly one queen per row and column
            for row in board:
                assert sum(row) == 1, f"Row has invalid queen count: {row}"
            for col in range(N):
                assert sum(board[row][col] for row in range(N)) == 1, f"Column {col} has invalid queen count"

def test_n_queens_impossible_cases():
    for N in [2, 3]:
        board = [[0 for _ in range(N)] for _ in range(N)]
        result = N_Queens(board, N)
        assert not result