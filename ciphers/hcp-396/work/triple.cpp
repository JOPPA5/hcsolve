#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
#include <array>
#include <random>
#include <cmath>
using namespace std;float q[26*26*26*26];mt19937 rng(396);string ct;
string dec(string s,const vector<int>&k){int w=k.size(),n=s.size(),h=n/w,e=n%w,at=0;string out(n,' ');for(int c:k)for(int r=0;r<h+(c<e);r++)out[r*w+c]=s[at++];return out;}
string decrypt(const array<vector<int>,3>&k){string s=ct;for(int j=2;j>=0;j--)s=dec(s,k[j]);return s;}
float score(string s){float z=0;for(int i=0;i+3<s.size();i++)z+=q[((s[i]-'a')*26+s[i+1]-'a')*676+(s[i+2]-'a')*26+s[i+3]-'a'];return z;}
int main(int argc,char**argv){fill(begin(q),end(q),-4);ifstream f(argv[1]);string g;float v;while(f>>g>>v){int i=0;for(char c:g)i=i*26+c-'a';q[i]=v;}ifstream in(argv[2]);in>>ct;array<int,3>w={16,18,20};if(argc>3)for(int j=0;j<3;j++)w[j]=stoi(argv[j+3]);float best=-1e9;array<vector<int>,3>bk;string bp;for(int restart=0;restart<100;restart++){array<vector<int>,3>k;for(int j=0;j<3;j++){k[j].resize(w[j]);iota(k[j].begin(),k[j].end(),0);shuffle(k[j].begin(),k[j].end(),rng);}float sc=score(decrypt(k));for(int it=0;it<50000;it++){auto kk=k;int j=rng()%3,a=rng()%w[j],b=rng()%w[j];swap(kk[j][a],kk[j][b]);if(it%5==0){if(a>b)swap(a,b);reverse(kk[j].begin()+a,kk[j].begin()+b+1);}float ns=score(decrypt(kk));float t=0.3+5.0*(1.0-(it%5000)/5000.0);if(ns>sc||uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/t)){k=kk;sc=ns;}if(sc>best){best=sc;bk=k;bp=decrypt(k);}}}cout<<best<<" "<<bp<<endl;for(auto k:bk){for(int x:k)cout<<x<<",";cout<<endl;}}
