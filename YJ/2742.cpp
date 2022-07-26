#include<iostream>
using namespace std;

int main(){
    int N;
    cin>>N;

    for(int i=N;i>0;i--)
        cout<<i<<'\n'; //endl하면 시간초과 남
}