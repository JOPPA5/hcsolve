#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <random>
#include <cmath>
using namespace std;
vector<float> models[3];float floors[3];float weights[]={.15,.4,.8};string ct;

string decode(const vector<int>&key){int w=key.size(),n=ct.size(),h=n/w,extra=n%w,at=0;string s(n,'.');for(int col:key){int len=h+(col<extra);for(int r=0;r<len;r++)s[r*w+col]=ct[at++];}return s;}
float score(const string&s){float total=0;for(int m=0;m<3;m++){int n=m+3;for(int i=0;i+n<=(int)s.size();i++){int id=0;bool ok=true;for(int j=0;j<n;j++){if(s[i+j]<'a'||s[i+j]>'z'){ok=false;break;}id=id*26+s[i+j]-'a';}if(ok)total+=weights[m]*models[m][id];}}return total;}
int main(int argc,char**argv){for(int m=0;m<3;m++){int len=pow(26,m+3);ifstream f(string(argv[1])+"/model"+to_string(m+3)+".tsv");string word;float val;f>>word>>floors[m];models[m].assign(len,floors[m]);while(f>>word>>val){int id=0;for(char c:word)id=id*26+c-'a';models[m][id]=val;}}ifstream f(argv[2]);f>>ct;mt19937 rng(369521);int first=stoi(argv[3]),last=stoi(argv[4]);for(int w=first;w<=last;w++){float best=-1e20;vector<int>bk;string bt;int extra=ct.size()%w;for(int restart=0;restart<24;restart++){vector<int>k(w);for(int i=0;i<w;i++)k[i]=i;shuffle(k.begin(),k.end(),rng);float sc=score(decode(k));for(int t=0;t<60000;t++){auto kk=k;int a=rng()%w,b=rng()%w;if(rng()%10<7){vector<int>eligible;for(int j=0;j<w;j++)if((k[j]<extra)==(k[a]<extra))eligible.push_back(j);b=eligible[rng()%eligible.size()];}swap(kk[a],kk[b]);if(t%13==0){int lo=min(a,b),hi=max(a,b);if(hi>lo)rotate(kk.begin()+lo,kk.begin()+lo+1,kk.begin()+hi+1);}string s=decode(kk);float ns=score(s);float temp=.2+5*(1-(t%6000)/6000.f);if(ns>sc||uniform_real_distribution<float>(0,1)(rng)<exp((ns-sc)/temp)){k=kk;sc=ns;}if(ns>best){best=ns;bk=kk;bt=s;}}}cout<<w<<" "<<best<<" ";for(int x:bk)cout<<x<<",";cout<<" "<<bt<<"\n"<<flush;}}
