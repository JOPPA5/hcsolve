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
struct Node {array<int,26> ch;float reward;Node():reward(-1e9){ch.fill(-1);}};
vector<Node> trie(1);
string ct;mt19937 rng(610332);
int ident(const string&s){int x=0;for(char c:s)x=x*26+c-'a';return x;}
void load(string dir){for(int n=3;n<=5;n++){ifstream f(dir+"/model"+to_string(n)+".tsv");string tag;float floor;f>>tag>>floor;int total=1;for(int i=0;i<n;i++)total*=26;grams[n].assign(total,floor);string s;float v;while(f>>s>>v)grams[n][ident(s)]=v;}ifstream f(dir+"/words.tsv");string w;int freq;while(f>>w>>freq){if(w.size()<2||w.size()>25)continue;int at=0;for(char c:w){int x=c-'a';if(trie[at].ch[x]<0){trie[at].ch[x]=trie.size();trie.emplace_back();}at=trie[at].ch[x];}trie[at].reward=.2*w.size()*w.size()-5+min(2.,log(1.+freq));}}
float lex(const string&s){int n=s.size();float dp[128];fill(dp,dp+n+1,-1e9);dp[0]=0;for(int i=0;i<n;i++){dp[i+1]=max(dp[i+1],dp[i]-3);int at=0;for(int j=i;j<n&&j<i+25;j++){at=trie[at].ch[s[j]-'a'];if(at<0)break;dp[j+1]=max(dp[j+1],dp[i]+trie[at].reward);if(j==n-1&&j-i>=2)dp[n]=max(dp[n],dp[i]+(j-i+1)*.75f-3);}}return dp[n];}
float score(const string&s){float sc=0;float weight[]={0,0,0,.15,.4,.8};for(int n=3;n<=5;n++){int ix=0,pow=1;for(int j=1;j<n;j++)pow*=26;for(int i=0;i<(int)s.size();i++){if(i>=n)ix-=(s[i-n]-'a')*pow;ix=ix*26+s[i]-'a';if(i>=n-1)sc+=weight[n]*grams[n][ix];}}return sc+2*lex(s);}
string dec(const vector<int>&key){string s=ct;for(char&c:s)c='a'+key[c-'a'];return s;}
int main(int argc,char**argv){load(argv[1]);ifstream in(argv[2]);in>>ct;ifstream seeds(argv[3]);string ks,mask;float best=-1e9;vector<int>bk;string bp;int r=0;while(seeds>>ks>>mask){vector<int>k(26),free;for(int i=0;i<26;i++){k[i]=ks[i]-'a';if(mask[i]=='0')free.push_back(i);}float sc=score(dec(k));for(int it=0;it<2000;it++){auto kk=k;swap(kk[free[rng()%free.size()]],kk[free[rng()%free.size()]]);float ns=score(dec(kk)),temp=.3+5*(1.-it/2000.);if(ns>sc||uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/temp)){k=kk;sc=ns;}if(sc>best){best=sc;bk=k;bp=dec(k);}}if(r%100==0)cerr<<r<<" best="<<best<<" "<<bp<<endl;r++;}cout<<best<<" lex="<<lex(bp)<<" ";for(int v:bk)cout<<char('a'+v);cout<<" "<<bp<<endl;}
