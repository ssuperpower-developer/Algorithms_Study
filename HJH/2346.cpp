#include<iostream>
#include <vector>
using namespace::std;

int main(void){
    int N;
    int tempInput;
    cin>>N;
    vector<pair <int,int> > vec;
    for(int i=1;i<=N;i++){
        cin>>tempInput;
        vec.push_back(make_pair(i,tempInput));
    }
    // 입력 
    int num;
    while(!vec.empty()){
        cout<<vec.front().first<<" ";
        num = vec.front().second;   // second - pair 의 두번째입력값
        vec.erase(vec.begin());
        if(vec.empty()) return 0;
        if(num>0){
            for(int i = 0 ;i<num-1;i++){
                vec.push_back(vec.front());
                vec.erase(vec.begin());
            }
        }
        else{
            for (int i = 0; i < abs(num); i++) {
                vec.insert(vec.begin(), vec.back());
                vec.erase(vec.end()-1);
            }
        }
    }
    return 0;
}