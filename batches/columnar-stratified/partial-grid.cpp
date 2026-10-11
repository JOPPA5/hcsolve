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
struct Node{uint32_t mask=0;array<unsigned char,26>key{};array<char,256>grid{};int consumed=0;float score=0;};
int main(int argc,char**argv){for(int m=0;m<4;m++){int n=m+2;ifstream f(string(argv[1])+"/model"+to_string(n)+".tsv");string word;float v;f>>word>>floors[m];models[m].assign((int)pow(26,n),floors[m]);while(f>>word>>v){int id=0;for(char c:word)id=id*26+c-'a';models[m][id]=v;}}ifstream f(argv[2]);string ct;f>>ct;int w=stoi(argv[3]),beam=stoi(argv[4]),n=ct.size();if(n>256||w<5||w>26)return 2;int q=n/w,extra=n%w;Node root;root.grid.fill('.');vector<Node>current{root};
for(int depth=0;depth<w;depth++){vector<Node>next;next.reserve(current.size()*(w-depth));for(auto&a:current)for(int col=0;col<w;col++)if(!(a.mask&(1u<<col))){Node b=a;b.mask|=1u<<col;b.key[depth]=col;for(int row=0;row<q+(col<extra);row++){int pos=row*w+col;b.grid[pos]=ct[b.consumed++];for(int m=0;m<4;m++){int len=m+2;for(int start=max(0,pos-len+1);start<=pos&&start+len<=n;start++){bool ok=true;int id=0;for(int j=start;j<start+len;j++){char ch=b.grid[j];if(ch<'a'||ch>'z'){ok=false;break;}id=id*26+ch-'a';}if(ok)b.score+=weights[m]*(models[m][id]+len*log(26.));}}}next.push_back(b);}if(next.size()>(size_t)beam){nth_element(next.begin(),next.begin()+beam,next.end(),[](auto&a,auto&b){return a.score>b.score;});next.resize(beam);}current=std::move(next);cout<<"# depth "<<depth+1<<" retained "<<current.size()<<"\n"<<flush;}
for(auto&a:current){float sc=0;for(int m=0;m<4;m++){int len=m+2;for(int i=0;i+len<=n;i++){int id=0;bool ok=true;for(int j=i;j<i+len;j++){char ch=a.grid[j];if(ch<'a'||ch>'z'){ok=false;break;}id=id*26+ch-'a';}if(ok)sc+=weights[m]*models[m][id];}}a.score=sc;}
sort(current.begin(),current.end(),[](auto&a,auto&b){return a.score>b.score;});for(int k=0;k<min(100,(int)current.size());k++){auto&a=current[k];cout<<a.score<<" ";for(int j=0;j<w;j++)cout<<(int)a.key[j]<<",";cout<<" "<<string(a.grid.data(),n)<<"\n";}}
