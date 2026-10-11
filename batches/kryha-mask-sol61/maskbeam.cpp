#include <algorithm>
#include <array>
#include <cassert>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;vector<float>grams[6];int coord[52],P[26],O[26],m,anchor,width;string ct;float weight[6]={0,0,.1,.15,.4,.8};int v[30][52][30];struct Node{array<unsigned char,30>h;float score;};
float gramvalue(int n,int pos,const Node&x){int ix=0;for(int j=0;j<n;j++){int i=pos+j;ix=ix*26+v[i%m][x.h[i%m]][i/m];}return grams[n][ix]*weight[n];}
float inside(int r,const Node&x){float score=0;for(int n=2;n<=5;n++)if(r+1>=n)for(int pos=r-n+1;pos+n<=ct.size();pos+=m)score+=gramvalue(n,pos,x);return score;}
float wrap(const Node&x){float score=0;for(int n=2;n<=5;n++)for(int pos=0;pos+n<=ct.size();pos++)if(pos%m+n>m)score+=gramvalue(n,pos,x);return score;}
string plaintext(const Node&x){string s;for(int i=0;i<ct.size();i++)s+=char('a'+v[i%m][x.h[i%m]][i/m]);return s;}
void precompute(){for(int r=0;r<m;r++)for(int h=0;h<52;h++){int actual=(anchor+h)%52;int displacement=coord[actual]-coord[anchor]+(actual<anchor?179:0);for(int q=0;r+q*m<ct.size();q++)v[r][h][q]=P[((O[ct[r+q*m]-'a']-displacement-23*q)%26+26)%26];}}
int main(int argc,char**argv){ifstream f(argv[1]);f>>ct;m=stoi(argv[2]);width=stoi(argv[3]);ifstream keys(argv[4]);for(int&x:P)keys>>x;for(int&x:O)keys>>x;ifstream coordinates(argv[5]);for(int&x:coord)coordinates>>x;for(int n=2;n<=5;n++){int size=1;for(int j=0;j<n;j++)size*=26;grams[n].assign(size,-n);ifstream model(string(argv[6])+(n<4?"/model":"/ring-")+to_string(n)+(n<4?".tsv":"grams.tsv"));if(n>=4){model.close();model.open(string(argv[7])+"/ring-"+to_string(n)+"grams.tsv");}assert(model);string s;float val;while(model>>s>>val){int ix=0;for(char c:s)ix=ix*26+c-'a';grams[n][ix]=val;}}for(anchor=0;anchor<52;anchor++){precompute();Node first{};first.h[0]=0;first.score=0;vector<Node>beam{first};for(int r=1;r<m;r++){vector<Node>next;for(auto&x:beam)for(int h=x.h[r-1]+1;h<=52-(m-r);h++){Node y=x;y.h[r]=h;y.score=x.score+inside(r,y);if(r==m-1)y.score+=wrap(y);next.push_back(y);}int keep=min(width,int(next.size()));if(keep<next.size())nth_element(next.begin(),next.begin()+keep,next.end(),[](auto&a,auto&b){return a.score>b.score;});next.resize(keep);beam=std::move(next);}sort(beam.begin(),beam.end(),[](auto&a,auto&b){return a.score>b.score;});for(int rank=0;rank<min(4,int(beam.size()));rank++){auto x=beam[rank];cout<<anchor<<'\t'<<rank<<'\t'<<x.score<<'\t';for(int r=0;r<m;r++)cout<<(r?",":"")<<(anchor+x.h[r])%52;cout<<'\t'<<plaintext(x)<<'\n'<<flush;}cerr<<anchor<<" done\n"<<flush;}}
