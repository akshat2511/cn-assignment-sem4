// BELLMAN FORD ALGO
#include <iostream>
#include <unordered_map>
#include <vector>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max(); // Represents infinity

// Function to perform Distance Vector Routing
unordered_map<char, unordered_map<char, int>> distanceVectorRouting(
    const unordered_map<char, unordered_map<char, int>>& graph,
    const unordered_map<char, unordered_map<char, int>>& neighbors) {
    
    unordered_map<char, unordered_map<char, int>> distanceTables;

    // Initialize distance tables
    for (const auto& node : graph) {
        distanceTables[node.first][node.first] = 0; // Distance to itself is 0
        for (const auto& neighbor : node.second) {
            distanceTables[node.first][neighbor.first] = neighbor.second; // Directly connected neighbors
        }
    }

    bool updated;
    do {
        updated = false;
        // Update distance tables based on neighbors
        for (const auto& node : graph) {
            for (const auto& neighbor : neighbors.at(node.first)) {
                char neighborNode = neighbor.first;
                int costToNeighbor = neighbor.second;

                for (const auto& destination : graph) {
                    char destNode = destination.first;
                    int newDistance = distanceTables[node.first][neighborNode] + distanceTables[neighborNode][destNode];
                    if (newDistance < distanceTables[node.first][destNode]) {
                        distanceTables[node.first][destNode] = newDistance;
                        updated = true;
                    }
                }
            }
        }
    } while (updated);

    return distanceTables;
}

int main() {
    // Define the graph as an adjacency matrix
    unordered_map<char, unordered_map<char, int>> graph = {
        {'A', {{'A', 0}, {'B', 2}, {'C', 1}}},
        {'B', {{'A', 2}, {'B', 0}, {'C', 3}, {'D', 1}}},
        {'C', {{'A', 1}, {'B', 3}, {'C', 0}, {'D', 2}}},
        {'D', {{'B', 1}, {'C', 2}, {'D', 0}}}
    };

    // Define the neighbors for each node
    unordered_map<char, unordered_map<char, int>> neighbors = {
        {'A', {{'B', 2}, {'C', 1}}},
        {'B', {{'A', 2}, {'C', 3}, {'D', 1}}},
        {'C', {{'A', 1}, {'B', 3}, {'D', 2}}},
        {'D', {{'B', 1}, {'C', 2}}}
    };

    // Perform Distance Vector Routing
    unordered_map<char, unordered_map<char, int>> distanceTables = distanceVectorRouting(graph, neighbors);

    // Print distance tables
    for (const auto& node : distanceTables) {
        cout << "Distance table for node " << node.first << ":" << endl;
        for (const auto& entry : node.second) {
            cout << "To " << entry.first << ": " << entry.second << endl;
        }
        cout << endl;
    }

    return 0;
}
