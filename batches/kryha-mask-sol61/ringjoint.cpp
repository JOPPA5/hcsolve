#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <vector>
using namespace std;vector<float>grams[6];vector<int>cipher,d;array<int,26>P,O;mt19937 rng(52619632);float weight[6]={0,0,.1,.15,.4,.8};
float score(const array<int,26>&p,const array<int,26>&o){int plain[1000];for(int i=0;i<cipher.size();i++)plain[i]=p[(o[cipher[i]]-d[i]+26)%26];float total=0;for(int n=2;n<=5;n++)for(int i=0;i+n<=cipher.size();i++){int ix=0;for(int j=0;j<n;j++)ix=ix*26+plain[i+j];total+=weight[n]*grams[n][ix];}return total;}
int main(int argc,char**argv){ifstream f(argv[1]);string ct;f>>ct;for(char c:ct)cipher.push_back(c-'a');ifstream k(argv[2]);for(int&v:P)k>>v;for(int&v:O)k>>v;ifstream hs(argv[3]);vector<int>holes;int h;while(hs>>h)holes.push_back(h);int coord[52];ifstream cs(argv[4]);for(int&v:coord)cs>>v;int m=holes.size();for(int i=0;i<cipher.size();i++){int j=i%m;int dist=coord[holes[j]]-coord[holes[0]]+(holes[j]<holes[0]?179:0)+179*(i/m);d.push_back((dist%26+26)%26);}for(int n=2;n<=5;n++){int size=1;for(int j=0;j<n;j++)size*=26;grams[n].assign(size,-n);ifstream model(n<4?string(argv[5])+"/model"+to_string(n)+".tsv":string(argv[6])+"/ring-"+to_string(n)+"grams.tsv");assert(model);string s;float val;while(model>>s>>val){int ix=0;for(char c:s)ix=ix*26+c-'a';grams[n][ix]=val;}}int steps=stoi(argv[7]);float now=score(P,O),best=now;auto bp=P,bo=O;for(int it=0;it<steps;it++){auto pp=P,oo=O;int a=rng()%26,b=rng()%26;if((it/2500)%2==0)swap(pp[a],pp[b]);else swap(oo[a],oo[b]);float next=score(pp,oo),temp=.2+12*(1.-(it%10000)/10000.);if(next>=now||log((rng()+1.)/4294967297.)<(next-now)/temp){P=pp;O=oo;now=next;if(now>best){best=now;bp=P;bo=O;}}}cout<<best<<'\n';for(int v:bp)cout<<v<<' ';for(int v:bo)cout<<v<<' ';cout<<'\n';for(int i=0;i<cipher.size();i++)cout<<char('a'+bp[(bo[cipher[i]]-d[i]+26)%26]);cout<<'\n';}
