#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <vector>
using namespace std;
vector<float> grams[6]; vector<int> cipher;
float score(const vector<int>& k){
 float out=0; float wt[]={0,0,0,.2,.5,.8};
 for(int n=3;n<=5;n++) for(int i=0;i+n<=cipher.size();i++){
  int ix=0; for(int j=0;j<n;j++)ix=ix*26+k[cipher[i+j]];
  out+=wt[n]*grams[n][ix];
 } return out;
}
int main(int argc,char**argv){
 if(argc!=6)return 2;
 for(int n=3;n<=5;n++){
  ifstream f(string(argv[1])+"/model"+to_string(n)+".tsv");string s;float v;f>>s>>v;
  int size=1;for(int j=0;j<n;j++)size*=26;grams[n].assign(size,v);
  while(f>>s>>v){int ix=0;for(char c:s)ix=ix*26+c-'a';grams[n][ix]=v;}
 }
 ifstream f(argv[2]);string s;f>>s;for(char c:s)cipher.push_back(c-'a');
 mt19937 rng(stoul(argv[5])); int restarts=stoi(argv[3]),steps=stoi(argv[4]);
 float best=-1e30; vector<int>bk;
 for(int r=0;r<restarts;r++){
  vector<int>k(26);iota(k.begin(),k.end(),0);shuffle(k.begin(),k.end(),rng); swap(k[0],k[find(k.begin(),k.end(),10)-k.begin()]); swap(k[5],k[find(k.begin(),k.end(),4)-k.begin()]); swap(k[20],k[find(k.begin(),k.end(),3)-k.begin()]); swap(k[19],k[find(k.begin(),k.end(),21)-k.begin()]); swap(k[3],k[find(k.begin(),k.end(),18)-k.begin()]); float sc=score(k);
  for(int it=0;it<steps;it++){
   auto kk=k; int a=rng()%26,b=rng()%26; vector<int> fixed={0,5,20,19,3}; if(find(fixed.begin(),fixed.end(),a)!=fixed.end()||find(fixed.begin(),fixed.end(),b)!=fixed.end())continue; swap(kk[a],kk[b]);float ns=score(kk);
   float temp=.15+10*(1.-(it%5000)/5000.);
   if(ns>=sc||log((rng()+1.)/4294967297.)<(ns-sc)/temp){k=kk;sc=ns;}
   if(sc>best){best=sc;bk=k;}
  }
 }
 cout<<"score "<<best<<"\nkey ";for(int x:bk)cout<<char('a'+x);
 cout<<"\nplaintext ";for(int x:cipher)cout<<char('a'+bk[x]);
 cout<<"\nproposals "<<restarts*steps<<"\n";
}
