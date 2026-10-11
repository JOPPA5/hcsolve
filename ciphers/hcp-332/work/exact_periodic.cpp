#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <random>
#include <numeric>
#include <cmath>
using namespace std;
float q[26*26*26*26];
string ct; string mode;
mt19937 rng(332);
int id(string s){int r=0;for(char c:s)r=r*26+c-'a';return r;}
string dec(const vector<int>&key){string s=ct;for(int i=0;i<(int)s.size();i++){int x=s[i]-'a',k=key[i%key.size()];if(mode=="vigenere")s[i]='a'+(x-k+26)%26;else if(mode=="beaufort")s[i]='a'+(k-x+26)%26;else s[i]='a'+(x<13?13+(x+k)%13:(x-13-k+13)%13);}return s;}
float score(string s){float sum=0;for(int i=0;i+3<(int)s.size();i++)if(s[i]!='?'&&s[i+1]!='?'&&s[i+2]!='?'&&s[i+3]!='?')sum+=q[((s[i]-'a')*26+s[i+1]-'a')*26*26+(s[i+2]-'a')*26+s[i+3]-'a'];return sum;}
int main(int argc,char**argv){ifstream f(string(argv[1])+"/quadgrams.tsv");string x;float v;fill(begin(q),end(q),-4.0);while(f>>x>>v)q[id(x)]=v;ifstream c(argc>2?argv[2]:(string(argv[1])+"/cipher.txt"));c>>ct;
mode=argv[3];int alphabet=mode=="porta"?13:26; for(int w=1;w<=4;w++){float best=-1e9;vector<int>bk;string bt;long total=1;for(int i=0;i<w;i++)total*=alphabet;for(long ix=0;ix<total;ix++){long t=ix;vector<int>k(w);for(int i=0;i<w;i++){k[i]=t%alphabet;t/=alphabet;}string pt=dec(k);float sc=score(pt);if(sc>best){best=sc;bk=k;bt=pt;}}cout<<w<<" "<<total<<" "<<best<<" ";for(int i:bk)cout<<i<<",";cout<<" "<<bt<<endl;}}
