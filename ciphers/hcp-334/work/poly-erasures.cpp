#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <random>
#include <set>
#include <string>
#include <vector>
using namespace std;
float q[456976];
int transform(int c,int k,string f){if(c<0)return -1;if(f=="beaufort")return (k-c+26)%26;if(f=="porta")return c<13?13+(c+k)%13:(c-13-k+13)%13;return (c-k+26)%26;}
int main(int argc,char**argv){ifstream model(argv[1]);fill(begin(q),end(q),-4);string x;float v;while(model>>x>>v){int a=0;for(char c:x)a=a*26+c-'a';q[a]=v;}ifstream src(argv[2]);src>>x;vector<int>ct;for(char c:x)ct.push_back(c=='?'?-1:tolower(c)-'a');string family=argv[3];int lo=stoi(argv[4]),hi=stoi(argv[5]),restarts=stoi(argv[6]),steps=stoi(argv[7]),K=family=="porta"?13:26,N=ct.size();mt19937 rng(33461);auto win=[&](vector<int>&p,int a){int id=0;for(int j=a;j<a+4;j++){if(p[j]<0)return 0.f;id=id*26+p[j];}return q[id];};for(int w=lo;w<=hi;w++){vector<vector<int>>positions(w),wins(w);for(int i=0;i<N;i++)positions[i%w].push_back(i);for(int r=0;r<w;r++){set<int>s;for(int i:positions[r])for(int a=max(0,i-3);a<=min(i,N-4);a++)s.insert(a);wins[r]={s.begin(),s.end()};}float best=-1e9;vector<int>bk,bp;for(int restart=0;restart<restarts;restart++){vector<int>k(w),p(N);for(int&i:k)i=rng()%K;for(int i=0;i<N;i++)p[i]=transform(ct[i],k[i%w],family);float sc=0;for(int a=0;a+3<N;a++)sc+=win(p,a);for(int t=0;t<steps;t++){int r=rng()%w,old=k[r],nk=rng()%K;float before=0,after=0;for(int a:wins[r])before+=win(p,a);for(int i:positions[r])p[i]=transform(ct[i],nk,family);for(int a:wins[r])after+=win(p,a);float delta=after-before,temp=.15+4.*(1.-(t%3000)/3000.);if(delta>=0||uniform_real_distribution<float>(0,1)(rng)<exp(delta/temp)){k[r]=nk;sc+=delta;}else{for(int i:positions[r])p[i]=transform(ct[i],old,family);}if(sc>best){best=sc;bk=k;bp=p;}}}cout<<w<<" "<<best<<" ";for(int k:bk)cout<<k<<",";cout<<" ";for(int c:bp)cout<<(c<0?'?':char('a'+c));cout<<endl;}}
