#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <vector>
#include <cmath>
using namespace std;
float quad[26*26*26*26];
mt19937 rng(357);
string dec(const string &ct,const vector<int>&key){int w=key.size(),n=ct.size(),h=n/w,extra=n%w,at=0;string s(n,' ');for(int col:key){int len=h+(col<extra);for(int r=0;r<len;r++)s[r*w+col]=ct[at++];}return s;}
string cascade(string t,const vector<vector<int>>&keys){for(auto&k:keys)t=dec(t,k);return t;}
float score(const string&s){float v=0;for(int i=0;i+3<(int)s.size();i++)v+=quad[((s[i]-'a')*26+s[i+1]-'a')*676+(s[i+2]-'a')*26+s[i+3]-'a'];return v;}
int main(int argc,char**argv){string path=argv[1],file=argv[2];fill(begin(quad),end(quad),-4);ifstream f(path+"/quadgrams.tsv");string z;float v;while(f>>z>>v){int id=0;for(char c:z)id=id*26+c-'a';quad[id]=v;}ifstream c(path+"/"+file);string ct;c>>ct;
for(int stages=2;stages<=3;stages++)for(int w=16;w<=22;w++){
float best=-1e9;string bt;vector<vector<int>> bk;
for(int restart=0;restart<30;restart++){
vector<vector<int>> keys(stages,vector<int>(w));for(auto &k:keys){iota(k.begin(),k.end(),0);shuffle(k.begin(),k.end(),rng);}float old=score(cascade(ct,keys));
for(int it=0;it<30000;it++){
auto kk=keys;int k=rng()%stages,a=rng()%w,b=rng()%w;swap(kk[k][a],kk[k][b]);if(it%5==0){if(a>b)swap(a,b);reverse(kk[k].begin()+a,kk[k].begin()+b+1);}string t=cascade(ct,kk);float now=score(t);float temp=0.5+6.0*(1.-(it%10000)/10000.);if(now>old||uniform_real_distribution<float>(0,1)(rng)<exp((now-old)/temp)){keys=kk;old=now;}if(now>best){best=now;bk=kk;bt=t;}
}}
cout<<"stages="<<stages<<" width="<<w<<" score="<<best<<" text="<<bt<<" keys=";for(auto &k:bk){cout<<"[";for(int j:k)cout<<j<<",";cout<<"]";}cout<<endl;
}}
