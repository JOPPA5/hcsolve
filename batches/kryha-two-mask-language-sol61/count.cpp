#include <iostream>
#include <vector>
#include <array>
#include <string>
#include <algorithm>
using namespace std;using cpp_int=unsigned __int128;
string dec(cpp_int x){string s;do{s+=char(48+x%10);x/=10;}while(x);reverse(s.begin(),s.end());return s;}
int mod(int x){return (x%26+26)%26;}
int main(){int n;cin>>n;vector<int>d(52),delta(n),c(104),p(n+1);for(auto&x:d)cin>>x;for(auto&x:delta)cin>>x;for(int i=1;i<104;i++)c[i]=c[i-1]+d[(i-1)%52];for(int i=0;i<n;i++)p[i+1]=mod(p[i]+delta[i]);if(p[n])return 1;cpp_int total=0;for(int a0=0;a0<52;a0++)for(int b0=0;b0<52;b0++){array<cpp_int,2704>prev{},cur{},sum{};prev[0]=1;for(int s=1;s<n;s++){for(int a=0;a<52;a++)for(int b=0;b<52;b++){int k=a*52+b;sum[k]=prev[k];if(a)sum[k]+=sum[k-52];if(b)sum[k]+=sum[k-1];if(a&&b)sum[k]-=sum[k-53];}cur.fill(0);for(int a=s;a<=52-(n-s);a++)for(int b=s;b<=52-(n-s);b++)if(mod(c[b0+b]-c[a0+a]-c[b0]+c[a0])==p[s])cur[a*52+b]=sum[(a-1)*52+b-1];prev.swap(cur);}cpp_int t=0;for(auto&v:prev)t+=v;if(t!=0){cout<<a0<<' '<<b0<<' '<<dec(t)<<'\n';total+=t;}}cerr<<"TOTAL "<<dec(total)<<'\n';}
