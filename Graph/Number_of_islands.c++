#include <iostream> 
#include <vector> 

using namespace std;

vector<bool> DFS (vector<vector<int>> &graph, int start, vector<bool> &visited) {
    visited[start] = true;
    for (int i = 0; i < graph[start].size(); i++) {
        if (graph[start][i] == 1 && !visited[i]) {
            DFS(graph,i,visited);
        }
    }
    return visited;
}


int main() {
    vector<vector<int>> vec = {{1,1,0},{1,1,0},{0,0,1}};
    int start = 0;
    vector<bool> visited (vec.size(),false);
    int island_count = 0;
    for (int i = 0; i < vec.size(); i++) {
        if (!visited[i]) {
            island_count ++;
            DFS(vec,i,visited);
        }
    } 
    //DFS(vec,start,visited);
    for (auto it : visited){
        cout << it <<endl;
    }
    cout << "Count: "<< island_count << endl;
    return 0;

}