#include <iostream>
#include <fstream>
#include <vector>
#include <array>
#include <algorithm>
#include <random>
#include <cmath>
#include <string>
#include <utility>
using namespace std; using Key=vector<int>; using Keys=array<Key,3>;
vector<float> gram[6];
void load(string d){for(int n=3;n<=5;n++){ifstream f(d+"/model"+to_string(n)+".tsv");string s;float v;f>>s>>v;int z=1;for(int i=0;i<n;i++)z*=26;gram[n].assign(z,v);while(f>>s>>v){int x=0;for(char c:s)x=x*26+c-'a';gram[n][x]=v;}}}
float score(string s){float z=0,w[]={0,0,0,.15,.4,.8};for(int n=3;n<=5;n++){int x=0,p=1;for(int j=1;j<n;j++)p*=26;for(int i=0;i<(int)s.size();i++){if(i>=n)x-=(s[i-n]-'a')*p;x=x*26+s[i]-'a';if(i>=n-1)z+=w[n]*gram[n][x];}}return z;}
void canon(Key& k){rotate(k.begin(),find(k.begin(),k.end(),1),k.end());}
// Independent inverse: determine physical rank at alignment, then interleave columns.
string inv(string s,Key k,int n){int w=k.size(),pivot=find(k.begin(),k.end(),n)-k.begin();vector<string> col(w);int at=0;for(int rank=1;rank<=w;rank++){int original=find(k.begin(),k.end(),rank)-k.begin();int physical=(original-pivot+w)%w;int len=s.size()/w+(physical<(int)s.size()%w);col[physical]=s.substr(at,len);at+=len;}string out;for(int row=0;row<((int)s.size()+w-1)/w;row++)for(auto &c:col)if(row<(int)c.size())out+=c[row];return out;}
vector<pair<int,string>> payloads;
vector<string> plain(Keys k){vector<string> out;for(auto [n,c]:payloads){for(int j=2;j>=0;j--)c=inv(c,k[j],n);out.push_back(c);}return out;}
float objective(Keys k){float s=0;for(auto p:plain(k))s+=score(p);return s;}
int main(int argc,char**argv){load(argv[1]);ifstream in(argv[2]),kf(argv[3]);int n;string s;while(in>>n>>s)payloads.push_back({n,s});Keys truth;for(int j=0;j<3;j++){truth[j].resize(j==0?21:j==1?19:20);for(int& x:truth[j])kf>>x;}cout<<"truth score "<<objective(truth)<<"\n";for(auto p:plain(truth))cout<<"verified "<<p<<"\n";if(stoi(argv[4])==-1)return 0;int mode=stoi(argv[4]),starts=stoi(argv[5]),steps=stoi(argv[6]);mt19937 rng(619395+mode);float overall=-1e20;Keys best;for(int run=0;run<starts;run++){Keys k=truth;for(int j=0;j<3;j++)if(mode==3||mode==j){shuffle(k[j].begin(),k[j].end(),rng);canon(k[j]);}float sc=objective(k),top=sc;Keys peak=k;for(int it=0;it<steps;it++){int j=mode==3?rng()%3:mode;Key old=k[j];int w=old.size(),a=rng()%w,b=rng()%w;if(a>b)swap(a,b);if(rng()%3==0)reverse(k[j].begin()+a,k[j].begin()+b+1);else if(rng()%2)swap(k[j][a],k[j][b]);else if(a<b)rotate(k[j].begin()+a,k[j].begin()+a+1,k[j].begin()+b+1);canon(k[j]);float ns=objective(k);float temp=18*pow(.015,(it%(steps/4+1))/double(steps/4+1));if(ns>=sc||log((rng()+1.0)/4294967297.0)<(ns-sc)/temp){sc=ns;if(sc>top){top=sc;peak=k;}}else k[j]=old;}if(top>overall){overall=top;best=peak;}int exact=0;auto pt=plain(truth),pp=plain(peak);for(int i=0;i<(int)pt.size();i++)for(int q=0;q<(int)pt[i].size();q++)exact+=pt[i][q]==pp[i][q];cout<<"run "<<run<<" score "<<top<<" matches "<<exact<<"/250 keys "<<(peak==truth)<<"\n"<<flush;}cout<<"BEST "<<overall<<"\n";for(auto k:best){for(int x:k)cout<<x<<' ';cout<<'\n';}for(auto p:plain(best))cout<<p<<'\n';return 0;}
