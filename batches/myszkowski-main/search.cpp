#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
struct Row { double score; string keyword, text; };
int main(int argc,char**argv){
    ifstream corpus(argv[1]), model4(argv[2]), model5(argv[3]), input(argv[4]);
    map<string,double> models[6]; string gram; double v;
    while(model4>>gram>>v)models[4][gram]=v;
    while(model5>>gram>>v)models[5][gram]=v;
    string ct;input>>ct;vector<Row> best; string key;
    while(corpus>>key){
        int width=key.size();string pt(ct.size(),'.');int at=0;
        string letters=key;sort(letters.begin(),letters.end());letters.erase(unique(letters.begin(),letters.end()),letters.end());
        for(char ch:letters)for(int row=0;row<ct.size();row+=width)for(int col=0;col<width;col++)
            if(key[col]==ch && row+col<ct.size())pt[row+col]=ct[at++];
        if(at!=ct.size())return 2;
        double score=0;
        for(int n=4;n<=5;n++)for(int i=0;i+n<=pt.size();i++){
            auto g=pt.substr(i,n);if(g.find('.')!=string::npos)continue;
            auto it=models[n].find(g);score+=(n==4?.4:.8)*(it==models[n].end()?-n:it->second);
        }
        best.push_back({score,key,pt});
        if(best.size()>40){sort(best.begin(),best.end(),[](auto&a,auto&b){return a.score>b.score;});best.resize(20);}
    }
    sort(best.begin(),best.end(),[](auto&a,auto&b){return a.score>b.score;});if(best.size()>20)best.resize(20);
    for(auto&r:best)cout<<r.score<<'\t'<<r.keyword<<'\t'<<r.text<<'\n';
}
