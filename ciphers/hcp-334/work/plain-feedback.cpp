#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <random>
#include <set>
#include <string>
#include <vector>
using namespace std;
float q[456976];
int mod(int x){x%=26;return x<0?x+26:x;}
int main(int argc,char**argv){ifstream model(argv[1]);fill(begin(q),end(q),-4);string s;float v;while(model>>s>>v){int a=0;for(char c:s)a=a*26+c-'a';q[a]=v;}ifstream src(argv[2]);src>>s;string family=argv[3];int lo=stoi(argv[4]),hi=stoi(argv[5]),restarts=stoi(argv[6]),steps=stoi(argv[7]),N=s.size();int a=family=="reverse-subtract"?-1:1,b=family=="subtract"?-1:1;mt19937 rng(334612);auto win=[&](const vector<int>&p,int i){return q[((p[i]*26+p[i+1])*26+p[i+2])*26+p[i+3]];};for(int w=lo;w<=hi;w++){int gaps=count(s.begin()+min(w,N),s.end(),'?'),V=w+gaps;vector<vector<int>>coef(N,vector<int>(V));vector<int>constant(N);int next=w;for(int i=0;i<N;i++){if(i<w){coef[i][i]=1;continue;}for(int j=0;j<V;j++)coef[i][j]=b*coef[i-w][j];constant[i]=mod(b*constant[i-w]);if(s[i]=='?')coef[i][next++]=a;else constant[i]=mod(constant[i]+a*(s[i]-'a'));}vector<vector<int>>positions(V),wins(V);for(int j=0;j<V;j++){set<int>ss;for(int i=0;i<N;i++)if(coef[i][j]){positions[j].push_back(i);for(int t=max(0,i-3);t<=min(i,N-4);t++)ss.insert(t);}wins[j]={ss.begin(),ss.end()};}float best=-1e9;vector<int>bk,bp;for(int r=0;r<restarts;r++){vector<int>key(V),p=constant;for(int &x:key)x=rng()%26;for(int i=0;i<N;i++){for(int j=0;j<V;j++)p[i]+=coef[i][j]*key[j];p[i]=mod(p[i]);}float sc=0;for(int i=0;i+3<N;i++)sc+=win(p,i);for(int t=0;t<steps;t++){int j=rng()%V,nk=rng()%26,delta=nk-key[j];float before=0,after=0;for(int i:wins[j])before+=win(p,i);for(int i:positions[j])p[i]=mod(p[i]+coef[i][j]*delta);for(int i:wins[j])after+=win(p,i);float ds=after-before,temp=.2+5*(1.-(t%3000)/3000.);if(ds>=0||uniform_real_distribution<float>(0,1)(rng)<exp(ds/temp)){sc+=ds;key[j]=nk;}else for(int i:positions[j])p[i]=mod(p[i]-coef[i][j]*delta);if(sc>best){best=sc;bk=key;bp=p;}}}cout<<w<<" "<<best<<" ";for(int x:bk)cout<<x<<",";cout<<" ";for(int x:bp)cout<<char('a'+x);cout<<endl;}}
