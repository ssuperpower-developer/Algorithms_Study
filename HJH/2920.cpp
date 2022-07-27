#include<iostream>
using namespace::std;
int func(int,int);
int main(void){
    int arr[8];
    int checkWhatItIs[7];
    for(int i=0;i<8;i++){
        cin>>arr[i];
    }
    int runTime = 0;
    while(runTime < 7){
        checkWhatItIs[runTime] = func(arr[runTime],arr[runTime+1]);
        ++runTime;
    }
    int temp;
    for(int i=0;i<7;i++){
        if(checkWhatItIs[i]==0){
            cout<<"mixed"<<endl;
            temp = 0;
            break;
        }
        else if(checkWhatItIs[i]==1){
            temp = 1;
            continue;
        }
        else if(checkWhatItIs[i]==2){
            temp =2;
            continue;
        }
    }
    if(temp == 1)   cout<<"ascending"<<endl;
    else if(temp == 2) cout<<"descending"<<endl;
    
    return 0;
}

int func (int a,int b){
    int tmp = a-b;
    if(tmp == -1)   return 1;
    else if (tmp == 1) return 2;
    else return 0;
}