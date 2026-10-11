#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
#include <string>
#include <random>
#include <map>
#include <cmath>
using namespace std;mt19937 rng(3503852);int H[26][26]={};int steps[]={7,6,7,5,6,7,6,8,6,10,5,6,5,7,6,5,9};
vector<int> projection(const vector<int>&O){vector<int>N(26);for(int c=0;c<26;c++)for(int d=0;d<26;d++)N[(O[c]-d+26)%26]+=H[c][d];return N;}
int concentration(const vector<int>&N){int z=0;for(int n:N)z+=n*n;return z;}
int main(int argc,char**argv){ifstream in(argv[1]);string ct;in>>ct;int phase=stoi(argv[2]),sign=stoi(argv[3]),nRestart=argc>4?stoi(argv[4]):3000;int shift=0;for(int i=0;i<ct.size();i++){H[ct[i]-'a'][shift]++;shift=(shift+sign*(steps[(phase+2*i)%17]+steps[(phase+2*i+1)%17])+26)%26;}map<vector<int>,int>top;int maxsc=0;for(int r=0;r<nRestart;r++){vector<int>O(26);iota(O.begin(),O.end(),0);shuffle(O.begin(),O.end(),rng);vector<int>N=projection(O);int sc=concentration(N),best=sc;vector<int>bk=O;for(int it=0;it<10000;it++){int a=rng()%26,b=rng()%26;int delta[26],change=0;for(int t=0;t<26;t++){delta[t]=H[a][(O[b]-t+26)%26]+H[b][(O[a]-t+26)%26]-H[a][(O[a]-t+26)%26]-H[b][(O[b]-t+26)%26];change+=2*N[t]*delta[t]+delta[t]*delta[t];}float temp=.1+70*(1.0-(it%2000)/2000.0);if(change>=0||uniform_real_distribution<float>(0,1)(rng)<exp(change/temp)){swap(O[a],O[b]);for(int t=0;t<26;t++)N[t]+=delta[t];sc+=change;}if(sc>best){best=sc;bk=O;}}int offset=bk[0];for(int&x:bk)x=(x-offset+26)%26;top[bk]=best;maxsc=max(maxsc,best);if(top.size()>300){auto worst=min_element(top.begin(),top.end(),[](auto&a,auto&b){return a.second<b.second;});top.erase(worst);}}vector<pair<int,vector<int>>>out;for(auto&[k,sc]:top)out.push_back({sc,k});sort(out.rbegin(),out.rend());for(auto&[sc,k]:out){cout<<sc<<" ";for(int c:k)cout<<c<<",";cout<<endl;}}
