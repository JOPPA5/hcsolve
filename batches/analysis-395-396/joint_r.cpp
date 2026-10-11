// Conditional R/XQ model: common daily rank permutations; each is rotated to n.
// Columnar ranks are 1-based; plaintext is row-written and columns read by rank.
#include <algorithm>
#include <cassert>
#include <cmath>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
using Key=vector<int>; using Keys=vector<Key>;
float quad[26*26*26*26]; mt19937 rng(395396);
vector<int> widths(string s){replace(s.begin(),s.end(),',',' ');istringstream f(s);vector<int> w;int v;while(f>>v)w.push_back(v);return w;}
Key aligned(const Key&k,int n){Key out(k.size());auto at=find(k.begin(),k.end(),n);assert(at!=k.end());int i=at-k.begin();for(int j=0;j<(int)k.size();j++)out[j]=k[(i+j)%k.size()];return out;}
string stage(const string&text,const Key&k,int n,bool encrypt){Key a=aligned(k,n);int w=k.size(),N=text.size(),pos=0;string out(N,' ');for(int rank=1;rank<=w;rank++){int col=find(a.begin(),a.end(),rank)-a.begin();for(int i=col;i<N;i+=w){if(encrypt)out[pos++]=text[i];else out[i]=text[pos++];}}return out;}
string cascade(string text,const Keys&keys,int n,bool encrypt){if(encrypt)for(auto&k:keys)text=stage(text,k,n,true);else for(auto it=keys.rbegin();it!=keys.rend();it++)text=stage(text,*it,n,false);return text;}
float score(const string&s){float z=0;for(int i=0;i+3<(int)s.size();i++)z+=quad[((s[i]-'a')*26+s[i+1]-'a')*676+(s[i+2]-'a')*26+s[i+3]-'a'];return z;}
Keys randomkeys(const vector<int>&ws){Keys all;for(int w:ws){Key k(w);iota(k.begin(),k.end(),1);shuffle(k.begin()+1,k.end(),rng);all.push_back(k);}return all;}
string read(string path){ifstream f(path);string s;f>>s;return s;}
void printkeys(const Keys&ks){for(auto&k:ks){cout<<'[';for(auto v:k)cout<<v<<',';cout<<']';}cout<<'\n';}
int main(int argc,char**argv){if(argc<6){cerr<<"joint_r quadgrams widths mode text395 text396 [restarts=20] [steps=30000]\n";return 2;}fill(begin(quad),end(quad),-4);ifstream f(argv[1]);string gram;float value;while(f>>gram>>value){int j=0;for(char c:gram)j=j*26+c-'a';quad[j]=value;}auto ws=widths(argv[2]);string mode=argv[3],x=read(argv[4]),y=read(argv[5]);int rest=argc>6?stoi(argv[6]):20,steps=argc>7?stoi(argv[7]):30000;
if(mode=="generate"){
rng.seed(981234); // Independent planted-key seed; must differ from attack restarts.
auto k=randomkeys(ws);string cx=cascade(x,k,9,true),cy=cascade(y,k,7,true);assert(cascade(cx,k,9,false)==x);assert(cascade(cy,k,7,false)==y);cout<<"cipher395 "<<cx<<"\ncipher396 "<<cy<<"\ntrue_score "<<score(x)+score(y)<<"\nkeys ";printkeys(k);return 0;}
// Roundtrip property for unequal widths and irregular row lengths.
for(int i=0;i<100;i++){auto k=randomkeys(ws);assert(cascade(cascade(x,k,9,true),k,9,false)==x);assert(cascade(cascade(y,k,7,true),k,7,false)==y);}rng.seed(395396);
float best=-1e9;Keys bestk;string bx,by;
for(int rep=0;rep<rest;rep++){
auto keys=randomkeys(ws);string tx=cascade(x,keys,9,false),ty=cascade(y,keys,7,false);float sc=score(tx)+score(ty);
for(int it=0;it<steps;it++){
auto kk=keys;int which=rng()%ws.size(),w=ws[which];int a=1+rng()%(w-1),b=1+rng()%(w-1);swap(kk[which][a],kk[which][b]);if(it%5==0){if(a>b)swap(a,b);reverse(kk[which].begin()+a,kk[which].begin()+b+1);}tx=cascade(x,kk,9,false);ty=cascade(y,kk,7,false);float ns=score(tx)+score(ty),temperature=0.5+9.*(1.-(it%10000)/10000.);if(ns>sc||uniform_real_distribution<double>(0,1)(rng)<exp((ns-sc)/temperature)){keys=kk;sc=ns;}if(ns>best){best=ns;bestk=kk;bx=tx;by=ty;}
}}
cout<<"best_score "<<best<<"\nplaintext395 "<<bx<<"\nplaintext396 "<<by<<"\nkeys ";printkeys(bestk);cout<<"evaluations "<<rest*steps<<"\n";
}
