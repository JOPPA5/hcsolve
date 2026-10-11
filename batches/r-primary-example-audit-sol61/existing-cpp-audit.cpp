#define main existing_search_main
#include "../analysis-395-396/joint_r.cpp"
#undef main
int main(){Keys keys={{7,10,21,3,18,6,20,1,19,15,9,13,5,16,2,17,4,12,8,11,14},{7,15,8,6,18,3,10,9,17,14,2,13,1,19,11,5,12,4,16},{7,20,3,12,6,19,8,16,2,17,1,18,11,5,9,4,10,15,14,13}};vector<string> s={"stahovanievyslanectvanutnexposlitesemihnedsluzobnyvozxx","noyaehnzeisexvxbsnstnviztulvechytxadelolsnmoeoisvapnatu","xypscvhtonebatainntoyvszlonuexxasduehaiesonlsleviezmvtn","exzoeipsnietdtclsxyshneaunnhasvszloetinatuvnxebamvolyvo"};for(int j=0;j<3;j++){assert(stage(s[j],keys[j],7,true)==s[j+1]);assert(stage(s[j+1],keys[j],7,false)==s[j]);cout<<"existing joint_r stage "<<j+1<<" exact encoder/inverse PASS\n";}assert(cascade(s[0],keys,7,true)==s[3]);assert(cascade(s[3],keys,7,false)==s[0]);}
