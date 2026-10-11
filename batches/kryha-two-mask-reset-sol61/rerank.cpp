#include <fstream>
#include <iostream>
#include <vector>
#include <array>
#include <unordered_map>
#include <algorithm>
#include <cstdint>
using namespace std;unordered_map<uint64_t,double>M[8];
double score(const array<int,26>&p,const vector<string>&v,int n){double s=0;for(auto&t:v)for(int i=0;i+n<=t.size();i++){uint64_t z=0;for(int j=0;j<n;j++)z=z*26+p[t[i+j]-'a'];auto x=M[n].find(z);s+=x==M[n].end()?-n:x->second;}return s;}
struct C{double s;int id,a,b;array<int,26>p;bool operator<(const C&o)const{return s>o.s;}};
int main(int argc,char**argv){for(int n:{6,7}){ifstream f(string(argv[1])+"/model"+to_string(n)+".tsv");if(!f){cerr<<"Missing model\n";return 2;}string g;double v;while(f>>g>>v){uint64_t z=0;for(char c:g)z=z*26+c-'a';M[n][z]=v;}}ifstream pro(argv[2]);string a,b;vector<vector<string>>v;while(pro>>a>>b)v.push_back({a,b});ifstream f(argv[3]);int id;double old;vector<C>win[8];while(f>>id>>old){array<int,26>p;for(int&x:p)f>>x;f>>a>>b;for(int i=-1;i<26;i++)for(int j=(i==-1?-1:i+1);j<(i==-1?0:26);j++){auto q=p;if(i>=0)swap(q[i],q[j]);for(int n:{6,7})win[n].push_back({score(q,v[id],n),id,i,j,q});}}cout.precision(15);for(int n:{6,7}){sort(win[n].begin(),win[n].end());cout<<"N "<<n<<" COUNT "<<win[n].size()<<'\n';for(int k=0;k<min(100,(int)win[n].size());k++){auto&w=win[n][k];cout<<w.s<<' '<<w.id<<' '<<w.a<<' '<<w.b<<'\n';for(int x:w.p)cout<<x<<' ';cout<<'\n';for(auto&t:v[w.id]){for(char c:t)cout<<char('a'+w.p[c-'a']);cout<<'\n';}}}}
