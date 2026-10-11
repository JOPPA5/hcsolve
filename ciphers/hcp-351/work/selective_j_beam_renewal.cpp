#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;
int steps[]={7,6,7,5,6,7,6,8,6,10,5,6,5,7,6,5,9};
struct State{array<int8_t,26>O;array<int16_t,26>N{};uint32_t used=0;int d=0,k=0;double score=0,boundary=0;int run=0;};
vector<double>weights;array<double,101>logJ,logLetter;
double score(State&s){array<int,25>counts;for(int i=1;i<26;i++)counts[i-1]=s.N[i];sort(counts.rbegin(),counts.rend());double z=s.boundary;for(int i=0;i<25;i++)z+=counts[i]*weights[i];return z;}
State advance(State s,int c,int pos){if(s.O[c]<0){s.O[c]=pos;s.used|=1u<<pos;}int slot=(s.O[c]-s.d+26)%26;s.N[slot]++;s.boundary+=(slot==0?logJ[min(s.run,100)]:logLetter[min(s.run,100)]);s.run=slot==0?0:s.run+1;for(int i=0;i<(slot==0?2:1);i++){s.d=(s.d+steps[s.k%17])%26;s.k++;}s.score=score(s);return s;}
int main(int argc,char**argv){ifstream input(argv[1]);string ct;input>>ct;ifstream freq(argv[2]);double x;for(int i=0;i<25;i++){freq>>x;weights.push_back(x);}for(int i=0;i<101;i++)freq>>logJ[i]>>logLetter[i];int width=stoi(argv[3]),phase=stoi(argv[4]);State start;start.O.fill(-1);start.k=phase;vector<State>beam{start};for(char ch:ct){int c=ch-'a';vector<State>next;for(auto&s:beam){if(s.O[c]>=0)next.push_back(advance(s,c,s.O[c]));else for(int p=0;p<26;p++)if(!(s.used&(1u<<p)))next.push_back(advance(s,c,p));}if(next.size()>width){nth_element(next.begin(),next.begin()+width,next.end(),[](auto&a,auto&b){return a.score>b.score;});next.resize(width);}beam=move(next);}sort(beam.begin(),beam.end(),[](auto&a,auto&b){return a.score>b.score;});for(int i=0;i<min(300,(int)beam.size());i++){cout<<int(beam[i].score*1000)<<" ";for(int pos:beam[i].O)cout<<pos<<",";cout<<"\n";}}
