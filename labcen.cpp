//write a centralized routing algorithm
// DIGIJSTRAS ALGORITHM

#include <iostream>
#include <unordered_map>
#include <vector>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max(); // Represents infinity

class Graph {
private:
    unordered_map<char, unordered_map<char, int>> adjList; // Adjacency list representation

public:
    // Function to add an edge to the graph
    void addEdge(char u, char v, int weight) {
        adjList[u][v] = weight;
        adjList[v][u] = weight; // Assuming undirected graph
    }

    // Function to perform centralized routing
    vector<char> centralizedRouting(char source, char destination) {
        unordered_map<char, int> distance; // Store shortest distance from source to all nodes
        unordered_map<char, char> previous; // Store previous node in shortest path

        // Initialize distance and previous arrays
        for (auto& pair : adjList) {
            distance[pair.first] = INF;
            previous[pair.first] = '\0';
        }
        distance[source] = 0;

        // Relax edges repeatedly
        for (int i = 0; i < adjList.size() - 1; ++i) {
            for (auto& pair : adjList) {
                char u = pair.first;
                for (auto& neighbor : pair.second) {
                    char v = neighbor.first;
                    int weight = neighbor.second;
                    if (distance[u] != INF && distance[u] + weight < distance[v]) {
                        distance[v] = distance[u] + weight;
                        previous[v] = u;
                    }
                }
            }
        }

        // Reconstruct the shortest path
        vector<char> path;
        char current = destination;
        while (current != '\0') {
            path.insert(path.begin(), current);
            current = previous[current];
        }

        return path;
    }
};

int main() {
    Graph graph;

    // Add edges to the graph
    graph.addEdge('A', 'B', 2);
    graph.addEdge('A', 'C', 1);
    graph.addEdge('B', 'C', 3);
    graph.addEdge('B', 'D', 1);
    graph.addEdge('C', 'D', 2);

    char source = 'A';
    char destination = 'D';

    vector<char> shortestPath = graph.centralizedRouting(source, destination);

    // Print the shortest path
    cout << "Shortest path from " << source << " to " << destination << ": ";
    for (char node : shortestPath) {
        cout << node << " ";
    }
    cout << endl;

    return 0;
}
