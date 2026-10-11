#include <algorithm>
#include <array>
#include <cmath>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>
using namespace std;
float q[456976];string ct;int T;mt19937 rng(33451);vector<array<int,26>>H;vector<pair<int,vector<int>>>top;long long enumeration=0;
float score(vector<int>&K,vector<int>&v){float z=0;for(int i=0;i+3<v.size();i++){if(v[i]<0||v[i+1]<0||v[i+2]<0||v[i+3]<0)continue;z+=q[(K[v[i]]*26+K[v[i+1]])*676+K[v[i+2]]*26+K[v[i+3]]];}return z;}
vector<int>projection(vector<int>&R){vector<int>v;for(int i=0;i<ct.size();i++){int c=ct[i]-'a';v.push_back(c<0||c>=26?-1:(c-R[i%T]+26)%26);}return v;}
string decode(vector<int>&K,vector<int>&v){string s;for(int x:v)s+=x<0?'?':'a'+K[x];return s;}
void enumerate(vector<int>&R,int p){if(p==T){enumeration++;array<int,26>N={};for(int r=0;r<T;r++)for(int c=0;c<26;c++)N[(c-R[r]+26)%26]+=H[r][c];int sc=0;for(int x:N)sc+=x*x;if(top.size()<64||sc>top.back().first){top.push_back({sc,R});sort(top.rbegin(),top.rend());if(top.size()>64)top.pop_back();}return;}for(int x=0;x<26;x++){R[p]=x;enumerate(R,p+1);}}
int main(int argc,char**argv){fill(begin(q),end(q),-4);ifstream f(argv[1]);string s;float z;while(f>>s>>z){int n=0;for(char c:s)n=n*26+c-'a';q[n]=z;}ifstream in(argv[2]);in>>ct;T=stoi(argv[3]);H.resize(T);for(int i=0;i<ct.size();i++)if(ct[i]>='a'&&ct[i]<='z')H[i%T][ct[i]-'a']++;vector<int>R(T);enumerate(R,1);float best=-1e9;vector<int>bk,br,bv;for(auto&[ic,rr]:top){auto v=projection(rr);for(int r=0;r<6;r++){vector<int>K(26);iota(K.begin(),K.end(),0);shuffle(K.begin(),K.end(),rng);float sc=score(K,v);for(int it=0;it<30000;it++){auto kk=K;swap(kk[rng()%26],kk[rng()%26]);float ns=score(kk,v),temp=.2+9*(1.-(it%10000)/10000.);if(ns>sc||uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/temp)){K=kk;sc=ns;}if(sc>best){best=sc;bk=K;br=rr;bv=v;}}}}
for(int r=0;r<6;r++){auto K=bk,R=br,v=projection(R);float sc=score(K,v);for(int it=0;it<100000;it++){auto kk=K,rr=R;if((it/2500)%2==0)swap(kk[rng()%26],kk[rng()%26]);else if(T>1)rr[1+rng()%(T-1)]=rng()%26;auto vv=projection(rr);float ns=score(kk,vv),temp=.2+9*(1.-(it%10000)/10000.);if(ns>sc||uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/temp)){K=kk;R=rr;v=vv;sc=ns;}if(sc>best){best=sc;bk=K;br=R;bv=v;}}}cout<<best<<" "<<decode(bk,bv)<<endl;for(int x:bk)cout<<x<<",";cout<<endl;for(int x:br)cout<<x<<",";cout<<endl;cout<<"enumerated "<<enumeration<<" retained "<<top.size()<<endl;}
