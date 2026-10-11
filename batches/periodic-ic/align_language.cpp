#include <algorithm>
#include <array>
#include <cmath>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>
using namespace std;
float q[456976];int T,S;string ct;mt19937 rng(521943);
int idx(string s){int v=0;for(char c:s)v=v*26+c-'a';return v;}
string dec(vector<int>&P,vector<int>&O,vector<int>&R){string pt=ct;for(int i=0;i<ct.size();i++)pt[i]='a'+P[(O[ct[i]-'a']-R[i%T]-(i/T*S)%26+52)%26];return pt;}
float score(string s){float z=0;for(int i=0;i+3<s.size();i++)z+=q[idx(s.substr(i,4))];return z;}
int main(int argc,char**argv){ifstream f(argv[1]);string s;float v;fill(begin(q),end(q),-4);while(f>>s>>v)q[idx(s)]=v;ifstream in(argv[2]);in>>ct;T=stoi(argv[3]);S=stoi(argv[4]);ifstream cand(argv[5]);int concentration,num=0;string encoded;float global=-1e9;vector<int>bp,bo,br;while(cand>>concentration>>encoded){vector<int>O;string item;for(char c:encoded){if(c==','){O.push_back(stoi(item));item.clear();}else item+=c;}vector<array<int,26>>H(T);for(int i=0;i<ct.size();i++)H[i%T][(O[ct[i]-'a']-(i/T*S)%26+26)%26]++;int bic=-1;vector<int>rkey;for(int r=0;r<20;r++){vector<int>R(T);array<int,26>N={};for(int p=0;p<T;p++){R[p]=rng()%26;for(int j=0;j<26;j++)N[(j-R[p]+26)%26]+=H[p][j];}int sc=0;for(int x:N)sc+=x*x;for(int it=0;it<5000;it++){int p=rng()%T,a=R[p],b=rng()%26;array<int,26>delta={};int change=0;for(int j=0;j<26;j++){delta[j]=H[p][(j+b)%26]-H[p][(j+a)%26];change+=2*N[j]*delta[j]+delta[j]*delta[j];}float temp=.1+70*(1.-(it%1000)/1000.);if(change>=0||uniform_real_distribution<float>(0,1)(rng)<exp(change/temp)){R[p]=b;for(int j=0;j<26;j++)N[j]+=delta[j];sc+=change;}if(sc>bic){bic=sc;rkey=R;}}}float best=-1e9;vector<int>pk;string text;for(int r=0;r<8;r++){vector<int>P(26);iota(P.begin(),P.end(),0);shuffle(P.begin(),P.end(),rng);float sc=score(dec(P,O,rkey));for(int it=0;it<30000;it++){auto pp=P;swap(pp[rng()%26],pp[rng()%26]);float ns=score(dec(pp,O,rkey)),temp=.2+9*(1.-(it%10000)/10000.);if(ns>sc||uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/temp)){P=pp;sc=ns;}if(sc>best){best=sc;pk=P;text=dec(P,O,rkey);}}}cout<<num++<<" "<<concentration<<" "<<bic<<" "<<best<<" "<<text<<endl;for(int x:pk)cout<<x<<",";cout<<endl;for(int x:O)cout<<x<<",";cout<<endl;for(int x:rkey)cout<<x<<",";cout<<endl;if(best>global){global=best;bp=pk;bo=O;br=rkey;}}
for(int r=0;r<8;r++){auto P=bp,O=bo,R=br;float sc=score(dec(P,O,R));for(int it=0;it<100000;it++){auto pp=P,oo=O,rr=R;int which=(it/2500)%3;if(which==0)swap(pp[rng()%26],pp[rng()%26]);else if(which==1)swap(oo[rng()%26],oo[rng()%26]);else rr[rng()%T]=rng()%26;float ns=score(dec(pp,oo,rr)),temp=.2+9*(1.-(it%10000)/10000.);if(ns>sc||uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/temp)){P=pp;O=oo;R=rr;sc=ns;}if(sc>global){global=sc;bp=P;bo=O;br=R;}}}
cout<<"FINAL "<<global<<" "<<dec(bp,bo,br)<<endl;for(int x:bp)cout<<x<<",";cout<<endl;for(int x:bo)cout<<x<<",";cout<<endl;for(int x:br)cout<<x<<",";cout<<endl;}
