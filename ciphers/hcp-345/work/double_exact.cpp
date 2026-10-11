#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;
float q[456976];
string dec(const string&s,const vector<int>&k){int n=s.size(),w=k.size(),at=0;string o(n,' ');for(int c:k)for(int pos=c;pos<n;pos+=w)o[pos]=s[at++];return o;}
float score(const string&s){float z=0;for(int i=0;i+3<(int)s.size();i++)z+=q[((s[i]-'a')*26+s[i+1]-'a')*676+(s[i+2]-'a')*26+s[i+3]-'a'];return z;}
int main(int argc,char**argv){if(argc!=3&&argc!=4)return 2;int maxw=argc==4?stoi(argv[3]):6;fill(begin(q),end(q),-4);ifstream f(argv[1]);string g;float v;while(f>>g>>v){int id=0;for(char c:g)id=26*id+c-'a';q[id]=v;}ifstream c(argv[2]);string ct;c>>ct;vector<vector<int>>ks;for(int w=2;w<=maxw;w++){vector<int>k(w);iota(k.begin(),k.end(),0);do{ks.push_back(k);}while(next_permutation(k.begin(),k.end()));}float best=-1e9;string bp;vector<int>b1,b2;long long count=0;for(auto&k2:ks){string mid=dec(ct,k2);for(auto&k1:ks){string p=dec(mid,k1);float sc=score(p);count++;if(sc>best){best=sc;bp=p;b1=k1;b2=k2;}}}cout<<"evaluations "<<count<<"\nscore "<<best<<"\nkey1 ";for(int x:b1)cout<<x<<',';cout<<"\nkey2 ";for(int x:b2)cout<<x<<',';cout<<"\nplaintext "<<bp<<'\n';}
