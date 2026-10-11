#include <iostream>
#include <vector>
#include <array>
#include <algorithm>
#include <cmath>
#include <queue>
#include <fstream>
#include <unordered_map>
#include <cstdint>
using namespace std;int mod(int x){return(x%26+26)%26;}using Node=pair<int,int>;struct Winner{double s;vector<Node>h;bool operator<(const Winner&o)const{return s>o.s;}};priority_queue<Winner>top;int n=23,a0,b0;vector<int>c(104),prefix(24);array<array<int,26>,23>H{};array<double,26>lp;vector<vector<Node>>layers;vector<Node>path;long long pathcount=0;vector<vector<char>>can;int ng=6,kzero;array<int,26>pin,outring;vector<string>texts_pair;unordered_map<uint64_t,double>model;uint64_t pw=1;
double profile(){double total=0;for(int q=0;q<2;q++){array<int,23>D{};for(int j=0;j<23;j++){int off=q?path[j].second:path[j].first;int anchor=q?b0:a0;D[j]=mod(c[anchor+off]-c[anchor]+(q?kzero:0));}uint64_t code=0;for(int i=0;i<texts_pair[q].size();i++){int v=pin[mod(outring[texts_pair[q][i]-'a']-D[i%23]-23*(i/23))];code=code*26+v;if(i>=ng)code-=uint64_t(pin[mod(outring[texts_pair[q][i-ng]-'a']-D[(i-ng)%23]-23*((i-ng)/23))])*pw*26;if(i>=ng-1){auto it=model.find(code);total+=it==model.end()?-ng:it->second;}}}return total;}

void dfs(int j,int a,int b){if(j==n){pathcount++;double s=profile();if(top.size()<100||s>top.top().s){auto abs=path;for(auto &v:abs){v.first=(v.first+a0)%52;v.second=(v.second+b0)%52;}top.push({s,abs});if(top.size()>100)top.pop();}return;}for(int k=0;k<(int)layers[j].size();k++){auto[x,y]=layers[j][k];if(x>a&&y>b&&can[j][k]){path[j]={x,y};dfs(j+1,x,y);}}}
int main(int argc,char**argv){ng=stoi(argv[1]);for(int i=0;i<ng-1;i++)pw*=26;ifstream mf(argv[2]);string word;double value;while(mf>>word>>value){uint64_t code=0;for(char ch:word)code=code*26+ch-'a';model[code]=value;}ifstream cfg(argv[3]);cfg>>kzero;for(int&x:outring)cfg>>x;for(int&x:pin)cfg>>x;texts_pair.resize(2);cfg>>texts_pair[0]>>texts_pair[1];vector<int>d(52),delta(23);for(auto&x:d)cin>>x;for(auto&x:delta)cin>>x;for(auto&x:lp)cin>>x;sort(lp.begin(),lp.end(),greater<double>());for(auto&r:H)for(auto&x:r)cin>>x;for(int i=1;i<104;i++)c[i]=c[i-1]+d[(i-1)%52];for(int j=0;j<23;j++)prefix[j+1]=mod(prefix[j]+delta[j]);for(a0=0;a0<52;a0++)for(b0=0;b0<52;b0++){layers.assign(n,{});can.assign(n,{});for(int j=1;j<n;j++)for(int a=j;a<=52-(n-j);a++)for(int b=j;b<=52-(n-j);b++)if(mod(c[b0+b]-c[a0+a]-c[b0]+c[a0])==prefix[j])layers[j].push_back({a,b});for(int j=n-1;j>0;j--){can[j].assign(layers[j].size(),0);for(int k=0;k<(int)layers[j].size();k++){if(j==n-1){can[j][k]=1;continue;}auto[a,b]=layers[j][k];for(int l=0;l<(int)layers[j+1].size();l++){auto[x,y]=layers[j+1][l];if(can[j+1][l]&&x>a&&y>b){can[j][k]=1;break;}}}}path.assign(n,{0,0});dfs(1,0,0);}
vector<Winner>w;while(top.size()){w.push_back(top.top());top.pop();}reverse(w.begin(),w.end());cout.precision(15);cout<<"COUNT "<<pathcount<<'\n';// paths stored need absolute anchors; fix below
for(auto&r:w){cout<<r.s;for(auto[a,b]:r.h)cout<<' '<<a<<' '<<b;cout<<'\n';}}
