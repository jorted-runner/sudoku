
list<int> NR_solve_maze(list<int> maze[], int start, int finish) {
    unordered_set<int> visited;
    list<int> path;

    path.push_back(start);
    int currentPoint = start;
    visited.insert(currentPoint);

    while (path.back() != finish && path.empty() == false) {
        list<int>::iterator iter = maze[currentPoint].begin();
        bool foundOutlet = false;
        while ((iter != maze[currentPoint].end()) && (!foundOutlet)) {
            if (visited.count(*iter) == 0) {
                foundOutlet = true;
            }
            else {
                iter++;
            }
        }
        if (foundOutlet) {
            path.push_back(*iter);
            visted.insert(*iter);
        } 
        else {
            path.pop_back();
        }
        currentPoint = path.back();
    }
    return path;
}