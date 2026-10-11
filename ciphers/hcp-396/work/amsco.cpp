#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
#include <string>
using namespace std;
float q[26*26*26*26];
int id(string s){int z=0;for(char c:s)z=z*26+c-'a';return z;}
float score(string s){float z=0;for(int i=0;i+3<s.size();i++)z+=q[id(s.substr(i,4))];return z;}
vector<vector<int>> cells(int n,int w,int phase,int mode){vector<vector<int>> a(w);int at=0,r=0;while(at<n){for(int c=0;c<w && at<n;c++){int len=1+((phase+c+(mode?r:r*w))%2);for(int j=0;j<len&&at<n;j++)a[c].push_back(at++);}r++;}return a;}
string dec(string ct,vector<int> k,int phase,int mode){auto a=cells(ct.size(),k.size(),phase,mode);string p(ct.size(),' ');int at=0;for(int c:k)for(int i:a[c])p[i]=ct[at++];return p;}
int main(int argc,char**argv){fill(begin(q),end(q),-4.0);ifstream f(argv[1]);string gram;float v;while(f>>gram>>v)q[id(gram)]=v;ifstream in(argv[2]);string ct;in>>ct;for(int w=2;w<=8;w++){vector<int> k(w);iota(k.begin(),k.end(),0);float best=-1e9;string bp;vector<int> bk;int bf=0,bm=0,br=0;long count=0;do{for(int phase=0;phase<2;phase++)for(int mode=0;mode<2;mode++)for(int rev=0;rev<2;rev++){string s=ct;if(rev)reverse(s.begin(),s.end());string p=dec(s,k,phase,mode);float sc=score(p);count++;if(sc>best){best=sc;bp=p;bk=k;bf=phase;bm=mode;br=rev;}}}while(next_permutation(k.begin(),k.end()));cout<<w<<" "<<count<<" "<<best<<" "<<bf<<" "<<bm<<" "<<br<<" ";for(int c:bk)cout<<c<<",";cout<<" "<<bp<<endl;}}
