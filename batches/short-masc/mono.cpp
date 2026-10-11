// Adapted frozen multigram, permutation/strict-anchor conventions from
// batches/scoring-sol61/mono-frequency-seeded-strict.cpp. New blind unlocked
// refinement retains several distinct keys instead of trusting one top score.
#include <algorithm>
#include <array>
#include <cmath>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <vector>
#include <set>
using namespace std;vector<float>g[6];string ct;int N;mt19937 rng(396345);
int fold(int v){return v==26?2:v==27?18:v;}
void load(string dir){for(int n=3;n<=5;n++){ifstream f(dir+"/model"+to_string(n)+".tsv");string s;float v;f>>s>>v;int size=1;for(int i=0;i<n;i++)size*=26;g[n].assign(size,v);while(f>>s>>v){int ix=0;for(char c:s)ix=ix*26+c-'a';g[n][ix]=v;}}}
string decode(vector<int>k,bool folded=true){string p=ct;for(char&c:p)c='a'+(folded?fold(k[c-'a']):k[c-'a']);return p;}
float score(string p){float out=0,wt[]={0,0,0,.15,.4,.8};for(int n=3;n<=5;n++){int ix=0,pow=1;for(int j=1;j<n;j++)pow*=26;for(int i=0;i<p.size();i++){if(i>=n)ix-=(p[i-n]-'a')*pow;ix=ix*26+p[i]-'a';if(i>=n-1)out+=wt[n]*g[n][ix];}}return out;}
struct Candidate{float sc;vector<int>key;};vector<Candidate>pool;
void retain(float sc,vector<int>k){pool.push_back({sc,k});if(pool.size()>256){sort(pool.begin(),pool.end(),[](auto&a,auto&b){return a.sc>b.sc;});set<string>unique;vector<Candidate>p;for(auto c:pool){string sig=decode(c.key,false);if(unique.insert(sig).second){p.push_back(c);if(p.size()==64)break;}}pool=p;}}
int main(int argc,char**argv){load(argv[1]);ifstream f(argv[2]),seeds(argv[3]);f>>ct;N=stoi(argv[4]);string key,mask;int count=0;while(seeds>>key>>mask){vector<int>k(N),free;for(int i=0;i<N;i++){k[i]=key[i]-'a';if(mask[i]=='0')free.push_back(i);}float sc=score(decode(k)),best=sc;vector<int>bk=k;int steps=free.size()<2?0:1000;for(int it=0;it<steps;it++){auto kk=k;swap(kk[free[rng()%free.size()]],kk[free[rng()%free.size()]]);float ns=score(decode(kk)),temp=.2+6*(1.-it/double(steps));if(ns>=sc||log((rng()+1.)/4294967297.)<(ns-sc)/temp){k=kk;sc=ns;}if(sc>best){best=sc;bk=k;}}retain(best,bk);count++;}sort(pool.begin(),pool.end(),[](auto&a,auto&b){return a.sc>b.sc;});if(pool.size()>64)pool.resize(64);auto starts=pool;for(int r=0;r<starts.size();r++){auto k=starts[r].key;float sc=starts[r].sc;auto bk=k;float best=sc;for(int it=0;it<10000;it++){auto kk=k;swap(kk[rng()%N],kk[rng()%N]);float ns=score(decode(kk)),temp=.2+5*(1.-(it%2000)/2000.);if(ns>=sc||log((rng()+1.)/4294967297.)<(ns-sc)/temp){k=kk;sc=ns;}if(sc>best){best=sc;bk=k;}}retain(best,bk);}sort(pool.begin(),pool.end(),[](auto&a,auto&b){return a.sc>b.sc;});set<string>unique;int out=0;for(auto c:pool){string raw=decode(c.key,false);if(!unique.insert(raw).second)continue;cout<<out++<<" score="<<c.sc<<" key=";for(int v:c.key)cout<<char('a'+v);cout<<" plain="<<decode(c.key)<<" raw="<<raw<<'\n';if(out==64)break;}cerr<<"strict starts "<<count<<" unlocked starts "<<starts.size()<<" survivors "<<out<<'\n';return 0;}
