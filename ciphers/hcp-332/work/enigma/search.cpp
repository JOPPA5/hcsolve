#include <algorithm>
#include <array>
#include <cassert>
#include <fstream>
#include <iostream>
#include <queue>
#include <string>
#include <vector>
using namespace std;
int mod(int n){n%=26;return n<0?n+26:n;}
struct Wheel{array<int,26>f,b;int notch;};
vector<Wheel> wheels;
vector<array<int,26>> reflectors;
int fw[8][26][26],bw[8][26][26];
array<int,26> wiring(string s,bool ref=false){assert(s.size()==26);array<int,26>a;array<bool,26>seen{};for(int i=0;i<26;i++){a[i]=s[i]-'A';assert(a[i]>=0&&a[i]<26&&!seen[a[i]]);seen[a[i]]=true;}if(ref)for(int i=0;i<26;i++)assert(a[a[i]]==i&&a[i]!=i);return a;}
void init(){string ss[]={"EKMFLGDQVZNTOWYHXUSPAIBRCJ","AJDKSIRUXBLHWTMCQGZNPYFVOE","BDFHJLCPRTXVZNYEIWGAKMUSQO","ESOVPZJAYQUIRHXLNFTGKDCMWB","VZBRGITYUPSDNHLXAWMJQOFECK"};string nt="QEVJZ";for(int i=0;i<5;i++){Wheel w;w.f=wiring(ss[i]);for(int j=0;j<26;j++)w.b[w.f[j]]=j;w.notch=nt[i]-'A';wheels.push_back(w);for(int p=0;p<26;p++)for(int j=0;j<26;j++){fw[i][p][j]=mod(w.f[(j+p)%26]-p);bw[i][p][j]=mod(w.b[(j+p)%26]-p);}}for(string s:{"EJMZALYXVBWFCRQUONTSPIKHGD","YRUHQSLDPXNGOKMIEBFZCWVJAT","FVPJIAOYEDRZXWGCTKUQSBNMHL"})reflectors.push_back(wiring(s,true));}
string crypt(string s,array<int,3>order,array<int,3>ring,string window,int ref,string plugs=""){array<int,26>pb;for(int i=0;i<26;i++)pb[i]=i;for(int i=0;i+1<(int)plugs.size();i+=2)swap(pb[plugs[i]-'A'],pb[plugs[i+1]-'A']);array<int,3>p;for(int i=0;i<3;i++)p[i]=window[i]-'A';string out;for(char c:s){bool mid=p[1]==wheels[order[1]].notch;bool right=p[2]==wheels[order[2]].notch;if(mid)p[0]=(p[0]+1)%26;if(mid||right)p[1]=(p[1]+1)%26;p[2]=(p[2]+1)%26;int x=pb[toupper(c)-'A'];for(int i=2;i>=0;i--)x=fw[order[i]][mod(p[i]-ring[i])][x];x=reflectors[ref][x];for(int i=0;i<3;i++)x=bw[order[i]][mod(p[i]-ring[i])][x];out+='a'+pb[x];}return out;}
struct Model{vector<float>g[6];Model(string dir){for(int n=3;n<=5;n++){ifstream f(dir+"/model"+to_string(n)+".tsv");string tag,s;float floor,v;f>>tag>>floor;assert(f);int total=1;for(int j=0;j<n;j++)total*=26;g[n].assign(total,floor);while(f>>s>>v){int ix=0;for(char c:s)ix=ix*26+c-'a';g[n][ix]=v;}}}float score(const string&s){float result=0;float wt[]={0,0,0,.15,.4,.8};for(int n=3;n<=5;n++){int ix=0,pow=1;for(int i=1;i<n;i++)pow*=26;for(int i=0;i<(int)s.size();i++){if(i>=n)ix-=(s[i-n]-'a')*pow;ix=ix*26+s[i]-'a';if(i>=n-1)result+=wt[n]*g[n][ix];}}return result;}};
struct Candidate{float score;array<int,3>order,ring;int ref;string plain;bool operator<(const Candidate&c)const{return score>c.score;}};
int main(int argc,char**argv){init();if(string(argv[1])=="crypt"){array<int,3>o,r;for(int i=0;i<3;i++){o[i]=argv[2][i]-'1';r[i]=argv[3][i]-'A';}cout<<crypt(argv[6],o,r,argv[4],argv[5][0]-'A',argc>7?argv[7]:"")<<'\n';return 0;}Model sk(argv[1]),de(argv[2]);ifstream in(argv[3]);string ct;in>>ct;priority_queue<Candidate>best[2];long count=0;for(int a=0;a<5;a++)for(int b=0;b<5;b++)for(int c=0;c<5;c++)if(a!=b&&a!=c&&b!=c){array<int,3>o{a,b,c};for(int ref=0;ref<3;ref++)for(int x=0;x<26;x++)for(int y=0;y<26;y++)for(int z=0;z<26;z++){array<int,3>r{x,y,z};string p=crypt(ct,o,r,"TRC",ref);float scores[]={sk.score(p),de.score(p)};for(int lang=0;lang<2;lang++){Candidate v{scores[lang],o,r,ref,p};if(best[lang].size()<1000)best[lang].push(v);else if(v.score>best[lang].top().score){best[lang].pop();best[lang].push(v);}}count++;}cerr<<"order "<<a+1<<b+1<<c+1<<" checked="<<count<<'\n';}cout<<"checked "<<count<<" window TRC plugboard empty\n";for(int lang=0;lang<2;lang++){vector<Candidate>v;while(!best[lang].empty()){v.push_back(best[lang].top());best[lang].pop();}reverse(v.begin(),v.end());for(auto k:v){cout<<(lang==0?"sk":"de")<<' '<<k.score<<' ';for(int x:k.order)cout<<x+1;cout<<' '<<char('A'+k.ref)<<' ';for(int x:k.ring)cout<<char('A'+x);cout<<' '<<k.plain<<'\n';}}}
