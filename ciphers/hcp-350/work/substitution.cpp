#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <random>
#include <numeric>
#include <cmath>
using namespace std;
float q[26*26*26*26]; string ct; mt19937 rng(374);
int id(string s){int r=0;for(char c:s)r=r*26+c-'a';return r;}
string dec(const vector<int>&k){string s=ct;for(char& c:s)c='a'+k[c-'a'];return s;}
float score(string s){float z=0;for(int i=0;i+3<s.size();i++)z+=q[((s[i]-'a')*26+s[i+1]-'a')*26*26+(s[i+2]-'a')*26+s[i+3]-'a'];return z;}
int main(int argc,char**argv){fill(begin(q),end(q),-4);ifstream f(string(argv[1])+"/quadgrams.tsv");string x;float v;while(f>>x>>v)q[id(x)]=v;ifstream c(string(argv[1])+"/cipher.txt");c>>ct;if(argc>2)reverse(ct.begin(),ct.end());float best=-1e9;
for(int r=0;r<100;r++){vector<int>k(26);iota(k.begin(),k.end(),0);shuffle(k.begin(),k.end(),rng);float sc=score(dec(k));for(int it=0;it<50000;it++){auto kk=k;swap(kk[rng()%26],kk[rng()%26]);float ns=score(dec(kk));float temp=0.3+5.0*(1-(it%5000)/5000.0);if(ns>sc||uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/temp)){k=kk;sc=ns;}if(sc>best){best=sc;cout<<best<<" ";for(int a:k)cout<<char('a'+a);cout<<" "<<dec(k)<<endl;}}}}
