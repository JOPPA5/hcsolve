#include <algorithm>
#include <array>
#include <cmath>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <vector>
using namespace std;
string enc(const string&p,const vector<int>&k){string x;for(int col:k)for(int i=col;i<p.size();i+=k.size())x+=p[i];return x;}
struct Fit{int score,matches;vector<int>last;};
Fit fit(const string&p,const string&c){int freq[26]={0};for(char x:c)freq[x-'a']++;int a[21][21]={};for(int col=1;col<=20;col++)for(int r=1;r<=20;r++)for(int row=0;row<3;row++)if(p[col-1+20*row]==c[(r-1)*3+row])a[col][r]-=freq[c[(r-1)*3+row]-'a']==1?4:1;
 int u[21]={},v[21]={},pcol[21]={},way[21]={};for(int i=1;i<=20;i++){pcol[0]=i;int j0=0,minv[21];bool used[21]={};fill(minv,minv+21,100000);do{used[j0]=true;int i0=pcol[j0],delta=100000,j1=0;for(int j=1;j<=20;j++)if(!used[j]){int cur=a[i0][j]-u[i0]-v[j];if(cur<minv[j])minv[j]=cur,way[j]=j0;if(minv[j]<delta)delta=minv[j],j1=j;}for(int j=0;j<=20;j++)if(used[j])u[pcol[j]]+=delta,v[j]-=delta;else minv[j]-=delta;j0=j1;}while(pcol[j0]!=0);do{int j1=way[j0];pcol[j0]=pcol[j1];j0=j1;}while(j0);}
 vector<int>k;int score=0;for(int j=1;j<=20;j++){k.push_back(pcol[j]-1);score-=a[pcol[j]][j];}string y=enc(p,k);int matches=0;for(int i=0;i<60;i++)matches+=y[i]==c[i];return{score,matches,k};}
void mutate(vector<int>&v,mt19937&rng){int mode=rng()%100;if(mode<85)swap(v[rng()%v.size()],v[rng()%v.size()]);else if(mode<93){int a=rng()%v.size(),b=rng()%v.size(),c=rng()%v.size();swap(v[a],v[b]);swap(v[b],v[c]);}else{int a=rng()%v.size(),b=rng()%v.size();if(a>b)swap(a,b);if(a<b)rotate(v.begin()+a,v.begin()+a+1,v.begin()+b+1);}}
int main(int argc,char**argv){ifstream f(argv[1]);string plain,cipher;f>>plain>>cipher;int seed=stoi(argv[2]),steps=stoi(argv[3]),restarts=stoi(argv[4]);mt19937 rng(seed);int best=-1;vector<int>best1,best2,best3;for(int r=0;r<restarts;r++){vector<int>a(21),b(19);for(int i=0;i<21;i++)a[i]=i;for(int i=0;i<19;i++)b[i]=i;shuffle(a.begin(),a.end(),rng);shuffle(b.begin(),b.end(),rng);auto now=fit(enc(enc(plain,a),b),cipher);for(int it=0;it<steps;it++){auto na=a,nb=b;if(rng()%2)mutate(na,rng);else mutate(nb,rng);if(rng()%20==0){mutate(na,rng);mutate(nb,rng);}auto nf=fit(enc(enc(plain,na),nb),cipher);double temp=.15+2.2*(1.-(it%10000)/10000.);if(nf.score>=now.score||log((rng()+1.)/4294967297.)<(nf.score-now.score)/temp){a=na;b=nb;now=nf;}if(now.score>best){best=now.score;best1=a;best2=b;best3=now.last;cerr<<r<<' '<<it<<' '<<best<<' '<<now.matches<<'\n';}if(now.matches==60)goto done;}}
 done:cout<<best<<'\n';for(auto&v:{best1,best2,best3}){for(int x:v)cout<<x<<' ';cout<<'\n';}cout<<enc(enc(enc(plain,best1),best2),best3)<<'\n';}
