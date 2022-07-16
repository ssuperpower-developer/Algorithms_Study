#include<iostream>
#include<stdio.h>
using namespace::std;

int main(void){
    int *arr = new int[10001];
    int N;
    scanf("%d",&N);
    int temp;
    for(int i=0;i<N;i++){
        scanf("%d",&temp);
        ++arr[temp];
    }
    for(int i=1;i<10001;i++){
        while(arr[i] > 0){
            cout<<i<<'\n';
            --arr[i];
        }
    }
    return 0;
}