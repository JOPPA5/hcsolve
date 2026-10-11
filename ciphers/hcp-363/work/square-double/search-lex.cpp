#include <algorithm>
#include <array>
#include <cmath>
#include <cassert>
#include <fstream>
#include <iostream>
#include <numeric>
#include <queue>
#include <random>
#include <string>
#include <vector>
using namespace std;
mt19937 rng(610363);
float bi[26][26];vector<float> gram[6];
void load(string dir,string big){ifstream f(big);string s;float v;while(f>>s>>v)bi[s[0]-'a'][s[1]-'a']=v;for(int n=3;n<=5;n++){ifstream g(dir+"/model"+to_string(n)+".tsv");string tag;float floor;g>>tag>>floor;int total=1;for(int i=0;i<n;i++)total*=26;gram[n].assign(total,floor);while(g>>s>>v){int ix=0;for(char c:s)ix=ix*26+c-'a';gram[n][ix]=v;}}}
float language(const string&s){float sc=0,wt[]={0,0,0,.15,.4,.8};for(int n=3;n<=5;n++){int ix=0,pow=1;for(int j=1;j<n;j++)pow*=26;for(int i=0;i<(int)s.size();i++){if(i>=n)ix-=(s[i-n]-'a')*pow;ix=ix*26+s[i]-'a';if(i>=n-1)sc+=wt[n]*gram[n][ix];}}return sc;}
#include "frozen-lex.hpp"
vector<string>rows;int width=20;
string reorder(const string&s,const vector<int>&cols){string t;for(int c:cols)t+=s[c];return t;}
float colscore(const vector<int>&cols){float sc=0;for(auto&s:rows)sc+=language(reorder(s,cols));return sc;}
void mutate(vector<int>&k){int a=rng()%20,b=rng()%20;if(a>b)swap(a,b);switch(rng()%4){case 0:swap(k[a],k[b]);break;case 1:reverse(k.begin()+a,k.begin()+b+1);break;case 2:{int x=k[a];k.erase(k.begin()+a);k.insert(k.begin()+b,x);break;}default:{vector<int>block(k.begin()+a,k.begin()+b+1);k.erase(k.begin()+a,k.begin()+b+1);int dest=rng()%(k.size()+1);k.insert(k.begin()+dest,block.begin(),block.end());}}}
float boundary(const string&a,const string&b){string s=a.substr(a.size()-4)+b.substr(0,4);float sc=0,wt[]={0,0,0,.15,.4,.8};for(int n=3;n<=5;n++)for(int start=5-n;start<4;start++){int ix=0;for(int j=0;j<n;j++)ix=ix*26+s[start+j]-'a';sc+=wt[n]*gram[n][ix];}return sc;}
int main(int argc,char**argv){load(argv[1],argv[2]);loadLex(argv[1]);ifstream f(argv[3]);string ct;f>>ct;assert(ct.size()==400);for(int i=0;i<20;i++)rows.push_back(ct.substr(i*20,20));
float adj[20][20]{};for(int a=0;a<20;a++)for(int b=0;b<20;b++)for(auto&s:rows)adj[a][b]+=bi[s[a]-'a'][s[b]-'a'];auto scorebi=[&](const vector<int>&k){float sc=0;for(int i=0;i<19;i++)sc+=adj[k[i]][k[i+1]];return sc;};
float global=-1e9;vector<int>best;
for(int rep=0;rep<80;rep++){vector<int>k(20);iota(k.begin(),k.end(),0);shuffle(k.begin(),k.end(),rng);float sc=scorebi(k);for(int it=0;it<5000;it++){auto t=k;mutate(t);float ns=scorebi(t),temp=.5+20*(1.-(it%1000)/1000.);if(ns>sc||uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/temp)){k=t;sc=ns;}}sc=colscore(k);for(int it=0;it<25000;it++){auto t=k;mutate(t);float ns=colscore(t),temp=.5+80*pow(1.-(it%5000)/5000.,2);if(ns>sc||uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/temp)){k=t;sc=ns;}if(sc>global){global=sc;best=k;}}if(rep%10==0)cerr<<"restart="<<rep<<" within_rows="<<global<<" row0="<<reorder(rows[0],best)<<endl;}
vector<string>clean;for(auto&s:rows)clean.push_back(reorder(s,best));float edge[20][20];for(int a=0;a<20;a++)for(int b=0;b<20;b++)edge[a][b]=boundary(clean[a],clean[b])+2*(lex(clean[a]+clean[b])-lex(clean[a])-lex(clean[b]));
int total=1<<20;vector<float>dp(total*20,-1e9);vector<unsigned char>prev(total*20,255);for(int i=0;i<20;i++)dp[(1<<i)*20+i]=0;
for(int mask=1;mask<total;mask++){int remaining=(total-1)^mask;for(int bits=mask;bits;bits&=bits-1){int last=__builtin_ctz((unsigned)bits);float sc=dp[mask*20+last];if(sc< -1e8)continue;for(int todo=remaining;todo;todo&=todo-1){int next=__builtin_ctz((unsigned)todo),nm=mask|(1<<next);float ns=sc+edge[last][next];if(ns>dp[nm*20+next]){dp[nm*20+next]=ns;prev[nm*20+next]=last;}}}}
int mask=total-1,last=max_element(dp.end()-20,dp.end())-(dp.end()-20);vector<int>order;while(mask){order.push_back(last);int parent=prev[mask*20+last];mask^=1<<last;last=parent;}reverse(order.begin(),order.end());string plain;for(int row:order)plain+=clean[row];vector<int>k1(20),k2(20);for(int i=0;i<20;i++){k1[best[i]]=i;k2[order[i]]=i;}cout<<language(plain)<<" key1=";for(int x:k1)cout<<x<<",";cout<<" key2=";for(int x:k2)cout<<x<<",";cout<<" "<<plain<<"\n";}
