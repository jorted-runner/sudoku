#include <iostream>
#include <list>
#include <unordered_set>

using namespace std;

list<int> NR_solve_maze(list<int> maze[], int start, int finish) {
    unordered_set<int> visited;
    list<int> path;

    path.push_back(start);
    int currentPoint = start;
    visited.insert(currentPoint);

    while (!path.empty() && path.back() != finish) { 
        list<int>::iterator iter = maze[currentPoint].begin();
        bool foundOutlet = false;

        while (iter != maze[currentPoint].end() && !foundOutlet) {
            if (visited.count(*iter) == 0) {
                foundOutlet = true;
            } else {
                iter++;
            }
        }

        if (foundOutlet) {
            path.push_back(*iter);
            visited.insert(*iter);
        } else {
            path.pop_back();
        }
        if (!path.empty()) {
            currentPoint = path.back();
        } else {
            return list<int>(); // No valid path found
}
    }
    return path;
}

bool R_solve_maze(list<int> maze[], int start, int finish, unordered_set<int>& visited, list<int>& path) {
    if (start == finish) {
        path.push_front(start);
        return true;
    }

    visited.insert(start);
    for (int neighbor : maze[start]) {
        if (visited.count(neighbor) == 0) {
            if (R_solve_maze(maze, neighbor, finish, visited, path)) {
                path.push_front(start);
                return true;
            }
        }
    }
    return false;
}

list<int> R_solve_maze(list<int> maze[], int start, int finish) {
    unordered_set<int> visited;
    list<int> solution_path;
    R_solve_maze(maze, start, finish, visited, solution_path);
    return solution_path;
}

int main() {
    list<int> sample_maze[9];

    sample_maze[0].push_back(1);
    sample_maze[0].push_back(3);

    sample_maze[1].push_back(0);
    sample_maze[1].push_back(2);

    sample_maze[2].push_back(1);

    sample_maze[3].push_back(0);
    sample_maze[3].push_back(4);
    sample_maze[3].push_back(6);

    sample_maze[4].push_back(3);
    sample_maze[4].push_back(5);
    sample_maze[4].push_back(7);

    sample_maze[5].push_back(4);

    sample_maze[6].push_back(3);

    sample_maze[7].push_back(4);
    sample_maze[7].push_back(8);

    sample_maze[8].push_back(7);
    
    list<int> solution = NR_solve_maze(sample_maze, 0, 8);

    list<int>::iterator iter;

    cout << "Path found by non-recursive solution: \n";
    for (iter = solution.begin(); iter != solution.end(); iter++) {
        cout << *iter << "\n";
    }

    list<int>solution2 = R_solve_maze(sample_maze, 0, 8);

    cout << "Path found by recursive solution: \n";
    for (iter = solution2.begin(); iter != solution2.end(); iter++) {
        cout << *iter << "\n";
    }

    return 0;
}