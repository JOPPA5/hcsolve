#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <vector>
using namespace std;
float q[26*26*26*26*26]; mt19937 rng;
vector<int> decrypt(const vector<int>&ct,const vector<int>&A,const vector<int>&R){vector<int>inv(26),p;for(int i=0;i<26;i++)inv[A[i]]=i;for(int i=0;i<ct.size();i++)p.push_back(ct[i]<0?-1:inv[(A[ct[i]]-R[i%R.size()]+26)%26]);return p;}
float score(const vector<int>&p){float s=0;for(int i=0;i+4<p.size();i++){if(p[i]<0||p[i+1]<0||p[i+2]<0||p[i+3]<0||p[i+4]<0)continue;int z=((p[i]*26+p[i+1])*26+p[i+2])*26+p[i+3];z=z*26+p[i+4];s+=q[z];}return s;}
int main(int argc,char**argv){fill(begin(q),end(q),-5);ifstream model(argv[1]);string g;float value;while(model>>g>>value){int id=0;for(char c:g)id=id*26+c-'a';q[id]=value;}ifstream file(argv[2]);string text;file>>text;vector<int>ct;for(char c:text)ct.push_back(c=='?'?-1:c-'a');int T=stoi(argv[3]),restarts=stoi(argv[4]),moves=stoi(argv[5]);rng.seed(stoul(argv[6]));ifstream seedfile(argv[7]);vector<int>seedA(26),seedR(T);for(int&v:seedA)seedfile>>v;for(int&v:seedR)seedfile>>v;float best=-1e30;vector<int>bestA,bestR;long long proposals=0;
for(int restart=0;restart<restarts;restart++){vector<int>A(26),R(T);A=seedA;R=seedR;if(restart){for(int z=0;z<5;z++)swap(A[rng()%26],A[rng()%26]);R[rng()%T]=rng()%26;}float sc=score(decrypt(ct,A,R));for(int it=0;it<moves;it++){auto a=A,r=R;if(rng()%4==0){int col=rng()%T;r[col]=rng()%26;}else{int x=rng()%26,y=rng()%26;swap(a[x],a[y]);}float next=score(decrypt(ct,a,r));float temp=.2+9*(1-(it%10000)/10000.0);if(next>=sc||uniform_real_distribution<float>(0,1)(rng)<exp((next-sc)/temp)){A=a;R=r;sc=next;}if(it%1000==0){int col=rng()%T;float high=sc;auto rr=R;for(int shift=0;shift<26;shift++){auto test=R;test[col]=shift;float ns=score(decrypt(ct,A,test));if(ns>high){high=ns;rr=test;}}R=rr;sc=high;}proposals++;if(sc>best){best=sc;bestA=A;bestR=R;}}if(restart%32==0)cerr<<restart<<" "<<best<<"\n";}
int rotation=bestA[0];for(int&v:bestA)v=(v-rotation+26)%26;cout<<best<<" "<<proposals<<"\n";for(int x:bestA)cout<<x<<",";cout<<"\n";for(int x:bestR)cout<<x<<",";cout<<"\n";for(int x:decrypt(ct,bestA,bestR))cout<<(x<0?'?':char('a'+x));cout<<"\n";return 0;}
