#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <vector>
using namespace std;float q[456976];int coord[52];string ct;mt19937 rng(5217903);
struct Key{vector<int>P,O,H;int phase;};
int idx(string s){int x=0;for(char c:s)x=x*26+c-'a';return x;}
string dec(const Key&k){string out;int m=k.H.size(),origin=coord[k.H[k.phase]];for(int i=0;i<ct.size();i++){int D=coord[k.H[(k.phase+i)%m]]+179*((k.phase+i)/m)-origin;out+=char('a'+k.P[(k.O[ct[i]-'a']-D%26+26)%26]);}return out;}
float score(string s){float z=0;for(int i=0;i+3<s.size();i++)z+=q[((s[i]-'a')*26+s[i+1]-'a')*676+(s[i+2]-'a')*26+s[i+3]-'a'];return z;}
int main(int argc,char**argv){fill(begin(q),end(q),-4);ifstream f(string(argv[1])+"/ring-4grams.tsv");string s;float x;while(f>>s>>x)q[idx(s)]=x;ifstream cipher(argv[2]);cipher>>ct;ifstream geometry(argv[3]);int d,i=0,total=0;while(geometry>>d){coord[i++]=total;total+=d;}if(i!=52||total!=179)return 2;int m=stoi(argv[5]);Key seed;seed.P.resize(26);seed.O.resize(26);seed.H.resize(m);ifstream input(argv[4]);for(int&x:seed.P)input>>x;for(int&x:seed.O)input>>x;for(int&x:seed.H)input>>x;input>>seed.phase;float best=-1e9;Key bk;
for(int r=0;r<8;r++){Key k=seed;for(int i=0;i<r%4;i++){swap(k.P[rng()%26],k.P[rng()%26]);swap(k.O[rng()%26],k.O[rng()%26]);}float sc=score(dec(k));for(int it=0;it<100000;it++){Key t=k;int type=rng()%100;if(type<40)swap(t.P[rng()%26],t.P[rng()%26]);else if(type<80)swap(t.O[rng()%26],t.O[rng()%26]);else if(type<98){int j=rng()%m,prev=k.H[(j+m-1)%m],next=k.H[(j+1)%m];vector<int>options;for(int h=0;h<52;h++)if(!binary_search(k.H.begin(),k.H.end(),h)){bool between=prev<next?(h>prev&&h<next):(h>prev||h<next);if(it%2==0||between)options.push_back(h);}if(!options.empty()){t.H[j]=options[rng()%options.size()];sort(t.H.begin(),t.H.end());}}else t.phase=rng()%m;float ns=score(dec(t)),temp=.2+9*(1.0-(it%10000)/10000.0);if(ns>sc||uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/temp)){k=t;sc=ns;}if(sc>best){best=sc;bk=k;}}}
cout<<best<<" "<<dec(bk)<<endl;for(int x:bk.P)cout<<x<<",";cout<<endl;for(int x:bk.O)cout<<x<<",";cout<<endl;for(int x:bk.H)cout<<x+1<<",";cout<<" "<<bk.phase<<endl;}
