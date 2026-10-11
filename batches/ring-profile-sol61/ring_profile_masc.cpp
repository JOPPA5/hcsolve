#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
#include <string>
#include <random>
#include <cmath>
using namespace std;
float q[456976];int steps[]={7,6,7,5,6,7,6,8,6,10,5,6,5,7,6,5,9};
int idx(string s){int x=0;for(char c:s)x=x*26+c-'a';return x;}
float score(const vector<int>&P,const vector<int>&v){float z=0;for(int i=0;i+3<v.size();i++){int id=(P[v[i]]*26+P[v[i+1]])*676+P[v[i+2]]*26+P[v[i+3]];z+=q[id];}return z;}
int main(int argc,char**argv){fill(begin(q),end(q),-4);ifstream f(string(argv[1])+"/ring-4grams.tsv");string s;float value;while(f>>s>>value)q[idx(s)]=value;ifstream in(argv[2]);string ct;in>>ct;int phase=stoi(argv[3]),sign=stoi(argv[4]);vector<int>d;int shift=0;for(int i=0;i<ct.size();i++){d.push_back(shift);shift=(shift+sign*steps[(phase+i)%17]+26)%26;}ifstream candidates(argv[5]);double concentration;int number=0;string key;while(candidates>>concentration>>key){vector<int>O;string item;for(char c:key){if(c==','){O.push_back(stoi(item));item.clear();}else item+=c;}vector<int>v;for(int i=0;i<ct.size();i++)v.push_back((O[ct[i]-'a']-d[i]+26)%26);mt19937 rng(350385);float best=-1e9;vector<int>bp;for(int r=0;r<8;r++){vector<int>P(26);iota(P.begin(),P.end(),0);shuffle(P.begin(),P.end(),rng);float sc=score(P,v);for(int it=0;it<30000;it++){auto pp=P;int a=rng()%26,b=rng()%26;swap(pp[a],pp[b]);if(it%100==0){int off=rng()%26;rotate(pp.begin(),pp.begin()+off,pp.end());}float ns=score(pp,v);float temp=.2+9*(1.0-(it%10000)/10000.0);if(ns>sc||uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/temp)){P=pp;sc=ns;}if(sc>best){best=sc;bp=P;}}}string text;for(int x:v)text+=char('a'+bp[x]);cout<<number++<<" "<<concentration<<endl<<best<<" "<<text<<endl;for(int x:bp)cout<<x<<",";cout<<endl;for(int x:O)cout<<x<<",";cout<<endl;}}
