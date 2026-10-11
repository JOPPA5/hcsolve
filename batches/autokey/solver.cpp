#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <random>
#include <cmath>
using namespace std;
vector<float> models[3];float floors[3];float weights[]={.15,.4,.8};string ct;int mode;
string decode(const vector<int>&key){string s=ct;int w=key.size();for(int i=0;i<(int)s.size();i++){int k=i<w?key[i]:((mode<3?s[i-w]:ct[i-w])-'a');if(ct[i]< 'a'||ct[i]>'z'||k<0||k>=26){s[i]='.';continue;}int c=ct[i]-'a';int p=mode%3==0?c-k:(mode%3==1?k-c:c+k);s[i]='a'+(p%26+26)%26;}return s;}
float score(const string&s){float total=0;for(int m=0;m<3;m++){int n=m+3;for(int i=0;i+n<=(int)s.size();i++){int id=0;bool ok=true;for(int j=0;j<n;j++){if(s[i+j]<'a'||s[i+j]>'z'){ok=false;break;}id=id*26+s[i+j]-'a';}if(ok)total+=weights[m]*models[m][id];}}return total;}
int main(int argc,char**argv){for(int m=0;m<3;m++){int len=pow(26,m+3);ifstream f(string(argv[1])+"/model"+to_string(m+3)+".tsv");string word;float val;f>>word>>floors[m];models[m].assign(len,floors[m]);while(f>>word>>val){int id=0;for(char c:word)id=id*26+c-'a';models[m][id]=val;}}ifstream f(argv[2]);f>>ct;mt19937 rng(369884);int maxw=argc>3?stoi(argv[3]):12;int restarts=argc>4?stoi(argv[4]):12;
int firstmode=argc>5?stoi(argv[5]):0; int lastmode=argc>5?firstmode+1:6; for(mode=firstmode;mode<lastmode;mode++)for(int w=1;w<=maxw;w++){float best=-1e20;vector<int>bk;string bt;auto retain=[&](const vector<int>&k){string s=decode(k);float v=score(s);if(v>best){best=v;bk=k;bt=s;}return v;};if(w<=3){int limit=pow(26,w);for(int x=0;x<limit;x++){vector<int>k(w);int z=x;for(int&i:k){i=z%26;z/=26;}retain(k);}}else{for(int r=0;r<restarts;r++){vector<int>k(w);for(int&i:k)i=rng()%26;float v=retain(k);for(int t=0;t<10000;t++){int pos=rng()%w,old=k[pos];k[pos]=rng()%26;float nv=retain(k);float temp=.4+8*(1-(t%2000)/2000.f);if(nv>v||uniform_real_distribution<float>(0,1)(rng)<exp((nv-v)/temp))v=nv;else k[pos]=old;}}}cout<<mode<<" "<<w<<" "<<best<<" ";for(int i:bk)cout<<char('a'+i);cout<<" "<<bt<<"\n"<<flush;}}
