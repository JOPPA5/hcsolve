#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
struct Row { double score; string keyword, text; int mode; };
int main(int argc,char**argv){
    ifstream corpus(argv[1]), model4(argv[2]), model5(argv[3]), input(argv[4]);
    map<string,double> models[6]; string gram; double v;
    while(model4>>gram>>v)models[4][gram]=v;
    while(model5>>gram>>v)models[5][gram]=v;
    string ct;input>>ct;vector<Row> best; string key;
    while(corpus>>key){
        int width=key.size();
        for(int mode=0;mode<4;mode++){
        vector<vector<int>> columns(width);int position=0,row=0,cell=0;
        while(position<ct.size()){
            for(int col=0;col<width && position<ct.size();col++,cell++){
                int size=1+((mode/2==0?cell:row+col)+(mode%2))%2;
                for(int j=0;j<size && position<ct.size();j++)columns[col].push_back(position++);
            }
            row++;
        }
        vector<int> cols;for(int c=0;c<width;c++)cols.push_back(c);
        stable_sort(cols.begin(),cols.end(),[&](int a,int b){return key[a]<key[b];});
        string pt(ct.size(),'.');int at=0;
        for(int col:cols)for(int index:columns[col])pt[index]=ct[at++];
        if(at!=ct.size())return 2;
        double score=0;
        for(int n=4;n<=5;n++)for(int i=0;i+n<=pt.size();i++){
            auto g=pt.substr(i,n);if(g.find('.')!=string::npos)continue;
            auto it=models[n].find(g);score+=(n==4?.4:.8)*(it==models[n].end()?-n:it->second);
        }
        best.push_back({score,key,pt,mode});
        if(best.size()>40){sort(best.begin(),best.end(),[](auto&a,auto&b){return a.score>b.score;});best.resize(20);}
        }
    }
    sort(best.begin(),best.end(),[](auto&a,auto&b){return a.score>b.score;});if(best.size()>20)best.resize(20);
    for(auto&r:best)cout<<r.score<<'\t'<<r.keyword<<'\t'<<r.mode<<'\t'<<r.text<<'\n';
}
