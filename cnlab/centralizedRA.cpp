#include <bits/stdc++.h>
#define inf 1000
using namespace std;

class router {
public:
  vector<int> distance;
  vector<int> from;
  router() {
    distance.resize(21,inf);
    from.resize(21,-1);
  }
};

int main() {
  router routers[20];
  for(int i = 0;i<20;i++) {
    routers[i].distance[i] = 0;
    routers[i].from[i] = i;
  }

  int number_of_routers;
  cout<<"Enter the number of routers: ";
  cin>>number_of_routers;

  vector<vector<int>> cost_matrix(number_of_routers+1,vector<int>(number_of_routers+1,inf));
  int u = 0,v = 0,w = 0;
  while(u != -1) {
    cout<<endl<<"Enter source router: ";
    cin>>u;
    if(u==-1)
    break;
    cout<<endl<<"Enter destination router: ";
    cin>>v;
    cout<<endl<<"Enter the cost: ";
    cin>>w;
    if(u != -1) {
      cost_matrix[u][v] = w;
      cost_matrix[v][u] = w; // Assume bidirectional links
    }
  }

  // Centralized Link State Algorithm
  vector<bool> visited(number_of_routers+1, false);
  vector<int> min_dist(number_of_routers+1, inf);
  vector<int> parent(number_of_routers+1, -1);

  int src = 1; // Assume the first router is the source
  min_dist[src] = 0;

  for(int i = 1; i <= number_of_routers; i++) {
    int u = -1;
    for(int j = 1; j <= number_of_routers; j++) {
      if(!visited[j] && (u == -1 || min_dist[j] < min_dist[u])) {
        u = j;
      }
    }

    visited[u] = true;

    for(int v = 1; v <= number_of_routers; v++) {
      if(cost_matrix[u][v] != inf && min_dist[u] + cost_matrix[u][v] < min_dist[v]) {
        min_dist[v] = min_dist[u] + cost_matrix[u][v];
        parent[v] = u;
      }
    }
  }

  // Print the routing table
  for(int i = 1; i <= number_of_routers; i++) {
    cout<<endl<<"For router "<<i<<endl;
    for(int j = 1; j <= number_of_routers; j++) {
      cout<<j<<"th Node via "<<parent[j]<<" with cost "<<min_dist[j]<<endl;
    }
  }

  return 0;
}
