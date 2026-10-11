#include <algorithm>
#include <array>
#include <cmath>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>
using namespace std;float q[456976];double lp[26];string ct;int T;mt19937 rng(33452);vector<array<int,26>>H;vector<int>R,bR,bK;float best=-1e9;long long countkeys=0;
vector<int>hungarian(vector<int>&R){double a[27][27]={};for(int c=0;c<26;c++)for(int pos=0;pos<26;pos++)for(int r=0;r<T;r++)a[c+1][pos+1]-=H[r][c]*lp[(pos-R[r]+26)%26];double u[27]={},v[27]={};int p[27]={},way[27]={};for(int i=1;i<=26;i++){p[0]=i;int j0=0;double minv[27];bool used[27]={};fill(minv,minv+27,1e99);do{used[j0]=true;int i0=p[j0],j1=0;double delta=1e99;for(int j=1;j<=26;j++)if(!used[j]){double cur=a[i0][j]-u[i0]-v[j];if(cur<minv[j]){minv[j]=cur;way[j]=j0;}if(minv[j]<delta){delta=minv[j];j1=j;}}for(int j=0;j<=26;j++)if(used[j]){u[p[j]]+=delta;v[j]-=delta;}else minv[j]-=delta;j0=j1;}while(p[j0]);do{int j1=way[j0];p[j0]=p[j1];j0=j1;}while(j0);}vector<int>K(26);for(int j=1;j<=26;j++)K[p[j]-1]=j-1;return K;}
string dec(vector<int>&K,vector<int>&R){string s=ct;for(int i=0;i<s.size();i++){int c=ct[i]-'a';s[i]=c<0||c>=26?'?':'a'+(K[c]-R[i%T]+26)%26;}return s;}
float score(string s){float sc=0;for(int i=0;i+3<s.size();i++){if(s[i]=='?'||s[i+1]=='?'||s[i+2]=='?'||s[i+3]=='?')continue;sc+=q[((s[i]-'a')*26+s[i+1]-'a')*676+(s[i+2]-'a')*26+s[i+3]-'a'];}return sc;}
void enumerate(int pos){if(pos<T){for(int x=0;x<26;x++){R[pos]=x;enumerate(pos+1);}return;}countkeys++;auto seed=hungarian(R);for(int r=0;r<6;r++){auto K=seed;for(int j=0;j<r;j++)swap(K[rng()%26],K[rng()%26]);float sc=score(dec(K,R));for(int it=0;it<10000;it++){auto kk=K;swap(kk[rng()%26],kk[rng()%26]);float ns=score(dec(kk,R)),temp=.2+9*(1.-it/10000.);if(ns>sc||uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/temp)){K=kk;sc=ns;}if(sc>best){best=sc;bK=K;bR=R;}}}}
int main(int argc,char**argv){fill(begin(q),end(q),-4);double freq[26]={};ifstream f(argv[1]);string s;float z;while(f>>s>>z){int n=0;for(char c:s)n=n*26+c-'a';q[n]=z;freq[s[0]-'a']+=exp(z);}double total=accumulate(freq,freq+26,0.);for(int c=0;c<26;c++)lp[c]=log((freq[c]+.1)/(total+2.6));ifstream in(argv[2]);in>>ct;T=stoi(argv[3]);H.resize(T);R.resize(T);for(int i=0;i<ct.size();i++)if(ct[i]>='a'&&ct[i]<='z')H[i%T][ct[i]-'a']++;enumerate(1);cout<<best<<" "<<dec(bK,bR)<<endl;for(int x:bK)cout<<x<<",";cout<<endl;for(int x:bR)cout<<x<<",";cout<<endl;cout<<"enumerated "<<countkeys<<endl;}
