// Shared770 histogram profile under a BLIND guessed real mask. Each message resets schedule.
// Adapted progressive pipeline with supplied actual-wheel schedule file argv6. No true ring seed.
#include <cassert>
// Adapted read-only from batches/ring-profile-sol61/ring_profile.cpp; fixed progressive d_i=i; phase0/sign+1.
#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
#include <string>
#include <random>
#include <map>
#include <cmath>
using namespace std;mt19937 rng(3503852);int H[26][26]={};vector<int> steps;
vector<int> projection(const vector<int>&O){vector<int>N(26);for(int c=0;c<26;c++)for(int d=0;d<26;d++)N[(O[c]-d+26)%26]+=H[c][d];return N;}
vector<double> logs,lf; double concentration(const vector<int>&N){auto v=N;sort(v.begin(),v.end());double z=0;for(int i=0;i<26;i++)z+=v[i]*logs[i]-lf[v[i]];return z;}
int main(int argc,char**argv){ifstream schedule(argv[6]);int st;while(schedule>>st)steps.push_back(st);assert(!steps.empty());ifstream in(argv[1]);vector<string>texts;string ct;int length=0;while(in>>ct){texts.push_back(ct);length+=ct.size();}int phase=stoi(argv[2]),sign=stoi(argv[3]),nRestart=argc>4?stoi(argv[4]):3000;ifstream model(argv[5]);string letter;double val;while(model>>letter>>val)logs.push_back(val);sort(logs.begin(),logs.end());if(logs.size()!=26)return 2;lf.resize(length+1);for(int i=0;i<=length;i++)lf[i]=lgamma(i+1);for(auto&ct:texts){int shift=0;for(int i=0;i<ct.size();i++){H[ct[i]-'a'][shift]++;shift=(shift+sign*steps[(phase+i)%steps.size()]+26)%26;}}map<vector<int>,double>top;double maxsc=-1e30;for(int r=0;r<nRestart;r++){vector<int>O(26);iota(O.begin(),O.end(),0);shuffle(O.begin(),O.end(),rng);vector<int>N=projection(O);double sc=concentration(N),best=sc;vector<int>bk=O;for(int it=0;it<10000;it++){int a=rng()%26,b=rng()%26;int delta[26];for(int t=0;t<26;t++){delta[t]=H[a][(O[b]-t+26)%26]+H[b][(O[a]-t+26)%26]-H[a][(O[a]-t+26)%26]-H[b][(O[b]-t+26)%26];}vector<int>NN=N;for(int t=0;t<26;t++)NN[t]+=delta[t];double next=concentration(NN),change=next-sc;float temp=.02+2*(1.0-(it%2000)/2000.0);if(change>=0||uniform_real_distribution<float>(0,1)(rng)<exp(change/temp)){swap(O[a],O[b]);for(int t=0;t<26;t++)N[t]+=delta[t];sc+=change;}if(sc>best){best=sc;bk=O;}}int offset=bk[0];for(int&x:bk)x=(x-offset+26)%26;top[bk]=best;maxsc=max(maxsc,best);if(top.size()>100){auto worst=min_element(top.begin(),top.end(),[](auto&a,auto&b){return a.second<b.second;});top.erase(worst);}}vector<pair<double,vector<int>>>out;for(auto&[k,sc]:top)out.push_back({sc,k});sort(out.rbegin(),out.rend());for(auto&[sc,k]:out){cout<<sc<<" ";for(int c:k)cout<<c<<",";cout<<endl;}}
