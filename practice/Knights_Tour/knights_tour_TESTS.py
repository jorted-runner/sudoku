import pytest
from knights_tour import knights_tour, place_knights

def test_knights_tour_works_for_small_N():
    assert place_knights(5) == True
    # assert place_knights(6) == True
    # assert place_knights(7) == True
    # assert place_knights(8) == True

def test_knights_tour_invalid_start():
    assert knights_tour(5, x = -1, y = -1) == False

def test_knights_tour_starts_at_0_0():
    assert place_knights(5) == True

def test_knights_tour_full_tour_possible():
    visited = []
    assert knights_tour(5, 0, 0, visited=visited)
    assert len(visited) == 25