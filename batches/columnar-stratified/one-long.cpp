#include <algorithm>
#include <array>
#include <cmath>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <cstdint>
using namespace std;
vector<float>models[4];float floors[4];float weights[]={.2,.15,.4,.8};
struct Node{uint32_t mask=0;array<unsigned char,26> key{};float score=0;};
int main(int argc,char**argv){for(int m=0;m<4;m++){int n=m+2;ifstream f(string(argv[1])+"/model"+to_string(n)+".tsv");string word;float v;f>>word>>floors[m];models[m].assign((int)pow(26,n),floors[m]);while(f>>word>>v){int id=0;for(char c:word)id=id*26+c-'a';models[m][id]=v;}}ifstream f(argv[2]);string ct;f>>ct;int w=stoi(argv[3]),beam=stoi(argv[4]);if(ct.size()%w!=1||w>26)return 2;int h=ct.size()/w;for(int longindex=0;longindex<w;longindex++){vector<string>chunks;int at=0;for(int j=0;j<w;j++){int len=h+(j==longindex);chunks.push_back(ct.substr(at,len));at+=len;}vector<Node>current(1);
for(int d=0;d<w;d++){vector<Node>next;next.reserve(current.size()*(w-d));for(auto &a:current)for(int col=0;col<w;col++)if(!(a.mask&(1u<<col))&&((d==0)==(col==longindex))){Node b=a;b.mask|=1u<<col;b.key[d]=col;for(int m=0;m<4;m++){int n=m+2;if(d+1<n)continue;for(int row=0;row<=h;row++){int id=0;bool ok=true;for(int k=d+1-n;k<=d;k++){if(row>=(int)chunks[b.key[k]].size()){ok=false;break;}char ch=chunks[b.key[k]][row];if(ch<'a'||ch>'z'){ok=false;break;}id=id*26+ch-'a';}if(ok)b.score+=weights[m]*models[m][id];}}next.push_back(b);}if(next.size()>(size_t)beam){nth_element(next.begin(),next.begin()+beam,next.end(),[](auto&a,auto&b){return a.score>b.score;});next.resize(beam);}current=std::move(next);}
for(auto &a:current){string s;for(int row=0;row<=h;row++)for(int j=0;j<w;j++)if(row<(int)chunks[a.key[j]].size())s+=chunks[a.key[j]][row];float score=0;for(int m=0;m<4;m++){int n=m+2;for(int i=0;i+n<=(int)s.size();i++){int id=0;bool ok=true;for(int j=0;j<n;j++){char ch=s[i+j];if(ch<'a'||ch>'z'){ok=false;break;}id=id*26+ch-'a';}if(ok)score+=weights[m]*models[m][id];}}a.score=score;}
sort(current.begin(),current.end(),[](auto&a,auto&b){return a.score>b.score;});for(int k=0;k<min(100,(int)current.size());k++){auto&a=current[k];cout<<a.score<<" ";for(int j=0;j<w;j++)cout<<(int)a.key[j]<<",";cout<<" ";for(int row=0;row<=h;row++)for(int j=0;j<w;j++)if(row<(int)chunks[a.key[j]].size())cout<<chunks[a.key[j]][row];cout<<"\n";}}}
