#define main search_main
#include "search.cpp"
#undef main
int main(int argc,char**argv){ifstream in(argv[1]);string p,c;in>>p>>c;ifstream kf(argv[2]);Keys keys;for(int j=0;j<3;j++)for(int i=0,x;i<W[j];i++){kf>>x;keys[j].push_back(x);}rng.seed(21920);auto candidate=keys;candidate[0]=full21(p,c,keys);cout<<matches(cipher(p,candidate),c)<<"\n";return matches(cipher(p,candidate),c)==65?0:1;}
