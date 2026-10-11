#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;
vector<float> q(26*26*26*26,-4);
int idx(const string&s){int r=0;for(char c:s)r=r*26+c-'a';return r;}
string decrypt(const string &ct,const vector<int>&k){int n=ct.size(),w=k.size(),a=0;string p(n,' ');for(int col:k)for(int row=0;row<n/w+(col<n%w);row++)p[row*w+col]=ct[a++];return p;}
string encrypt(const string&p,const vector<int>&k){string c;for(int col:k)for(int i=col;i<(int)p.size();i+=k.size())c+=p[i];return c;}
float score(const string&s){float t=0;for(size_t i=0;i+3<s.size();i++)t+=q[(((s[i]-'a')*26+s[i+1]-'a')*26+s[i+2]-'a')*26+s[i+3]-'a'];return t;}
string attack(const string&ct,int w,const string&label){vector<int>k(w),bk; iota(k.begin(),k.end(),0);float best=-1e20;string bp;long count=0;do{auto p=decrypt(ct,k);float s=score(p);if(s>best){best=s;bp=p;bk=k;}count++;}while(next_permutation(k.begin(),k.end()));cout<<label<<" width="<<w<<" length="<<ct.size()<<" tested="<<count<<" score="<<best<<" key=";for(int x:bk)cout<<x<<",";cout<<"\n"<<bp<<"\n";return bp;}
int main(){ifstream f("ciphers/hcp-393/work/quadgrams.tsv");string x;float v;while(f>>x>>v)q[idx(x)]=v;
string control="dnesprisielzrimavatikantelegramvktoromvyslanectvoziadaopakovaniepredchadzajucejspravytextsmeprekontrolovaliaposlalismehoponovnepretozeporuchapravdepodobnevzniklapriprenosenapostenoveoznamenieposielamediplomatickoucestouaziadamepotvrdenieprijatiaspravybezposkodenia";vector<int> key={3,0,8,5,1,7,4,2,6}; auto got=attack(encrypt(control,key),9,"positive_control");cout<<"control_exact="<<(got==control)<<"\n";if(got!=control)return 2;
for(int number:{395,396}){ifstream in("ciphers/hcp-"+to_string(number)+"/work/transcription.txt");vector<string> groups;while(in>>x)groups.push_back(x);for(bool remove:{false,true}){string ct;for(int i=0;i<(int)groups.size();i++)if(!remove||i!=7)ct+=groups[i];for(bool rev:{false,true}){string c=ct;if(rev)reverse(c.begin(),c.end());attack(c,number==395?9:7,to_string(number)+" remove_group8="+to_string(remove)+" reversed="+to_string(rev));}}}
}
