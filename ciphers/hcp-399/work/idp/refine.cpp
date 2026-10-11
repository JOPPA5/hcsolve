#include <sstream>
#define main idpProgramMain
#include "idp-physical.cpp"
#undef main
vector<float> gram[6];
void loadGrams(string dir){for(int n=3;n<=5;n++){ifstream f(dir+"/model"+to_string(n)+".tsv");string s;float v;f>>s>>v;int total=1;for(int i=0;i<n;i++)total*=26;gram[n].assign(total,v);while(f>>s>>v){int ix=0;for(char c:s)ix=ix*26+c-'a';gram[n][ix]=v;}}}
float language(const string&s){float sc=0,wt[]={0,0,0,.15,.4,.8};for(int n=3;n<=5;n++){int ix=0,pow=1;for(int i=1;i<n;i++)pow*=26;for(int i=0;i<(int)s.size();i++){if(i>=n)ix-=(s[i-n]-'a')*pow;ix=ix*26+s[i]-'a';if(i>=n-1)sc+=wt[n]*gram[n][ix];}}return sc;}
Key readkey(string file){ifstream f(file);string s;f>>s;replace(s.begin(),s.end(),',',' ');istringstream ss(s);Key k;int x;while(ss>>x)k.push_back(x);return k;}
int main(int argc,char**argv){loadGrams(argv[1]);ifstream f(argv[2]);string ct;f>>ct;Key k1=readkey(argv[3]),k2=readkey(argv[4]);assert(!k1.empty()&&!k2.empty());auto t1=transforms(k1.size()),t2=transforms(k2.size());float sc=language(dec(dec(ct,k2),k1));for(int pass=0;pass<12;pass++){bool improved=false;for(int stage=0;stage<2;stage++){Key&key=stage?k2:k1;auto&ts=stage?t2:t1;Key best=key;float top=sc;for(auto&t:ts){Key candidate=inverseKey(transformKey(inverseKey(key),t));auto p=stage?dec(dec(ct,candidate),k1):dec(dec(ct,k2),candidate);float ns=language(p);if(ns>top){top=ns;best=candidate;}}if(top>sc+.001){key=best;sc=top;improved=true;}}cerr<<"pass="<<pass<<" score="<<sc<<endl;if(!improved)break;}cout<<sc<<" key1=";for(int x:k1)cout<<x<<",";cout<<" key2=";for(int x:k2)cout<<x<<",";cout<<" "<<dec(dec(ct,k2),k1)<<endl;}
