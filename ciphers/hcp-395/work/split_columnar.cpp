#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
#include <string>
using namespace std;float q[26*26*26*26];
float score(string s){float z=0;for(int i=0;i+3<s.size();i++)z+=q[((s[i]-'a')*26+s[i+1]-'a')*676+(s[i+2]-'a')*26+s[i+3]-'a'];return z;}
string dec(string s,vector<int> k){int w=k.size(),h=s.size()/w,e=s.size()%w,at=0;string o(s.size(),' ');for(int c:k)for(int r=0;r<h+(c<e);r++)o[r*w+c]=s[at++];return o;}
int main(int argc,char**argv){fill(begin(q),end(q),-4);ifstream f(argv[1]);string g;float v;while(f>>g>>v){int id=0;for(char c:g)id=id*26+c-'a';q[id]=v;}ifstream in(argv[2]);vector<string>groups;while(in>>g)groups.push_back(g);bool control=argc>3;vector<int>bounds;if(control)bounds={41};else for(int b=11;b<=46;b++)bounds.push_back(b);for(int boundary:bounds)for(int half=0;half<2;half++){int start=half?boundary:0,end=half?groups.size():boundary;float best=-1e9;string bp;vector<int>bk;int bo=0,bw=0,br=0;long count=0;for(int omit=-1;omit<end-start;omit++){string ct;for(int i=start;i<end;i++)if(i-start!=omit)ct+=groups[i];for(int w=2;w<=7;w++){vector<int> k(w);iota(k.begin(),k.end(),0);do{for(int rev=0;rev<2;rev++){string s=ct;if(rev)reverse(s.begin(),s.end());string p=dec(s,k);float z=score(p);count++;if(z>best){best=z;bp=p;bk=k;bo=omit;bw=w;br=rev;}}}while(next_permutation(k.begin(),k.end()));}}cout<<boundary<<" "<<half<<" "<<count<<" "<<best<<" "<<bo<<" "<<bw<<" "<<br<<" ";for(int c:bk)cout<<c<<",";cout<<" "<<bp<<endl;}}
