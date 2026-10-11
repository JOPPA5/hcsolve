#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <random>
#include <numeric>
#include <cmath>
using namespace std;
float q[26*26*26*26];
mt19937 rng(399);
int id(string s){int r=0;for(char c:s)r=r*26+c-'a';return r;}
string dec(string s,const vector<int>&k){int n=s.size(),w=k.size(),h=n/w,r=n%w,at=0;string out(n,' ');for(int c:k)for(int y=0;y<h+(c<r);y++)out[y*w+c]=s[at++];return out;}
string decrypt(string s,const vector<vector<int>>&keys){for(int k=keys.size()-1;k>=0;k--)s=dec(s,keys[k]);return s;}
float score(const string&s){float r=0;for(int i=0;i+3<(int)s.size();i++)r+=q[((s[i]-'a')*26+s[i+1]-'a')*26*26+(s[i+2]-'a')*26+s[i+3]-'a'];return r;}
int main(int argc,char**argv){if(argc<7)return 2;ifstream f(argv[1]);string t;float v;fill(begin(q),end(q),-4.0);while(f>>t>>v)q[id(t)]=v;ifstream c(argv[2]);string ct;c>>ct;int restarts=stoi(argv[3]),steps=stoi(argv[4]);vector<int> widths;for(int a=5;a<argc;a++)widths.push_back(stoi(argv[a]));if(widths.back()==0)widths.pop_back();float best=-1e9;vector<vector<int>>bk;string bt;
for(int r=0;r<restarts;r++){vector<vector<int>>k;for(int w:widths){vector<int>x(w);iota(x.begin(),x.end(),0);shuffle(x.begin(),x.end(),rng);k.push_back(x);}float sc=score(decrypt(ct,k));for(int it=0;it<steps;it++){auto kk=k;auto &layer=kk[rng()%kk.size()];int w=layer.size(),a=rng()%w,b=rng()%w;if(a>b)swap(a,b);switch(rng()%4){case 0:swap(layer[a],layer[b]);break;case 1:reverse(layer.begin()+a,layer.begin()+b+1);break;case 2:rotate(layer.begin()+a,layer.begin()+a+1,layer.begin()+b+1);break;case 3:rotate(layer.begin(),layer.begin()+a,layer.end());break;}string pt=decrypt(ct,kk);float ns=score(pt),temp=.4+18.0*(1.0-(it%10000)/10000.0);if(ns>sc||uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/temp)){k=kk;sc=ns;}if(sc>best){best=sc;bk=k;bt=decrypt(ct,k);}}}
cout<<"score "<<best<<"\n";for(auto&k:bk){for(int x:k)cout<<x<<",";cout<<"\n";}cout<<bt<<"\n";return 0;
}
