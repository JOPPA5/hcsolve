#include "language.hpp"
#include <set>
#include <numeric>
vector<int>holes;array<int,52>coord;int m;
vector<vector<int>> physical(const vector<int>&h){vector<vector<int>>v;int start=h[0];for(auto&ct:cipher){vector<int>x;for(int i=0;i<ct.size();i++){int stop=h[i%m],dis=coord[stop]-coord[start]+(stop<start?179:0)+179*(i/m);x.push_back(((O[ct[i]]-dis)%26+26)%26);}v.push_back(x);}return v;}
int main(int argc,char**argv){load(argv[1],argv[2],argv[3],argv[4]);ifstream co(argv[5]);for(int&x:coord)co>>x;ifstream ring(argv[6]);for(int&x:P)ring>>x;for(int&x:O)ring>>x;ifstream stops(argv[7]);int h;while(stops>>h)holes.push_back(h);m=holes.size();assert(m>=20&&m<=30);float now=score(P,physical(holes));
 for(int iteration=0;iteration<8;iteration++){
  set<vector<int>>masks{holes};
  for(int pos=0;pos<m;pos++)for(int replacement=0;replacement<52;replacement++)if(find(holes.begin(),holes.end(),replacement)==holes.end()){
   auto candidate=holes;int start=pos==0?replacement:candidate[0];candidate[pos]=replacement;sort(candidate.begin(),candidate.end());rotate(candidate.begin(),find(candidate.begin(),candidate.end(),start),candidate.end());masks.insert(candidate);
  }
  for(int phase=1;phase<m;phase++){auto candidate=holes;rotate(candidate.begin(),candidate.begin()+phase,candidate.end());masks.insert(candidate);}
  float best=now;auto bp=P;auto bh=holes;long evaluations=0;
  for(auto&candidate:masks){auto v=physical(candidate);
   auto consider=[&](const array<int,26>&pp){float next=score(pp,v);evaluations++;if(next>best+.0001){best=next;bp=pp;bh=candidate;}};
   consider(P);
   for(int a=0;a<26;a++)for(int b=a+1;b<26;b++){auto pp=P;swap(pp[a],pp[b]);consider(pp);}
   for(int shift=1;shift<26;shift++){auto pp=P;rotate(pp.begin(),pp.begin()+shift,pp.end());consider(pp);}
  }
  cerr<<"local iteration "<<iteration<<" masks "<<masks.size()<<" joint evaluations "<<evaluations<<" before "<<now<<" after "<<best<<'\n';
  if(best<=now+.0001)break;P=bp;holes=bh;now=best;
 }
 d.clear();for(auto&ct:cipher){vector<int>x;for(int i=0;i<ct.size();i++){int stop=holes[i%m];x.push_back((coord[stop]-coord[holes[0]]+(stop<holes[0]?179:0)+179*(i/m))%26);}d.push_back(x);}emit(now,P,O);for(int x:holes)cout<<x<<' ';cout<<'\n';
}
