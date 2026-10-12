#include <algorithm>
#include <array>
#include <cmath>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <vector>
using namespace std;string enc(const string&p,const vector<int>&k){string o;for(int col:k)for(int i=col;i<(int)p.size();i+=k.size())o+=p[i];return o;}string dec(const string&s,const vector<int>&k){string o(s.size(),' ');int at=0;for(int col:k)for(int i=col;i<(int)s.size();i+=k.size())o[i]=s[at++];return o;}
int pb2[676]={},pb3[17576]={},cb2[676]={},cb3[17576]={},st2[676]={},st3[17576]={},generation=0;
struct Features{int h,b2,b3;double score(double weight)const{return weight*h+2*b2+3*b3;}};
Features evaluate(const vector<vector<int>>&keys,const string&p,const string&c){string x=c;for(int j=2;j>=0;j--)x=dec(x,keys[j]);Features f{0,0,0};generation++;for(int i=0;i<50;i++){f.h+=p[i]==x[i];if(i+1<50){int code=(x[i]-'a')*26+x[i+1]-'a';if(st2[code]!=generation)st2[code]=generation,cb2[code]=0;f.b2+=cb2[code]++<pb2[code];}if(i+2<50){int code=((x[i]-'a')*26+x[i+1]-'a')*26+x[i+2]-'a';if(st3[code]!=generation)st3[code]=generation,cb3[code]=0;f.b3+=cb3[code]++<pb3[code];}}return f;}
void mutate(vector<int>&k,mt19937&r){int n=k.size(),a=r()%n,b=r()%n;if(a>b)swap(a,b);int mode=r()%100;if(mode<55)swap(k[a],k[b]);else if(mode<75){if(a<b)rotate(k.begin()+a,k.begin()+a+1,k.begin()+b+1);}else if(mode<85)reverse(k.begin()+a,k.begin()+b+1);else{int size=1+r()%min(5,n/3);int x=r()%(n-size+1),y=r()%(n-size+1);if(abs(x-y)>=size)for(int i=0;i<size;i++)swap(k[x+i],k[y+i]);}}
int main(int argc,char**argv){ifstream in(argv[1]);string p,c;in>>p>>c;mt19937 rng(stoi(argv[2]));int restarts=stoi(argv[3]),steps=stoi(argv[4]);for(int i=0;i<50;i++){if(i+1<50)pb2[(p[i]-'a')*26+p[i+1]-'a']++;if(i+2<50)pb3[((p[i]-'a')*26+p[i+1]-'a')*26+p[i+2]-'a']++;}int best=0;vector<vector<int>>saved;int ws[3]={21,19,20};for(int rr=0;rr<restarts;rr++){vector<vector<int>>keys(3);for(int j=0;j<3;j++){keys[j].resize(ws[j]);iota(keys[j].begin(),keys[j].end(),0);shuffle(keys[j].begin(),keys[j].end(),rng);}auto now=evaluate(keys,p,c);for(int it=0;it<steps;it++){auto next=keys;mutate(next[rng()%3],rng);if(rng()%50==0)mutate(next[rng()%3],rng);auto q=evaluate(next,p,c);double phase=double(it%10000)/10000.,weight=.5+9.5*phase,temp=.2+12.*(1.-phase);if(q.score(weight)>=now.score(weight)||log((rng()+1.)/4294967297.)<(q.score(weight)-now.score(weight))/temp)keys=next,now=q;if(now.h>best){best=now.h;saved=keys;cerr<<rr<<' '<<it<<' '<<best<<' '<<now.b2<<' '<<now.b3<<'\n';}if(best==50)goto done;}}done:cout<<best<<'\n';for(auto k:saved){for(int v:k)cout<<v<<' ';cout<<'\n';}string out=p;for(auto k:saved)out=enc(out,k);cout<<out<<'\n';}
