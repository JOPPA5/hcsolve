#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>
using namespace std;
float q[456976];string ct;int T,family;mt19937 rng(3342844);
int ix(string s){int n=0;for(char c:s)n=n*26+c-'a';return n;}
string dec(vector<int>&K,vector<int>&R){string s=ct;for(int i=0;i<s.size();i++){int c=ct[i]-'a';s[i]=c<0||c>=26?'?':char('a'+(family==1?K[(c-R[i%T]+26)%26]:(K[c]-R[i%T]+26)%26));}return s;}
float score(string s){float z=0;for(int i=0;i+3<s.size();i++){if(s[i]=='?'||s[i+1]=='?'||s[i+2]=='?'||s[i+3]=='?')continue;z+=q[((s[i]-'a')*26+s[i+1]-'a')*676+(s[i+2]-'a')*26+s[i+3]-'a'];}return z;}
int main(int argc,char**argv){fill(begin(q),end(q),-4);ifstream f(argv[1]);string s;float v;while(f>>s>>v)q[ix(s)]=v;ifstream in(argv[2]);in>>ct;family=stoi(argv[3]);T=stoi(argv[4]);int restarts=stoi(argv[5]);float best=-1e9;string bp;vector<int>bk,br;for(int r=0;r<restarts;r++){vector<int>K(26),R(T);iota(K.begin(),K.end(),0);shuffle(K.begin(),K.end(),rng);for(int&x:R)x=rng()%26;float sc=score(dec(K,R));for(int it=0;it<50000;it++){auto k=K,rr=R;if((it/2500)%2==0)swap(k[rng()%26],k[rng()%26]);else rr[rng()%T]=rng()%26;float ns=score(dec(k,rr)),temp=.2+9*(1.-(it%10000)/10000.);if(ns>sc||uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/temp)){K=k;R=rr;sc=ns;}if(sc>best){best=sc;bp=dec(K,R);bk=K;br=R;}}}cout<<best<<" "<<bp<<endl;for(int x:bk)cout<<x<<",";cout<<endl;for(int x:br)cout<<x<<",";cout<<endl;}
