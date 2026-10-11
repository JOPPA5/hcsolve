#include <algorithm>
#include <array>
#include <cmath>
#include <fstream>
#include <iostream>
#include <numeric>
#include <queue>
#include <random>
#include <string>
#include <vector>
using namespace std;
mt19937 rng(610363);
float bi[26][26];vector<float> gram[6];
void load(string dir,string big){ifstream f(big);string s;float v;while(f>>s>>v)bi[s[0]-'a'][s[1]-'a']=v;for(int n=3;n<=5;n++){ifstream g(dir+"/model"+to_string(n)+".tsv");string tag;float floor;g>>tag>>floor;int total=1;for(int i=0;i<n;i++)total*=26;gram[n].assign(total,floor);while(g>>s>>v){int ix=0;for(char c:s)ix=ix*26+c-'a';gram[n][ix]=v;}}}
float language(const string&s){float sc=0,wt[]={0,0,0,.15,.4,.8};for(int n=3;n<=5;n++){int ix=0,pow=1;for(int j=1;j<n;j++)pow*=26;for(int i=0;i<(int)s.size();i++){if(i>=n)ix-=(s[i-n]-'a')*pow;ix=ix*26+s[i]-'a';if(i>=n-1)sc+=wt[n]*gram[n][ix];}}return sc;}
struct Seg{vector<string>chunks;vector<int>order;float score;bool operator<(const Seg&s)const{return score>s.score;}};
string decode(const vector<string>&chunks,const vector<int>&order){string p;int h=chunks[0].size();for(auto&c:chunks)h=max(h,(int)c.size());for(int r=0;r<h;r++)for(int col:order)if(r<(int)chunks[col].size())p+=chunks[col][r];return p;}
string plain(const Seg&s){return decode(s.chunks,s.order);}
void mutate(vector<int>&k,int split){int low=0,high=k.size();if(split>0&&split<(int)k.size()){if(rng()%2)high=split;else low=split;}if(high-low<2)return;int a=low+rng()%(high-low),b=low+rng()%(high-low);if(a>b)swap(a,b);switch(rng()%4){case 0:swap(k[a],k[b]);break;case 1:reverse(k.begin()+a,k.begin()+b+1);break;case 2:{int x=k[a];k.erase(k.begin()+a);k.insert(k.begin()+b,x);break;}default:{vector<int>block(k.begin()+a,k.begin()+b+1);k.erase(k.begin()+a,k.begin()+b+1);int dest=low+rng()%(high-low-block.size()+1);k.insert(k.begin()+dest,block.begin(),block.end());}}}
int main(int argc,char**argv){load(argv[1],argv[2]);ifstream f(argv[3]);string ct;f>>ct;int w=stoi(argv[4]),extra=ct.size()%w,h=ct.size()/w;int split=extra?extra:w;vector<int>pattern(w);fill(pattern.end()-extra,pattern.end(),1);priority_queue<Seg>pool;long patterns=0;float global=-1e9;Seg winner;
do{Seg s;int at=0;vector<int>L,S;for(int i=0;i<w;i++){int len=h+pattern[i];s.chunks.push_back(ct.substr(at,len));at+=len;(pattern[i]?L:S).push_back(i);}if(extra==0){L=S;S.clear();}float adj[32][32]{},wrap[32][32]{};for(int a=0;a<w;a++)for(int b=0;b<w;b++){auto&x=s.chunks[a];auto&y=s.chunks[b];for(int r=0;r<min(x.size(),y.size());r++)adj[a][b]+=bi[x[r]-'a'][y[r]-'a'];for(int r=0;r<(int)x.size()&&r+1<(int)y.size();r++)wrap[a][b]+=bi[x[r]-'a'][y[r+1]-'a'];}
auto score=[&](const vector<int>&k){float v=wrap[k.back()][k.front()];for(int i=0;i+1<w;i++)v+=adj[k[i]][k[i+1]];return v;};float best=-1e9;vector<int>bestorder;
for(int rep=0;rep<5;rep++){shuffle(L.begin(),L.end(),rng);shuffle(S.begin(),S.end(),rng);vector<int>k=L;k.insert(k.end(),S.begin(),S.end());float sc=score(k);for(int it=0;it<1500;it++){auto kk=k;mutate(kk,split);float ns=score(kk),temp=.5+12*(1.-(it%500)/500.);if(ns>sc||uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/temp)){k=kk;sc=ns;}if(sc>best){best=sc;bestorder=k;}}}s.order=bestorder;s.score=best;if(pool.size()<40)pool.push(s);else if(best>pool.top().score){pool.pop();pool.push(s);}patterns++;}while(next_permutation(pattern.begin(),pattern.end()));
vector<Seg>seeds;while(!pool.empty()){seeds.push_back(pool.top());pool.pop();}reverse(seeds.begin(),seeds.end());cerr<<"patterns="<<patterns<<" retained="<<seeds.size()<<"\n";
for(int r=0;r<(int)seeds.size();r++){auto s=seeds[r];float sc=language(plain(s));for(int it=0;it<100000;it++){auto k=s.order;mutate(k,split);float ns=language(decode(s.chunks,k)),temp=1+100*pow(1.-(it%20000)/20000.,2);if(ns>sc||uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/temp)){s.order=k;sc=ns;}if(sc>global){global=sc;winner=s;}}if(r%10==0)cerr<<"seed="<<r<<" best="<<global<<" "<<plain(winner).substr(0,80)<<"\n";}
cout<<w<<" "<<global<<" key=";vector<int>reading(w);for(int i=0;i<w;i++)reading[winner.order[i]]=i;for(int x:reading)cout<<x<<",";cout<<" "<<plain(winner)<<"\n";cout<<"pattern=";for(auto&c:winner.chunks)cout<<(c.size()>h?1:0);cout<<" physical_chunk_order=";for(int x:winner.order)cout<<x<<",";cout<<"\n";}
