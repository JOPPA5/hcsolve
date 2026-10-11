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
float score(const vector<int>&P,const vector<int>&v){vector<int>L;for(int x:v)if(P[x]!=9)L.push_back(P[x]);float z=0;for(int i=0;i+3<L.size();i++)z+=q[((L[i]*26+L[i+1])*26+L[i+2])*26+L[i+3]];return z;}
int main(int argc,char**argv){fill(begin(q),end(q),-4);ifstream f(string(argv[1])+"/selective-j-german-quadgrams.tsv");string s;float value;while(f>>s>>value)q[idx(s)]=value;ifstream in(argv[2]);string ct;in>>ct;int phase=stoi(argv[3]),sign=stoi(argv[4]);vector<int>d;int shift=0;for(int i=0;i<ct.size();i++){d.push_back(shift);shift=(shift+sign*steps[(phase+i)%17]+26)%26;}ifstream candidates(argv[5]);int concentration,number=0;string key;while(candidates>>concentration>>key){vector<int>O;string item;for(char c:key){if(c==','){O.push_back(stoi(item));item.clear();}else item+=c;}vector<int>v;int shift=0,k=phase;for(char c:ct){int slot=(O[c-'a']-shift+26)%26;v.push_back(slot);for(int z=0;z<(slot==0?2:1);z++){shift=(shift+sign*steps[k%17]+26)%26;k++;}}mt19937 rng(350385);float best=-1e9;vector<int>bp;for(int r=0;r<8;r++){vector<int>P(26);iota(P.begin(),P.end(),0);swap(P[0],P[9]);shuffle(P.begin()+1,P.end(),rng);float sc=score(P,v);for(int it=0;it<30000;it++){auto pp=P;int a=1+rng()%25,b=1+rng()%25;swap(pp[a],pp[b]);if(it%100==0){int off=rng()%25;rotate(pp.begin()+1,pp.begin()+1+off,pp.end());}float ns=score(pp,v);float temp=.2+9*(1.0-(it%10000)/10000.0);if(ns>sc||uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/temp)){P=pp;sc=ns;}if(sc>best){best=sc;bp=P;}}}string text;for(int x:v)text+=char('a'+bp[x]);cout<<number++<<" "<<concentration<<endl<<best<<" "<<text<<endl;for(int x:bp)cout<<x<<",";cout<<endl;for(int x:O)cout<<x<<",";cout<<endl;}}
