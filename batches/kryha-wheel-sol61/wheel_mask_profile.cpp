#include <algorithm>
#include <array>
#include <cmath>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <random>
#include <string>
#include <vector>
using namespace std;mt19937 rng(5217901);int coord[52]={};string ct;double weights[26],lf[10000];
struct Key{vector<int>O,stops;int phase;};
vector<int>project(const Key&k){vector<int>N(26);int m=k.stops.size(),d=0,j=k.phase;int origin=coord[k.stops[j]];for(int i=0;i<ct.size();i++){int at=k.stops[(k.phase+i)%m];int cycle=(k.phase+i)/m;int D=coord[at]+179*cycle-origin;N[(k.O[ct[i]-'a']-D%26+26)%26]++;}return N;}
double score(const Key&k){auto N=project(k);sort(N.rbegin(),N.rend());double z=lf[ct.size()];for(int j=0;j<26;j++)z+=N[j]*weights[j]-lf[N[j]];return z;}
string keystr(const Key&k){string s;for(int x:k.O)s+=to_string(x)+",";s+=' ';for(int x:k.stops)s+=to_string(x+1)+",";s+=' '+to_string(k.phase);return s;}
int main(int argc,char**argv){ifstream in(argv[1]);in>>ct;ifstream table(argv[2]);int d,sum=0,i=0;while(table>>d){coord[i++]=sum;sum+=d;}if(i!=52||sum!=179)return 2;int m=stoi(argv[3]),restarts=stoi(argv[4]);ifstream w(argv[5]);for(double &v:weights)w>>v;for(int j=0;j<10000;j++)lf[j]=lgamma(j+1);map<string,double>top;for(int r=0;r<restarts;r++){Key k;vector<int>all(52);iota(all.begin(),all.end(),0);shuffle(all.begin(),all.end(),rng);k.stops=vector<int>(all.begin(),all.begin()+m);sort(k.stops.begin(),k.stops.end());k.O.resize(26);iota(k.O.begin(),k.O.end(),0);shuffle(k.O.begin(),k.O.end(),rng);k.phase=rng()%m;double sc=score(k),best=sc;Key bk=k;for(int it=0;it<10000;it++){Key trial=k;int type=rng()%100;if(type<65){swap(trial.O[rng()%26],trial.O[rng()%26]);}else if(type<95){int j=rng()%m;vector<int>options;for(int h=0;h<52;h++)if(!binary_search(k.stops.begin(),k.stops.end(),h)){
// Half of hole relocations preserve cyclic ordinal between neighboring activeholes.
int prev=k.stops[(j+m-1)%m],next=k.stops[(j+1)%m];bool between=prev<next?(h>prev&&h<next):(h>prev||h<next);if(it%2==0||between)options.push_back(h);}
if(!options.empty()){trial.stops[j]=options[rng()%options.size()];sort(trial.stops.begin(),trial.stops.end());}}else{trial.phase=rng()%m;}double ns=score(trial),change=ns-sc;float temp=.02+3*(1.0-(it%2000)/2000.0);if(change>=0||uniform_real_distribution<float>(0,1)(rng)<exp(change/temp)){k=trial;sc=ns;}if(sc>best){best=sc;bk=k;}}
int offset=bk.O[0];for(int&x:bk.O)x=(x-offset+26)%26;top[keystr(bk)]=best;}
vector<pair<double,string>>rows;for(auto&[k,s]:top)rows.push_back({s,k});sort(rows.rbegin(),rows.rend());for(auto&[s,k]:rows)cout<<int(round(s*1000))<<" "<<k<<"\n";}
