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
struct Candidate {float score;array<int,10> cols,rows;string plain;bool operator<(const Candidate&o)const{return score>o.score;}};
int main(int argc,char**argv){load(argv[1],argv[2]);loadLex(argv[1]);ifstream f(argv[3]);string ct;f>>ct;assert(ct.size()==100);vector<string>raw;for(int i=0;i<10;i++)raw.push_back(ct.substr(i*10,10));
vector<float>g[6];float wt[]={0,0,0,.15,.4,.8};for(int n=3;n<=5;n++){int total=1;for(int i=0;i<n;i++)total*=10;g[n].assign(total,0);for(int ix=0;ix<total;ix++){int z=ix,cs[5];for(int j=n-1;j>=0;j--){cs[j]=z%10;z/=10;}for(auto&r:raw){int ind=0;for(int j=0;j<n;j++)ind=ind*26+r[cs[j]]-'a';g[n][ix]+=wt[n]*gram[n][ind];}}}
array<int,10>p;iota(p.begin(),p.end(),0);priority_queue<Candidate>heap;long count=0;do{float sc=0;for(int n=3;n<=5;n++)for(int j=0;j<=10-n;j++){int ix=0;for(int a=0;a<n;a++)ix=ix*10+p[j+a];sc+=g[n][ix];}Candidate c;c.score=sc;c.cols=p;if(heap.size()<64)heap.push(c);else if(sc>heap.top().score){heap.pop();heap.push(c);}count++;}while(next_permutation(p.begin(),p.end()));vector<Candidate>columns;while(!heap.empty()){columns.push_back(heap.top());heap.pop();}reverse(columns.begin(),columns.end());cerr<<"exact column permutations="<<count<<" retained="<<columns.size()<<endl;
priority_queue<Candidate>finals;for(int ci=0;ci<(int)columns.size();ci++){auto col=columns[ci];vector<string>r;for(auto&s:raw){string t;for(int c:col.cols)t+=s[c];r.push_back(t);}float edge[10][10];for(int a=0;a<10;a++)for(int b=0;b<10;b++)edge[a][b]=language(r[a].substr(6)+r[b].substr(0,4))-language(r[a].substr(6))-language(r[b].substr(0,4));iota(p.begin(),p.end(),0);do{float sc=col.score;for(int j=0;j<9;j++)sc+=edge[p[j]][p[j+1]];if(finals.size()<50000||sc>finals.top().score){Candidate c=col;c.score=sc;c.rows=p;if(finals.size()==50000)finals.pop();finals.push(c);}}while(next_permutation(p.begin(),p.end()));if(ci%16==0)cerr<<"row exhaustive column candidate="<<ci<<endl;}
vector<Candidate>out;while(!finals.empty()){auto c=finals.top();finals.pop();for(int r:c.rows)for(int col:c.cols)c.plain+=raw[r][col];c.score+=2*lex(c.plain);out.push_back(c);}sort(out.begin(),out.end(),[](auto&a,auto&b){return a.score>b.score;});if(argc>5){ifstream expf(argv[5]);string expected;expf>>expected;bool found=false;for(int j=0;j<(int)out.size();j++)if(out[j].plain==expected){cerr<<"truth lexical rank="<<j<<" score="<<out[j].score<<endl;found=true;}if(!found)cerr<<"truth absent retained 50000"<<endl;}for(int i=0;i<100;i++){auto&c=out[i];cout<<i<<" "<<c.score<<" cols=";for(int x:c.cols)cout<<x<<",";cout<<" rows=";for(int x:c.rows)cout<<x<<",";cout<<" "<<c.plain<<"\n";}}
