#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <vector>
#include <set>
using namespace std;
struct A{int off;string word,key;};
int main(int argc,char**argv){ifstream f(argv[1]);vector<A>a;A x;while(f>>x.off>>x.word>>x.key)a.push_back(x);vector<pair<int,string>>pool;long compatible=0;set<string>unique;
for(int i=0;i<(int)a.size();i++)for(int j=i+1;j<(int)a.size();j++){auto&b=a[i];auto&c=a[j];if(!(b.off+(int)b.word.size()<=c.off||c.off+(int)c.word.size()<=b.off))continue;string key=b.key;array<int,26>inv;inv.fill(-1);for(int z=0;z<26;z++)if(key[z]!='-')inv[key[z]-'a']=z;bool ok=true;for(int z=0;z<26;z++)if(c.key[z]!='-'){int y=c.key[z]-'a';if((key[z]!='-'&&key[z]!=c.key[z])||(inv[y]>=0&&inv[y]!=z)){ok=false;break;}key[z]=c.key[z];inv[y]=z;}if(!ok)continue;compatible++;if(!unique.insert(key).second)continue;int n=26-count(key.begin(),key.end(),'-');pool.push_back({n*100+int(b.word.size()+c.word.size()),key});}
sort(pool.begin(),pool.end(),[](auto&b,auto&c){return b.first>c.first||(b.first==c.first&&b.second<c.second);});ofstream out(argv[2]);mt19937 rng(610335);int limit=argc>3?stoi(argv[3]):100000;for(int i=0;i<min(limit,(int)pool.size());i++){string key=pool[i].second,mask;vector<int>free;for(int y=0;y<26;y++)if(key.find('a'+y)==string::npos)free.push_back(y);shuffle(free.begin(),free.end(),rng);for(int z=0;z<26;z++){mask+=key[z]=='-'?'0':'1';if(key[z]=='-'){key[z]='a'+free.back();free.pop_back();}}out<<key<<" "<<mask<<"\n";}cerr<<"anchors="<<a.size()<<" compatible_pairs="<<compatible<<" unique_partial_keys="<<pool.size()<<" written="<<min(limit,(int)pool.size())<<"\n";}
