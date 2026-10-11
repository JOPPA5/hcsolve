#define main search_main
#include "multistage.cpp"
#undef main
int main(int argc,char**argv){ifstream c(argv[1]),f(argv[2]);string s;c>>s;int count,w;f>>count;vector<vector<int>>keys;for(int i=0;i<count;i++){f>>w;vector<int>k(w);for(int &v:k)f>>v;keys.push_back(k);}cout<<decrypt(s,keys)<<"\n";}
