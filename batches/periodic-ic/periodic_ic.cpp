#include <algorithm>
#include <array>
#include <cmath>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <random>
#include <vector>
using namespace std;
int main(int argc,char**argv){ifstream in(argv[1]);string ct;in>>ct;int T=stoi(argv[2]),S=stoi(argv[3]),restarts=stoi(argv[4]);vector<array<array<int,26>,26>>H(T);for(int i=0;i<ct.size();i++)H[i%T][ct[i]-'a'][(i/T*S)%26]++;mt19937 rng(521943);map<vector<int>,int>top;for(int rr=0;rr<restarts;rr++){vector<int>O(26);iota(O.begin(),O.end(),0);shuffle(O.begin(),O.end(),rng);vector<array<int,26>>N(T);int sc=0;for(int p=0;p<T;p++)for(int c=0;c<26;c++)for(int d=0;d<26;d++)N[p][(O[c]-d+26)%26]+=H[p][c][d];for(auto&v:N)for(int n:v)sc+=n*n;int best=sc;vector<int>bk=O;for(int it=0;it<10000;it++){int a=rng()%26,b=rng()%26;vector<array<int,26>>delta(T);int change=0;for(int p=0;p<T;p++)for(int j=0;j<26;j++){int d=H[p][a][(O[b]-j+26)%26]+H[p][b][(O[a]-j+26)%26]-H[p][a][(O[a]-j+26)%26]-H[p][b][(O[b]-j+26)%26];delta[p][j]=d;change+=2*N[p][j]*d+d*d;}double temp=.1+10*(1.-(it%2000)/2000.);if(change>=0||uniform_real_distribution<double>(0,1)(rng)<exp(change/temp)){swap(O[a],O[b]);for(int p=0;p<T;p++)for(int j=0;j<26;j++)N[p][j]+=delta[p][j];sc+=change;}if(sc>best){best=sc;bk=O;}}int off=bk[0];for(int&v:bk)v=(v-off+26)%26;top[bk]=best;if(top.size()>100){auto w=min_element(top.begin(),top.end(),[](auto&a,auto&b){return a.second<b.second;});top.erase(w);}}vector<pair<int,vector<int>>>out;for(auto&[k,v]:top)out.push_back({v,k});sort(out.rbegin(),out.rend());for(auto&[v,k]:out){cout<<v<<" ";for(int x:k)cout<<x<<",";cout<<endl;}}
