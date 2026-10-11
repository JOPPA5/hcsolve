#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;int steps[]={7,6,7,5,6,7,6,8,6,10,5,6,5,7,6,5,9};array<double,101>logJ,logL;
struct State{array<uint32_t,26>domains;int d=0,k=0,run=0,jcount=0;double score=0;};
bool propagate(State&s){bool changed=true;while(changed){changed=false;uint32_t fixed=0;for(auto x:s.domains){if(!x)return false;if((x&(x-1))==0){if(fixed&x)return false;fixed|=x;}}for(auto&x:s.domains)if(x&(x-1)){auto y=x&~fixed;if(!y)return false;if(y!=x){changed=true;x=y;}}}return true;}
bool augment(int c,const State&s,array<int,26>&owner,uint32_t&visited){for(int p=0;p<26;p++)if((s.domains[c]&(1u<<p))&&!(visited&(1u<<p))){visited|=1u<<p;if(owner[p]<0||augment(owner[p],s,owner,visited)){owner[p]=c;return true;}}return false;}
bool complete(const State&s,array<int,26>&O){array<int,26>owner;owner.fill(-1);for(int c=0;c<26;c++){uint32_t visited=0;if(!augment(c,s,owner,visited))return false;}for(int p=0;p<26;p++)O[owner[p]]=p;return true;}
int main(int argc,char**argv){ifstream in(argv[1]);string ct;in>>ct;ifstream f(argv[2]);double unused;for(int i=0;i<25;i++)f>>unused;for(int i=0;i<101;i++)f>>logJ[i]>>logL[i];int width=stoi(argv[3]),phase=stoi(argv[4]);State initial;initial.domains.fill((1u<<26)-1);initial.k=phase;vector<State>beam{initial};int at=0;for(char ch:ct){vector<State>next;int c=ch-'a';for(auto state:beam)for(int isJ=0;isJ<2;isJ++){State s=state;uint32_t mask=1u<<s.d;if(isJ)s.domains[c]&=mask;else s.domains[c]&=~mask;if(!propagate(s))continue;s.score+=isJ?logJ[min(s.run,100)]:logL[min(s.run,100)];s.run=isJ?0:s.run+1;s.jcount+=isJ;for(int z=0;z<(isJ?2:1);z++){s.d=(s.d+steps[s.k%17])%26;s.k++;}next.push_back(s);}sort(next.begin(),next.end(),[](auto&a,auto&b){return a.score>b.score;});vector<State>keep;for(auto&s:next){array<int,26>O;if(complete(s,O))keep.push_back(s);if(keep.size()>=width)break;}beam=move(keep);if(beam.empty()){cerr<<"empty at "<<at<<endl;return 2;}at++;}int n=0;for(auto&s:beam){array<int,26>O;if(complete(s,O)){cout<<int(s.score*1000)<<" ";for(int x:O)cout<<x<<",";cout<<"\n";if(++n==300)break;}}}
