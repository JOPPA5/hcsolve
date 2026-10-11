#include <iostream>
#include <vector>
#include <array>
#include <algorithm>
using namespace std;
int mod26(int x){return (x%26+26)%26;}
int main(){
 int n;cin>>n;vector<int>d(52),delta(n),c(104),prefix(n+1);
 for(auto &x:d)cin>>x;for(auto &x:delta)cin>>x;
 for(int i=1;i<104;i++)c[i]=c[i-1]+d[(i-1)%52];
 for(int i=0;i<n;i++)prefix[i+1]=mod26(prefix[i]+delta[i]);
 if(prefix[n]!=0){cout<<"NO\n";return 0;}
 long fits=0;vector<pair<int,int>>first;
 for(int a0=0;a0<52;a0++)for(int b0=0;b0<52;b0++){
  vector<array<int,2704>>parent(n);array<int,2704>prev,cur;
  prev.fill(-1);prev[0]=0;
  bool alive=true;
  for(int step=1;step<n;step++){
   array<int,2704>best;best.fill(-1);
   for(int a=0;a<52;a++)for(int b=0;b<52;b++){
    int idx=a*52+b;
    if(prev[idx]>=0)best[idx]=idx;
    else if(a&&best[idx-52]>=0)best[idx]=best[idx-52];
    else if(b&&best[idx-1]>=0)best[idx]=best[idx-1];
   }
   cur.fill(-1);alive=false;
   for(int a=step;a<=52-(n-step);a++)for(int b=step;b<=52-(n-step);b++){
    int pred=best[(a-1)*52+b-1];
    if(pred>=0&&mod26(c[b0+b]-c[a0+a]-c[b0]+c[a0])==prefix[step]){
     cur[a*52+b]=pred;alive=true;
    }
   }
   parent[step]=cur;prev=cur;if(!alive)break;
  }
  if(!alive)continue;
  int end=-1;for(int i=0;i<2704;i++)if(prev[i]>=0){end=i;break;}
  if(end<0)continue;fits++;
  if(first.empty()){
   first.resize(n);for(int step=n-1;step>=1;step--){
    first[step]={(a0+end/52)%52,(b0+end%52)%52};end=parent[step][end];
   }first[0]={a0,b0};
  }
 }
 if(!fits){cout<<"NO\n";return 0;}
 cout<<"YES "<<fits<<"\n";for(auto [a,b]:first)cout<<a<<" "<<b<<"\n";
}
