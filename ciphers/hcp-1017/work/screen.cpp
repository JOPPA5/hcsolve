#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>
using namespace std;
int main(int argc,char**argv){ifstream f(argv[1]);string tag,s;float floor,v;f>>tag>>floor;vector<float>g(26*26*26*26,floor);while(f>>s>>v){int i=0;for(char c:s)i=26*i+c-'a';g[i]=v;}ifstream in(argv[2]);string ct;in>>ct;vector<int>a;for(char c:ct)a.push_back(c-'a');auto score=[&](vector<int>&k){float z=0;for(int i=0;i+3<a.size();i++)z+=g[((k[a[i]]*26+k[a[i+1]])*26+k[a[i+2]])*26+k[a[i+3]]];return z;};mt19937 r(1017);float best=-1e9;vector<int>bk;for(int n=0;n<200;n++){vector<int>k(26);iota(k.begin(),k.end(),0);shuffle(k.begin(),k.end(),r);float sc=score(k);for(int i=0;i<20000;i++){int x=r()%26,y=r()%26;swap(k[x],k[y]);float ss=score(k),t=.2+3*(1.-(i%5000)/5000.);if(ss>sc||uniform_real_distribution<float>(0,1)(r)<exp((ss-sc)/t))sc=ss;else swap(k[x],k[y]);if(sc>best){best=sc;bk=k;}}if(n%20==0){cerr<<n<<" "<<best<<" ";for(int x:a)cerr<<char('a'+bk[x]);cerr<<endl;}}cout<<best<<"\n";for(int x:bk)cout<<char('a'+x);cout<<"\n";for(int x:a)cout<<char('a'+bk[x]);cout<<endl;}
