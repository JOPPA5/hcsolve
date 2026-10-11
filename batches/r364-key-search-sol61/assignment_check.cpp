#define main search_main
#include "search.cpp"
#undef main
int main(){rng.seed(77119);int tests=0;for(int n=2;n<=7;n++)for(int t=0;t<50;t++){vector<vector<int>>cost(n,vector<int>(n));for(auto&row:cost)for(int&x:row)x=(int)(rng()%100)-50;auto a=assignment(cost);int got=0;for(int i=0;i<n;i++)got+=cost[i][a[i]];vector<int>p(n);iota(p.begin(),p.end(),0);int best=10000000;do{int z=0;for(int i=0;i<n;i++)z+=cost[i][p[i]];best=min(best,z);}while(next_permutation(p.begin(),p.end()));if(got!=best)return 1;tests++;}cout<<tests<<" independent exhaustive assignment comparisons passed\n";}
