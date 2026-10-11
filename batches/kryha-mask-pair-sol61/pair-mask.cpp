#include <algorithm>
#include <array>
#include <cassert>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;vector<float>grams[6];int coord[52],P[26],O[26],m=26,anchor,width;vector<string>cts;float weights[6]={0,0,.1,.15,.4,.8};int v[26][52][2][30];struct Node{array<unsigned char,26>h;float score;};
float gramvalue(int msg,int n,int pos,const Node&x){int ix=0;for(int j=0;j<n;j++){int i=pos+j;ix=ix*26+v[i%m][x.h[i%m]][msg][i/m];}return weights[n]*grams[n][ix];}
float inside(int r,const Node&x){float sum=0;for(int msg=0;msg<cts.size();msg++)for(int n=2;n<=5;n++)if(r+1>=n)for(int pos=r-n+1;pos+n<=cts[msg].size();pos+=m)sum+=gramvalue(msg,n,pos,x);return sum;}
float wrap(const Node&x){float sum=0;for(int msg=0;msg<cts.size();msg++)for(int n=2;n<=5;n++)for(int pos=0;pos+n<=cts[msg].size();pos++)if(pos%m+n>m)sum+=gramvalue(msg,n,pos,x);return sum;}
void precompute(){for(int r=0;r<m;r++)for(int h=0;h<52;h++){int actual=(anchor+h)%52;int dis=coord[actual]-coord[anchor]+(actual<anchor?179:0);for(int msg=0;msg<cts.size();msg++)for(int q=0;r+q*m<cts[msg].size();q++)v[r][h][msg][q]=P[((O[cts[msg][r+q*m]-'a']-dis-23*q)%26+26)%26];}}
string plaintext(int msg,const Node&x){string s;for(int i=0;i<cts[msg].size();i++)s+=char('a'+v[i%m][x.h[i%m]][msg][i/m]);return s;}
int main(int argc,char**argv){ifstream f(argv[1]);string s;while(f>>s)cts.push_back(s);assert(cts.size()==2);width=stoi(argv[2]);ifstream keys(argv[3]);for(int&x:P)keys>>x;for(int&x:O)keys>>x;ifstream coordinates(argv[4]);for(int&x:coord)coordinates>>x;for(int n=2;n<=5;n++){int size=1;for(int i=0;i<n;i++)size*=26;grams[n].assign(size,-n);ifstream model(n<4?string(argv[5])+"/model"+to_string(n)+".tsv":string(argv[6])+"/ring-"+to_string(n)+"grams.tsv");assert(model);float val;while(model>>s>>val){int ix=0;for(char c:s)ix=ix*26+c-'a';grams[n][ix]=val;}}for(anchor=0;anchor<52;anchor++){precompute();Node first{};vector<Node>beam{first};for(int r=1;r<m;r++){vector<Node>next;for(auto&x:beam)for(int h=x.h[r-1]+1;h<=52-(m-r);h++){Node y=x;y.h[r]=h;y.score=x.score+inside(r,y);if(r==m-1)y.score+=wrap(y);next.push_back(y);}int keep=min(width,int(next.size()));if(keep<next.size())nth_element(next.begin(),next.begin()+keep,next.end(),[](auto&a,auto&b){return a.score>b.score;});next.resize(keep);beam=std::move(next);}sort(beam.begin(),beam.end(),[](auto&a,auto&b){return a.score>b.score;});for(int rank=0;rank<min(4,int(beam.size()));rank++){auto x=beam[rank];cout<<anchor<<'\t'<<rank<<'\t'<<x.score<<'\t';for(int j=0;j<m;j++)cout<<(j?",":"")<<(anchor+x.h[j])%52;cout<<'\t'<<plaintext(0,x)<<'\t'<<plaintext(1,x)<<'\n'<<flush;}}}
