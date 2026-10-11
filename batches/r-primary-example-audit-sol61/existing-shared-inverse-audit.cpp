#define main existing_search_main
#include "../shared-r-sol61/joint.cpp"
#undef main
#include <cassert>
int main(){Keys keys={Key{7,10,21,3,18,6,20,1,19,15,9,13,5,16,2,17,4,12,8,11,14},Key{7,15,8,6,18,3,10,9,17,14,2,13,1,19,11,5,12,4,16},Key{7,20,3,12,6,19,8,16,2,17,1,18,11,5,9,4,10,15,14,13}};vector<string>s={"stahovanievyslanectvanutnexposlitesemihnedsluzobnyvozxx","noyaehnzeisexvxbsnstnviztulvechytxadelolsnmoeoisvapnatu","xypscvhtonebatainntoyvszlonuexxasduehaiesonlsleviezmvtn","exzoeipsnietdtclsxyshneaunnhasvszloetinatuvnxebamvolyvo"};for(int j=0;j<3;j++){assert(inv(s[j+1],keys[j],7)==s[j]);canon(keys[j]);assert(inv(s[j+1],keys[j],7)==s[j]);cout<<"existing shared inverse stage "<<j+1<<" canonical/noncanonical PASS\n";}}
