#include<algorithm>
#include<iostream>
#include<stdio.h>
using namespace std;

int main(){
    // 이분탐색
    int N;
    cin>>N;
    int *arr1 = new int[N];
    for(int i=0;i<N;i++){
        scanf("%d",&arr1[i]);
    }
    int K;
    cin>>K;
    int *arr2 = new int[K];
    for(int i=0;i<K;i++){
        scanf("%d",&arr2[i]);
    }
    
    int *result = new int[K];
    sort(arr1,arr1+N);

   // 이분 탐색 수행
    int left = 0, right = N-1; // left, right 초기화
    for(int i=0;i<K;i++){
        left = 0, right = N-1; // left, right 초기화
        while(left<=right){
            int mid = (left+right)/2;
            if(arr1[mid]==arr2[i]){
                result[i] = 1;
                break;
            }
            else if(arr1[mid]>arr2[i]){
                    right = mid-1;
            }
            else{
                left = mid+1;
            }
        }
    }
    for(int i=0;i<K;i++){
        cout<<result[i]<<'\n';
    }
    return 0;
}