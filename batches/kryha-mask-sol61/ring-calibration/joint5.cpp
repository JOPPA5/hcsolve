// Adapted progressive pipeline with supplied actual-wheel schedule file argv6. No true ring seed.
#include <cassert>
// Read-only source adaptation: frozen pure5gram objective; progressive unit steps.
#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
#include <string>
#include <random>
#include <cmath>
using namespace std;float q[456976],five[11881376];mt19937 rng(350385);string ct;vector<int>d;vector<int> steps;
int idx(string s){int x=0;for(char c:s)x=x*26+c-'a';return x;}
string dec(const vector<int>&P,const vector<int>&O){string s=ct;for(int i=0;i<s.size();i++)s[i]='a'+P[(O[ct[i]-'a']-d[i]+26)%26];return s;}
float score(string s,bool use5){float z=0;for(int i=0;i+3<s.size();i++){int id=((s[i]-'a')*26+s[i+1]-'a')*676+(s[i+2]-'a')*26+s[i+3]-'a';if(!use5)z+=q[id];else if(i+4<s.size())z+=five[id*26+s[i+4]-'a'];}return z;}
int main(int argc,char**argv){ifstream schedule(argv[6]);int st;while(schedule>>st)steps.push_back(st);assert(!steps.empty());fill(begin(q),end(q),-4);fill(begin(five),end(five),-5);ifstream f(string(argv[1])+"/ring-4grams.tsv"),g(string(argv[1])+"/ring-5grams.tsv");string s;float v;while(f>>s>>v)q[idx(s)]=v;while(g>>s>>v)five[idx(s)]=v;ifstream in(argv[2]);in>>ct;int phase=stoi(argv[3]),sign=stoi(argv[4]),restarts=8;bool use5=true;int shift=0;for(int i=0;i<ct.size();i++){d.push_back(shift);shift=(shift+sign*steps[(phase+i)%steps.size()]+26)%26;}float best=-1e9;vector<int>bp,bo;string text;for(int r=0;r<restarts;r++){vector<int>P(26),O(26);iota(P.begin(),P.end(),0);iota(O.begin(),O.end(),0);ifstream seeds(argv[5]);for(int&x:P)seeds>>x;for(int&x:O)seeds>>x;for(int k=0;k<r%4;k++){swap(P[rng()%26],P[rng()%26]);swap(O[rng()%26],O[rng()%26]);}float sc=score(dec(P,O),use5);for(int it=0;it<100000;it++){auto pp=P,oo=O;int a=rng()%26,b=rng()%26;bool input=(it/2500)%2==0;if(input)swap(pp[a],pp[b]);else swap(oo[a],oo[b]);if(it%100==0){int off=rng()%26;if(input)rotate(pp.begin(),pp.begin()+off,pp.end());else for(int&x:oo)x=(x+off)%26;}float ns=score(dec(pp,oo),use5);float temp=.2+9*(1.0-(it%10000)/10000.0);if(ns>sc||uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/temp)){P=pp;O=oo;sc=ns;}if(sc>best){best=sc;bp=P;bo=O;text=dec(P,O);}}}cout<<best<<" "<<text<<endl;for(int x:bp)cout<<x<<",";cout<<endl;for(int x:bo)cout<<x<<",";cout<<endl;}
