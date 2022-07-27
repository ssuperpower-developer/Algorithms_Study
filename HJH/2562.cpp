#include<stdio.h>
int main(void){
    int arr[9];
    for(int i=0;i<9;i++){
        scanf("%d",&arr[i]);
    }
    int max=arr[0];
    int max_index=1;
    for(int i=1;i<9;i++){
        if(arr[i]>max){
            max=arr[i];
            max_index=i+1;
        }
    }
    printf("%d\n%d\n",max,max_index);
    return 0;
}