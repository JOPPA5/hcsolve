#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <random>
#include <numeric>
#include <cmath>
using namespace std;
float q[26*26*26*26];
string ct;
mt19937 rng(332);
int id(string s){int r=0;for(char c:s)r=r*26+c-'a';return r;}
string dec(const vector<int>&key){string s=ct;for(char &c:s)c='a'+key[c-'a'];return s;}
float score(string s){float sum=0;for(int i=0;i+3<(int)s.size();i++)if(s[i]!='?'&&s[i+1]!='?'&&s[i+2]!='?'&&s[i+3]!='?')sum+=q[((s[i]-'a')*26+s[i+1]-'a')*26*26+(s[i+2]-'a')*26+s[i+3]-'a'];return sum;}
int main(int argc,char**argv){ifstream f(string(argv[1])+"/quadgrams.tsv");string x;float v;fill(begin(q),end(q),-4.0);while(f>>x>>v)q[id(x)]=v;ifstream c(argc>2?argv[2]:(string(argv[1])+"/cipher.txt"));c>>ct;
for(int w=26;w<=26;w++){float best=-1e9;vector<int>bk;string bt;for(int restart=0;restart<200;restart++){vector<int> k(w);iota(k.begin(),k.end(),0);shuffle(k.begin(),k.end(),rng);float sc=score(dec(k));for(int it=0;it<50000;it++){auto kk=k;int a=rng()%w;swap(kk[a],kk[rng()%w]);float ns=score(dec(kk));float temp=1.0+10.0*(1.0-(it%5000)/5000.0);if(ns>sc || uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/temp)){k=kk;sc=ns;}if(sc>best){best=sc;bk=k;bt=dec(k);}}}cout<<w<<" "<<best<<" ";for(int i:bk)cout<<i<<",";cout<<" "<<bt<<endl;}}
