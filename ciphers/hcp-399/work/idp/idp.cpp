// IDP algorithm adapted from CrypTool 2 IDPAnalyser.cs, Apache-2.0.
// Copyright (C) CrypTool 2 Team. New C++ control/search integration: GPT-6.1 Sol.
// Negative log scores require -infinity maxima instead of the upstream positive-score zero floor.
#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <set>
#include <string>
#include <vector>
using namespace std;
using Key=vector<int>;float bi[26][26];int width,nrows,nletters;vector<pair<int,int>> ranges;mt19937 rng(613993);
string dec(const string&s,const Key&k){string p(s.size(),' ');int at=0;for(int c:k)for(int pos=c;pos<(int)s.size();pos+=k.size())p[pos]=s[at++];assert(at==s.size());return p;}
void prepare(int n,int w){width=w;nletters=n;nrows=n/w;int longcols=n%w;ranges.clear();for(int i=0;i<w;i++){int lo=nrows*(i+1)-1+max(0,longcols-(w-i-1));int hi=nrows*(i+1)-1+min(i+1,longcols);ranges.push_back({lo-nrows+1,hi-nrows+1});}}
float potential(const string&s){struct Edge{float val;int a,b;};Edge edges[32*32];int size=0;for(int a=0;a<width;a++)for(int b=0;b<width;b++)if(a!=b){float best=-1e9;for(int pa=ranges[a].first;pa<=ranges[a].second;pa++)for(int pb=ranges[b].first;pb<=ranges[b].second;pb++){float z=0;for(int r=0;r<nrows;r++)z+=bi[s[pa+r]-'a'][s[pb+r]-'a'];best=max(best,z/nrows);}edges[size++]={best,a,b};}sort(edges,edges+size,[](auto&a,auto&b){if(a.val!=b.val)return a.val>b.val;return a.a!=b.a?a.a<b.a:a.b<b.b;});int left[32],right[32];fill(left,left+width,-1);fill(right,right+width,-1);float total=0;int selected=0;for(int e=0;e<size&&selected<width;e++){int a=edges[e].a,b=edges[e].b;if(right[a]>=0||left[b]>=0)continue;bool cycle=false;if(selected<width-1){int cur=a;while(left[cur]>=0){cur=left[cur];if(cur==b){cycle=true;break;}}}if(cycle)continue;left[b]=a;right[a]=b;total+=edges[e].val;selected++;}if(selected==width-1){int a=0,b=0;while(right[a]>=0)a++;while(left[b]>=0)b++;for(int i=0;i<size;i++)if(edges[i].a==a&&edges[i].b==b){total+=edges[i].val;selected++;break;}}assert(selected==width);return total/width;}
vector<Key> transforms(int w){set<Key> unique;Key identity(w);iota(identity.begin(),identity.end(),0);auto add=[&](Key k){if(k!=identity)unique.insert(k);};for(int a=0;a<w;a++)for(int b=a+1;b<=w;b++)for(int c=b+1;c<=w;c++){auto k=identity;rotate(k.begin()+a,k.begin()+b,k.begin()+c);add(k);}for(int a=0;a<w;a++)for(int b=a+1;b<=w;b++)for(int c=b;c<w;c++)for(int d=c+1;d<=w;d++){Key k;k.insert(k.end(),identity.begin(),identity.begin()+a);k.insert(k.end(),identity.begin()+c,identity.begin()+d);k.insert(k.end(),identity.begin()+b,identity.begin()+c);k.insert(k.end(),identity.begin()+a,identity.begin()+b);k.insert(k.end(),identity.begin()+d,identity.end());add(k);}for(int a=0;a<w;a++)for(int b=a+1;b<w;b++){auto k=identity;swap(k[a],k[b]);add(k);}return vector<Key>(unique.begin(),unique.end());}
Key transformKey(const Key&k,const Key&t){Key out;for(int x:t)out.push_back(k[x]);return out;}
struct Cand{float sc;Key k;};
int main(int argc,char**argv){ifstream big(argv[1]);string s;float v;while(big>>s>>v)bi[s[0]-'a'][s[1]-'a']=v;ifstream f(argv[2]);string ct;f>>ct;int w1=stoi(argv[3]),w2=stoi(argv[4]);prepare(ct.size(),w1);if(argc>5&&string(argv[5])=="score"){cout<<potential(ct)<<"\n";return 0;}auto ts=transforms(w2);cerr<<"transformations="<<ts.size()<<endl;int randomcount=argc>5?stoi(argv[5]):4000;vector<Cand>pool;Key k(w2);iota(k.begin(),k.end(),0);for(int i=0;i<randomcount;i++){shuffle(k.begin(),k.end(),rng);pool.push_back({potential(dec(ct,k)),k});}sort(pool.begin(),pool.end(),[](auto&a,auto&b){return a.sc>b.sc;});pool.resize(min(64,(int)pool.size()));for(auto&c:pool){for(int i=0;i<w2-1;i++)for(int j=i+1;j<w2;j++){auto kk=c.k;swap(kk[i],kk[j]);float sc=potential(dec(ct,kk));if(sc>c.sc){c={sc,kk};}}}sort(pool.begin(),pool.end(),[](auto&a,auto&b){return a.sc>b.sc;});pool.resize(min(16,(int)pool.size()));vector<Cand>finals;for(int rep=0;rep<(int)pool.size();rep++){auto c=pool[rep];for(int iteration=0;iteration<30;iteration++){Cand best=c;for(auto&t:ts){auto kk=transformKey(c.k,t);float sc=potential(dec(ct,kk));if(sc>best.sc+1e-6)best={sc,kk};}if(best.sc<=c.sc+1e-6)break;c=best;cerr<<"seed="<<rep<<" round="<<iteration<<" idp="<<c.sc<<endl;}finals.push_back(c);}sort(finals.begin(),finals.end(),[](auto&a,auto&b){return a.sc>b.sc;});for(int i=0;i<(int)finals.size();i++){cout<<i<<" idp="<<finals[i].sc<<" outer=";for(int x:finals[i].k)cout<<x<<",";cout<<" "<<dec(ct,finals[i].k)<<"\n";}return 0;}
