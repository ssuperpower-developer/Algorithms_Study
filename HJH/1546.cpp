#include<stdio.h>
#include<stdlib.h>
int main(void){
int n;
scanf("%d",&n);
double *arr;
double m=0,sum=0;
double result;
arr=(double *)malloc(sizeof(double)*n);
for(int p=0;p<n;p++){
        scanf("%lf",&arr[p]);
        }

for(int i=0;i<n;i++){
        if(arr[i]>m){
        m=arr[i];
        }
}

for(int k=0;k<n;k++){
        arr[k]=arr[k]/m*100;
        sum+=arr[k];
        }
result=sum/n;
printf("%f",result);
return 0;
}