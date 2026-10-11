#include "frozen-score.hpp"
#include <sstream>
struct Ranked{float score;string line;};
int main(int argc,char**argv){load(argv[1]);ifstream f(argv[2]);string line;getline(f,line);vector<Ranked> ranked;while(getline(f,line)){istringstream in(line);string lang,order,ref,ring,plain;float old;in>>lang>>old>>order>>ref>>ring>>plain;if(lang!=argv[3])continue;ranked.push_back({score(plain),line});}sort(ranked.begin(),ranked.end(),[](auto&a,auto&b){return a.score>b.score;});for(auto r:ranked)cout<<r.score<<" "<<r.line<<"\n";}
