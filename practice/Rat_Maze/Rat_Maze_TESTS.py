import pytest
from Rat_Maze import start_maze

def test_solve_maze_path_exists(capfd):
    maze = [
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 1]
    ]
    expected_output = "YES\n1 1 0\n0 1 0\n0 1 1"
    start_maze(maze)
    out, _ = capfd.readouterr()
    assert out.strip() == expected_output.strip()

def test_solve_branching(capfd):
    maze = [
        [1, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1]
    ]
    expected_output = "YES\n1 1 0 0 0 0\n0 1 0 0 0 0\n0 1 1 1 0 0\n0 0 0 1 0 0\n0 0 0 1 1 0\n0 0 0 0 1 1"
    start_maze(maze)
    out, _ = capfd.readouterr()
    assert out.strip() == expected_output.strip()

def test_solve_maze_no_path(capfd):
    maze = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    start_maze(maze)
    out, _ = capfd.readouterr()
    assert "NO" in out

def test_solve_maze_single_cell(capfd):
    maze = [
        [1]
    ]
    expected_output = "YES\n1"
    start_maze(maze)
    out, _ = capfd.readouterr()
    assert out.strip() == expected_output.strip()

def test_solve_maze_blocked_start(capfd):
    maze = [
        [0, 1],
        [1, 1]
    ]
    start_maze(maze)
    out, _ = capfd.readouterr()
    assert "NO" in out

def test_solve_maze_blocked_end(capfd):
    maze = [
        [1, 1],
        [1, 0]
    ]
    start_maze(maze)
    out, _ = capfd.readouterr()
    assert "NO" in out