#include <vector>
// Whole-cycle output-ring collision constraints pooled across independently reset paired messages.
#include <array>
#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
using namespace std;array<int,26>ctkey;vector<string>texts;int m,kind;mt19937 rng(52619601);
double score(const array<int,26>&O){int hist[30][26]={};for(auto&ct:texts)for(int i=0;i<ct.size();i++)hist[i%m][(O[ct[i]-'a']-23*(i/m)%26+26)%26]++;double total=0;for(int r=0;r<m;r++)for(int v=0;v<26;v++){int n=hist[r][v];total+=kind==2?n*(n-1)/2.:n*(n-1)*(n-2)/6.;}return total;}
int main(int argc,char**argv){ifstream f(argv[1]);string ct;while(f>>ct)texts.push_back(ct);m=atoi(argv[2]);if(m<20||m>30)return 2;kind=atoi(argv[3]);int starts=atoi(argv[4]),steps=atoi(argv[5]);array<int,26>best;double global=-1e30;for(int restart=0;restart<starts;restart++){array<int,26>O;for(int i=0;i<26;i++)O[i]=i;shuffle(O.begin(),O.end(),rng);double now=score(O),local=now;array<int,26>localkey=O;for(int it=0;it<steps;it++){int x=rng()%26,y=rng()%26;swap(O[x],O[y]);double next=score(O),temp=(kind==2?10.:18.)*(1.-it/double(steps))+.05;if(next>=now||log((rng()+1.)/4294967297.)<(next-now)/temp){now=next;if(now>local){local=now;localkey=O;}}else swap(O[x],O[y]);}O=localkey;now=local;for(int pass=0;pass<10;pass++){double gain=0;int bx=-1,by=-1;for(int x=0;x<26;x++)for(int y=x+1;y<26;y++){swap(O[x],O[y]);double next=score(O);if(next-now>gain){gain=next-now;bx=x;by=y;}swap(O[x],O[y]);}if(bx<0)break;swap(O[bx],O[by]);now+=gain;}int gauge=O[0];for(int&v:O)v=(v-gauge+26)%26;cout<<restart<<'\t'<<now<<'\t';for(int i=0;i<26;i++)cout<<(i?",":"")<<O[i];cout<<'\n'<<flush;if(now>global){global=now;best=O;}}cerr<<"completed m="<<m<<" order="<<kind<<" max="<<global<<'\n';}
