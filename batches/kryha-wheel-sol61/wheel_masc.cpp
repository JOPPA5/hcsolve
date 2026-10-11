#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <vector>
using namespace std;float q[456976];int coord[52];
int idx(string s){int x=0;for(char c:s)x=x*26+c-'a';return x;}
vector<int>csv(string s){vector<int>x;string v;for(char c:s){if(c==','){x.push_back(stoi(v));v.clear();}else v+=c;}return x;}
float score(const vector<int>&P,const vector<int>&v){float z=0;for(int i=0;i+3<v.size();i++)z+=q[((P[v[i]]*26+P[v[i+1]])*26+P[v[i+2]])*26+P[v[i+3]]];return z;}
int main(int argc,char**argv){fill(begin(q),end(q),-4);ifstream f(string(argv[1])+"/ring-4grams.tsv");string s;float x;while(f>>s>>x)q[idx(s)]=x;ifstream cipher(argv[2]);string ct;cipher>>ct;ifstream geometry(argv[3]);int d,i=0,sum=0;while(geometry>>d){coord[i++]=sum;sum+=d;}if(i!=52||sum!=179)return 2;ifstream candidates(argv[4]);int IC,phase,num=0;string Ostr,Mstr;while(candidates>>IC>>Ostr>>Mstr>>phase){auto O=csv(Ostr),stops=csv(Mstr);int m=stops.size(),origin=coord[stops[phase]-1];vector<int>v;for(int t=0;t<ct.size();t++){int D=coord[stops[(phase+t)%m]-1]+179*((phase+t)/m)-origin;v.push_back((O[ct[t]-'a']-D%26+26)%26);}mt19937 rng(350385);float best=-1e9;vector<int>bp;for(int r=0;r<8;r++){vector<int>P(26);iota(P.begin(),P.end(),0);shuffle(P.begin(),P.end(),rng);float sc=score(P,v);for(int it=0;it<30000;it++){auto pp=P;swap(pp[rng()%26],pp[rng()%26]);if(it%100==0){int off=rng()%26;rotate(pp.begin(),pp.begin()+off,pp.end());}float ns=score(pp,v),temp=.2+9*(1.0-(it%10000)/10000.0);if(ns>sc||uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/temp)){P=pp;sc=ns;}if(sc>best){best=sc;bp=P;}}}cout<<num++<<" "<<IC<<" "<<phase<<" "<<Mstr<<endl<<best<<" ";for(int x:v)cout<<char('a'+bp[x]);cout<<endl;for(int x:bp)cout<<x<<",";cout<<endl;for(int x:O)cout<<x<<",";cout<<endl;}}
