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
      routers[u].distance[v] = w;
      routers[v].distance[u] = w;
      routers[u].from[v] = v;
      routers[v].from[u] = u;
    }
  }
  for(int i = 1;i<=number_of_routers;i++) {
    for(int j = 1;j<=number_of_routers;j++) {
      cost_matrix[i][j] = routers[i].distance[j];
    }
  }
  int count = 0;
  do{
    count = 0;
    for(int i = 1;i<=number_of_routers;i++) {
      for(int j = 1;j<=number_of_routers;j++) {
        for(int k = 1;k<=number_of_routers;k++) {
          if(routers[i].distance[j] > cost_matrix[i][k] + routers[k].distance[j]) {
            routers[i].distance[j] = routers[i].distance[k] + routers[k].distance[j];
            routers[i].from[j] = k;
            count++;
          }
        }
      }
    }
  } while(count != 0);

  for(int i = 1;i<=number_of_routers;i++) {
    cout<<endl<<"For router "<<i<<endl;
    for(int j = 1;j<=number_of_routers;j++) {
      cout<<j<<"th Node via "<<routers[i].from[j]<<" with cost "<<routers[i].distance[j]<<endl;
    }
  }
  return 0;
}