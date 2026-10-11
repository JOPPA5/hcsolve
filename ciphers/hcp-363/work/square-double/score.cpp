#include <algorithm>
#include <array>
#include <cmath>
#include <cassert>
#include <fstream>
#include <iostream>
#include <numeric>
#include <queue>
#include <random>
#include <string>
#include <vector>
using namespace std;
mt19937 rng(610363);
float bi[26][26];vector<float> gram[6];
void load(string dir,string big){ifstream f(big);string s;float v;while(f>>s>>v)bi[s[0]-'a'][s[1]-'a']=v;for(int n=3;n<=5;n++){ifstream g(dir+"/model"+to_string(n)+".tsv");string tag;float floor;g>>tag>>floor;int total=1;for(int i=0;i<n;i++)total*=26;gram[n].assign(total,floor);while(g>>s>>v){int ix=0;for(char c:s)ix=ix*26+c-'a';gram[n][ix]=v;}}}
float language(const string&s){float sc=0,wt[]={0,0,0,.15,.4,.8};for(int n=3;n<=5;n++){int ix=0,pow=1;for(int j=1;j<n;j++)pow*=26;for(int i=0;i<(int)s.size();i++){if(i>=n)ix-=(s[i-n]-'a')*pow;ix=ix*26+s[i]-'a';if(i>=n-1)sc+=wt[n]*gram[n][ix];}}return sc;}

#include "frozen-lex-long.hpp"
int main(int argc,char**argv){load(argv[1],argv[2]);loadLex(argv[1]);for(int i=3;i<argc;i++){ifstream f(argv[i]);string s;f>>s;cout<<argv[i]<<" gram="<<language(s)<<" lex="<<lex(s)<<" combined="<<language(s)+2*lex(s)<<"\n";}}
