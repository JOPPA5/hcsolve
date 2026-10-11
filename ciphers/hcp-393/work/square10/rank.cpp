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
#include "frozen-lex.hpp"
struct Candidate {float score;array<int,10> cols,rows;string plain;bool operator<(const Candidate&o)const{return score>o.score;}};
int main(int argc,char**argv){load(argv[1],argv[2]);ifstream f(argv[3]);string p;f>>p;vector<string>r;for(int i=0;i<10;i++)r.push_back(p.substr(i*10,10));float edge[10][10];for(int a=0;a<10;a++)for(int b=0;b<10;b++)edge[a][b]=language(r[a].substr(6)+r[b].substr(0,4))-language(r[a].substr(6))-language(r[b].substr(0,4));float truth=0;for(int i=0;i<9;i++)truth+=edge[i][i+1];array<int,10>order;iota(order.begin(),order.end(),0);long greater=0,equal=0;do{float sc=0;for(int i=0;i<9;i++)sc+=edge[order[i]][order[i+1]];if(sc>truth+0.001)greater++;else if(abs(sc-truth)<=0.001)equal++;}while(next_permutation(order.begin(),order.end()));cout<<"rows above truth="<<greater<<" ties="<<equal<<" among=3628800\n";}