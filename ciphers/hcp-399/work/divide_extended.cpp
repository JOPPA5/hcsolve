#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
#include <string>
#include <random>
#include <cmath>
using namespace std;float bi[676];mt19937 rng(2399);string ct;int w1,w2;
string dec(string s,const vector<int>&k){int w=k.size(),h=s.size()/w,e=s.size()%w,at=0;string p(s.size(),' ');for(int c:k)for(int r=0;r<h+(c<e);r++)p[r*w+c]=s[at++];return p;}
vector<vector<float>> pairs(string s){int h=s.size()/w1;vector<vector<float>> a(w1,vector<float>(w1));for(int i=0;i<w1;i++)for(int j=0;j<w1;j++){if(i==j){a[i][j]=-1e6;continue;}float z=0;for(int r=0;r<h;r++)z+=bi[(s[i*h+r]-'a')*26+s[j*h+r]-'a'];a[i][j]=z;}return a;}
float potential(string s){auto a=pairs(s);float z=0;for(int i=0;i<w1;i++){float best=-1e6;for(int j=0;j<w1;j++)best=max(best,a[i][j]);z+=best;}for(int j=0;j<w1;j++){float best=-1e6;for(int i=0;i<w1;i++)best=max(best,a[i][j]);z+=best;}return z;}
float pathscore(const vector<int>&k,const vector<vector<float>>&a){float z=0;for(int i=0;i+1<k.size();i++)z+=a[k[i]][k[i+1]];return z;}
int main(int argc,char**argv){ifstream f(argv[1]);string g;float v;while(f>>g>>v)bi[(g[0]-'a')*26+g[1]-'a']=v;ifstream c(argv[2]);c>>ct;w1=stoi(argv[3]);w2=stoi(argv[4]);if(ct.size()%w1){cerr<<"requires regular first width\n";return 1;}float best=-1e9;vector<int>bk;for(int restart=0;restart<100;restart++){vector<int>k(w2);iota(k.begin(),k.end(),0);shuffle(k.begin(),k.end(),rng);float sc=potential(dec(ct,k));for(int it=0;it<100000;it++){auto kk=k;int x=rng()%w2,y=rng()%w2;swap(kk[x],kk[y]);if(it%5==0){if(x>y)swap(x,y);reverse(kk.begin()+x,kk.begin()+y+1);}if(it%5==1){int v=kk[x];kk.erase(kk.begin()+x);kk.insert(kk.begin()+y,v);}if(it%5==2){int off=rng()%w2;rotate(kk.begin(),kk.begin()+off,kk.end());}float ns=potential(dec(ct,kk));float t=.1+12.0*(1.0-(it%10000)/10000.0);if(ns>sc||uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/t)){k=kk;sc=ns;}if(sc>best){best=sc;bk=k;}}}string mid=dec(ct,bk);auto a=pairs(mid);float bestpath=-1e9;vector<int>order;for(int restart=0;restart<100;restart++){vector<int>k(w1);iota(k.begin(),k.end(),0);shuffle(k.begin(),k.end(),rng);float sc=pathscore(k,a);for(int it=0;it<10000;it++){auto kk=k;int x=rng()%w1,y=rng()%w1;swap(kk[x],kk[y]);float ns=pathscore(kk,a);float t=.1+4.0*(1.0-(it%2000)/2000.0);if(ns>sc||uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/t)){k=kk;sc=ns;}if(sc>bestpath){bestpath=sc;order=k;}}}int h=ct.size()/w1;string plain;for(int r=0;r<h;r++)for(int c:order)plain+=mid[c*h+r];cout<<best<<" "<<bestpath<<" "<<plain<<endl;for(int c:bk)cout<<c<<",";cout<<endl;for(int c:order)cout<<c<<",";cout<<endl;}
