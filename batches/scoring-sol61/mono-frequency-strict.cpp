#include <algorithm>
#include <array>
#include <cmath>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <vector>
using namespace std;
vector<float> grams[6];
struct Node {array<int,26> ch;float reward;int mask;Node():reward(-1e9),mask(0){ch.fill(-1);}};
vector<Node> trie(1);
float tr[10][10];string ct;mt19937 rng(610332);
int ident(const string&s){int x=0;for(char c:s)x=x*26+c-'a';return x;}
void load(string dir){for(int n=3;n<=5;n++){ifstream f(dir+"/model"+to_string(n)+".tsv");string tag;float floor;f>>tag>>floor;int total=1;for(int i=0;i<n;i++)total*=26;grams[n].assign(total,floor);string s;float v;while(f>>s>>v)grams[n][ident(s)]=v;}ifstream tf(dir+"/pos-transitions.tsv");int aa,bb;float vv;while(tf>>aa>>bb>>vv)tr[aa][bb]=vv;ifstream f(dir+"/words-pos.tsv");string w;int freq,mask;while(f>>w>>freq>>mask){if(w.size()<2||w.size()>25)continue;int at=0;for(char c:w){int x=c-'a';if(trie[at].ch[x]<0){trie[at].ch[x]=trie.size();trie.emplace_back();}at=trie[at].ch[x];}trie[at].reward=1.2*w.size()-5+min(4.,log(1.+freq));trie[at].mask=mask;}}
float lex(const string&s){int n=s.size();float dp[128][9];for(int i=0;i<=n;i++)fill(dp[i],dp[i]+9,-1e9);dp[0][8]=0;float partial=-1e9;for(int i=0;i<n;i++){for(int t=0;t<9;t++)dp[i+1][t]=max(dp[i+1][t],dp[i][t]-10);int at=0;for(int j=i;j<n&&j<i+25;j++){at=trie[at].ch[s[j]-'a'];if(at<0)break;if(trie[at].mask){for(int nt=0;nt<8;nt++)if(trie[at].mask&(1<<nt)){float v=-1e9;for(int t=0;t<9;t++)v=max(v,dp[i][t]+tr[t][nt]);dp[j+1][nt]=max(dp[j+1][nt],v+trie[at].reward);}}if(j==n-1&&j-i>=2){for(int t=0;t<9;t++)partial=max(partial,dp[i][t]+(j-i+1)*.75f-3);}}}float best=partial;for(int t=0;t<9;t++)best=max(best,dp[n][t]+tr[t][9]);return best;}
float score(const string&s){float sc=0;float weight[]={0,0,0,.15,.4,.8};for(int n=3;n<=5;n++){int ix=0,pow=1;for(int j=1;j<n;j++)pow*=26;for(int i=0;i<(int)s.size();i++){if(i>=n)ix-=(s[i-n]-'a')*pow;ix=ix*26+s[i]-'a';if(i>=n-1)sc+=weight[n]*grams[n][ix];}}return sc+2*lex(s);}
string dec(const vector<int>&key){string s=ct;for(char&c:s)c='a'+key[c-'a'];return s;}
int main(int argc,char**argv){load(argv[1]);ifstream in(argv[2]);in>>ct;if(argc>3&&string(argv[3])=="score"){cout<<score(ct)<<" lex="<<lex(ct)<<" "<<ct<<endl;return 0;}int restarts=argc>3?stoi(argv[3]):100;float best=-1e9;vector<int>bk;string bp;for(int r=0;r<restarts;r++){vector<int>k(26);iota(k.begin(),k.end(),0);shuffle(k.begin(),k.end(),rng);string pt=dec(k);float sc=score(pt);for(int it=0;it<50000;it++){vector<int>kk=k;swap(kk[rng()%26],kk[rng()%26]);string pp=dec(kk);float ns=score(pp),temp=.3+4.5*(1.-(it%10000)/10000.);if(ns>sc||uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/temp)){k=kk;sc=ns;}if(sc>best){best=sc;bk=k;bp=dec(k);}}if(r%10==0)cerr<<r<<" best="<<best<<" "<<bp<<endl;}cout<<best<<" lex="<<lex(bp)<<" ";for(int v:bk)cout<<char('a'+v);cout<<" "<<bp<<endl;}
