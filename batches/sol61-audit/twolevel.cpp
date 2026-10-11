#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <vector>
using namespace std;
float q[26*26*26*26];
int id(const string&s){int v=0;for(char c:s)v=26*v+c-'a';return v;}
float score(const string&s){float z=0;for(int i=0;i+3<(int)s.size();i++)z+=q[((s[i]-'a')*26+s[i+1]-'a')*676+(s[i+2]-'a')*26+s[i+3]-'a'];return z;}
string dec(const vector<string>&chunks,const vector<int>&k,int N){string out(N,' ');int w=k.size();for(int j=0;j<w;j++)for(int y=0;y<(int)chunks[j].size();y++)out[y*w+k[j]]=chunks[j][y];return out;}
int main(int argc,char**argv){if(argc!=6)return 2;fill(begin(q),end(q),-4);ifstream f(argv[1]);string gram;float val;while(f>>gram>>val)q[id(gram)]=val;ifstream c(argv[2]);string ct;c>>ct;int w=22,N=ct.size(),rest=stoi(argv[3]),steps=stoi(argv[4]);if(N%w!=w-1){cerr<<"Requires one short column\n";return 3;}mt19937 rng(stoul(argv[5]));float best=-1e9;vector<int>bk;string bp;long long eval=0;
for(int shortpos=0;shortpos<w;shortpos++){
 vector<string> chunks;int at=0;for(int j=0;j<w;j++){int len=N/w+(j!=shortpos);chunks.push_back(ct.substr(at,len));at+=len;}vector<int>slots;for(int j=0;j<w;j++)if(j!=shortpos)slots.push_back(j);
 for(int rep=0;rep<rest;rep++){
 vector<int>k(w),longs(w-1);iota(longs.begin(),longs.end(),0);shuffle(longs.begin(),longs.end(),rng);k[shortpos]=w-1;for(int j=0;j<w-1;j++)k[slots[j]]=longs[j];float sc=score(dec(chunks,k,N));
 for(int it=0;it<steps;it++){
 auto kk=k;int a=rng()%(w-1),b=rng()%(w-1);if(a>b)swap(a,b);if(it%3==0)swap(kk[slots[a]],kk[slots[b]]);else if(it%3==1){for(int j=a;j<=b;j++)kk[slots[j]]=k[slots[a+b-j]];}else{int v=kk[slots[a]];for(int j=a;j<b;j++)kk[slots[j]]=kk[slots[j+1]];kk[slots[b]]=v;}
 string pt=dec(chunks,kk,N);float ns=score(pt),t=.5+10.*(1.-(it%5000)/5000.);eval++;if(ns>sc||uniform_real_distribution<double>(0,1)(rng)<exp((ns-sc)/t)){k=kk;sc=ns;}if(ns>best){best=ns;bk=kk;bp=pt;}
 }
 }
}
cout<<"score "<<best<<"\nevaluations "<<eval<<"\nkey ";for(int x:bk)cout<<x<<',';cout<<"\nplaintext "<<bp<<'\n';
}
