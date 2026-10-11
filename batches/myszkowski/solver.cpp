#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <numeric>
#include <queue>
#include <string>
#include <vector>
using namespace std;
vector<float> grams[6];string ct;long long tested=0;
struct Candidate{float score;string plain,key;bool operator<(const Candidate&o)const{return score>o.score;}};
priority_queue<Candidate> top;
void load(string dir){for(int n=3;n<=5;n++){ifstream f(dir+"/model"+to_string(n)+".tsv");string tag,s;float floor,v;f>>tag>>floor;int sz=1;for(int i=0;i<n;i++)sz*=26;grams[n].assign(sz,floor);while(f>>s>>v){int ix=0;for(char c:s)ix=ix*26+c-'a';grams[n][ix]=v;}}}
string dec(const vector<int>&k){int w=k.size(),r=*max_element(k.begin(),k.end());string out(ct.size(),'.');int at=0;for(int rank=0;rank<=r;rank++)for(int row=0;row*w<(int)ct.size();row++)for(int col=0;col<w;col++)if(k[col]==rank&&row*w+col<(int)ct.size())out[row*w+col]=ct[at++];return out;}
float score(const string&s){float z=0;float a[6]={0,0,0,.15,.4,.8};for(int n=3;n<=5;n++)for(int i=0;i+n<=(int)s.size();i++){int ix=0;bool ok=true;for(int j=0;j<n;j++){int v=s[i+j]-'a';if(v<0||v>25){ok=false;break;}ix=ix*26+v;}if(ok)z+=a[n]*grams[n][ix];}return z;}
void evaluate(const vector<int>&k){tested++;auto s=dec(k);float sc=score(s);if(top.size()<100||sc>top.top().score){string key;for(int x:k)key+=char('a'+x);top.push({sc,s,key});if(top.size()>100)top.pop();}}
// Ordered set partitions: every onto rank assignment occurs once, including ties.
void enumerate(vector<int>&k,int pos,int ranks,int mask){if(pos==(int)k.size()){if(mask==(1<<ranks)-1)evaluate(k);return;}for(int x=0;x<ranks;x++){k[pos]=x;enumerate(k,pos+1,ranks,mask|(1<<x));}}
int main(int argc,char**argv){if(argc<5)return 2;load(argv[1]);ifstream f(argv[2]);f>>ct;int maxw=stoi(argv[3]);for(int w=2;w<=maxw;w++)for(int ranks=1;ranks<=w;ranks++){vector<int>k(w);enumerate(k,0,ranks,0);}ifstream keys(argv[4]);string s;while(keys>>s){vector<int>k;for(char c:s)k.push_back(c-'a');if(k.size()>maxw)evaluate(k);}vector<Candidate>out;while(!top.empty()){out.push_back(top.top());top.pop();}reverse(out.begin(),out.end());cout<<"tested "<<tested<<"\n";for(auto&r:out)cout<<r.score<<" "<<r.key<<" "<<r.plain<<"\n";}
