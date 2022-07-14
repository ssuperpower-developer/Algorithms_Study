#include<stdio.h>
int main(void){
int N;
scanf("%d",&N);
for(int i=1;i<=N;i++){
        for(int k=1;k<=N-i;k++){
                printf(" ");
                }
        for(int f=1;f<=i;f++){
                printf("*");
                }
        printf("\n");
        }
return 0;
}