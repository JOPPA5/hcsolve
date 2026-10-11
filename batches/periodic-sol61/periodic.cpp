// Reuses formula families from HCP332 exact_periodic/reciprocal.cpp.
// New combined frozen 3/4/5-gram scorer, erasure-aware incremental windows,
// monogram blind starts and exhaustive residue coordinate refinement.
#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <vector>
#include <sstream>
using namespace std;vector<float>gram[6];array<float,26>frequency;mt19937 rng(619369);
void load(string dir,string freqs){for(int n=3;n<=5;n++){ifstream f(dir+"/model"+to_string(n)+".tsv");assert(f);string s;float v;f>>s>>v;int total=1;for(int i=0;i<n;i++)total*=26;gram[n].assign(total,v);while(f>>s>>v){int ix=0;for(char c:s)ix=ix*26+c-'a';gram[n][ix]=v;}}ifstream f(freqs);char c;float x;float total=0;frequency.fill(1);while(f>>c>>x){frequency[c-'a']=x+1;total+=x+1;}for(float&v:frequency)v=log(v/total);}
int transform(int c,int k,string mode){if(c<0)return -1;if(mode=="vigenere")return (c-k+26)%26;if(mode=="variant")return (c+k)%26;if(mode=="beaufort")return (k-c+26)%26;return c<13?13+(c-k+13)%13:(c-13+k)%13;}
struct Window{int start,n;float weight;};struct Cand{float score;vector<int>key;string plain;};
struct Task{string ct,mode;int T,A;vector<int>cipher,plain;vector<Window>windows;vector<vector<int>>affected;vector<float>cache;float total;Task(string s,string m,int t):ct(s),mode(m),T(t),A(m=="porta"?13:26){for(char c:s)cipher.push_back(c=='.'?-1:c-'a');plain=cipher;float weights[]={0,0,0,.15,.4,.8};for(int n=3;n<=5;n++)for(int i=0;i+n<=s.size();i++){bool valid=true;for(int j=0;j<n;j++)if(cipher[i+j]<0)valid=false;if(valid)windows.push_back({i,n,weights[n]});}affected.resize(T);for(int wi=0;wi<windows.size();wi++){auto w=windows[wi];for(int r=0;r<T;r++){bool included=false;for(int j=0;j<w.n;j++)if((w.start+j)%T==r)included=true;if(included)affected[r].push_back(wi);}}cache.resize(windows.size());}
float value(int i){auto w=windows[i];int ix=0;for(int j=0;j<w.n;j++)ix=ix*26+plain[w.start+j];return w.weight*gram[w.n][ix];}
void initialize(vector<int>key){for(int i=0;i<cipher.size();i++)plain[i]=transform(cipher[i],key[i%T],mode);total=0;for(int i=0;i<windows.size();i++){cache[i]=value(i);total+=cache[i];}}
float change(int r,int k){float before=0,after=0;for(int i:affected[r])before+=cache[i];for(int i=r;i<plain.size();i+=T)plain[i]=transform(cipher[i],k,mode);for(int i:affected[r])after+=value(i);return total-before+after;}
void commit(int r,float score){for(int i:affected[r])cache[i]=value(i);total=score;}
string text(){string s;for(int v:plain)s+=v<0?'.':char('a'+v);return s;}
vector<int> mono(){vector<int>k(T);for(int r=0;r<T;r++){float best=-1e30;for(int x=0;x<A;x++){float sc=0;for(int i=r;i<cipher.size();i+=T)if(cipher[i]>=0)sc+=frequency[transform(cipher[i],x,mode)];if(sc>best){best=sc;k[r]=x;}}}return k;}
};
void keep(vector<Cand>&p,float score,vector<int>key,string text){for(auto c:p)if(c.plain==text)return;if(p.size()<4||score>p.back().score){p.push_back({score,key,text});sort(p.begin(),p.end(),[](auto&a,auto&b){return a.score>b.score;});if(p.size()>4)p.pop_back();}}
vector<Cand> solve(string ct,string mode,int T,int restarts,int steps){Task task(ct,mode,T);vector<Cand>pool;if(T<=3){long size=1;for(int i=0;i<T;i++)size*=task.A;for(long v=0;v<size;v++){long x=v;vector<int>key(T);for(int&r:key){r=x%task.A;x/=task.A;}task.initialize(key);if(pool.size()<4||task.total>pool.back().score)keep(pool,task.total,key,task.text());}return pool;}auto mono=task.mono();for(int restart=0;restart<restarts;restart++){auto key=mono;for(int i=0;i<T;i++)if(restart>=4|| (restart>0&&rng()%5==0))key[i]=rng()%task.A;task.initialize(key);keep(pool,task.total,key,task.text());for(int it=0;it<steps;it++){int r=rng()%T,old=key[r],v=rng()%task.A;float ns=task.change(r,v),temp=.3+15*(1.-it/double(steps));if(ns>=task.total||log((rng()+1.)/4294967297.)<(ns-task.total)/temp){key[r]=v;task.commit(r,ns);if(pool.size()<4||ns>pool.back().score)keep(pool,ns,key,task.text());}else for(int i=r;i<task.plain.size();i+=T)task.plain[i]=transform(task.cipher[i],old,mode);}for(int pass=0;pass<3;pass++){bool improved=false;for(int r=0;r<T;r++){float best=task.total;int choice=key[r];for(int v=0;v<task.A;v++){float ns=task.change(r,v);if(ns>best+.001){best=ns;choice=v;}}task.change(r,choice);if(best>task.total+.001)improved=true;key[r]=choice;task.commit(r,best);}keep(pool,task.total,key,task.text());if(!improved)break;}}return pool;}
int main(int argc,char**argv){load(argv[1],argv[2]);ifstream in(argv[3]);string line;while(getline(in,line)){istringstream ss(line);string label,kind,ct;int restarts,steps;ss>>label>>kind>>ct>>restarts>>steps;assert(!ct.empty());vector<string>modes=kind=="all"?vector<string>{"vigenere","beaufort","porta"}:vector<string>{kind};for(auto mode:modes)for(int T=1;T<=16;T++){auto pool=solve(ct,mode,T,restarts,steps);for(int rank=0;rank<pool.size();rank++){auto c=pool[rank];auto emit=[&](string name,vector<int>key){cout<<label<<'\t'<<name<<'\t'<<T<<'\t'<<rank<<'\t'<<c.score<<'\t';for(int i=0;i<key.size();i++)cout<<(i?",":"")<<key[i];cout<<'\t'<<c.plain<<'\n';};emit(mode,c.key);if(kind=="all"&&mode=="vigenere"){auto key=c.key;for(int&v:key)v=(26-v)%26;emit("variant",key);}}}cout<<flush;cerr<<label<<" done\n"<<flush;}return 0;}
