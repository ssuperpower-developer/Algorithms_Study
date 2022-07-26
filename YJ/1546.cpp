#include<iostream>
#include<cmath>
using namespace std;


int main(){
    int N;
    cin>>N;

    float scores[N];


    for(int i=0;i<N;i++){   
        cin>>scores[i];
    }

    float M=0;
    for(int i=0;i<N;i++){
        if(M<scores[i])   
            M=scores[i];
    }
    // cout<<M<<endl;
    
    float ch_scores[N];
    for(int i=0;i<N;i++){
        ch_scores[i]=(scores[i]/M*100);
        // cout<<ch_scores[i]<<" ";
    }
    float sum=0;
    for(int i=0;i<N;i++){
        sum=sum+ch_scores[i];
    }
    float aver;
    aver=sum/N;

    cout<<aver;
}

//점수/M*100
//50  100