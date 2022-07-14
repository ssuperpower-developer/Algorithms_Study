#include<iostream>
#include<string>
#include <stdint.h> 
using namespace::std;

class testCase{
private:
    string S;
    int N;
    int T;
    int L;
    int spec;
    int resultForSingleSecond; 
    unsigned long int resultOfDetectMaxInput;
    unsigned long int maxInputable;
public:
    testCase(){}
    void Initialization(string S,int N,int T,int L){
        this->S = S;
        this->N = N;
        this->T = T;
        this->L = L;
        spec = 0;
        this->resultForSingleSecond = 100000000;
        this->resultOfDetectMaxInput = 1;
        maxInputable = L*resultForSingleSecond;
    }
    void detectMaxInput();
    void detectTimeResult();
};


void testCase::detectMaxInput(){
    if(S == "O(N)"){
        this->resultOfDetectMaxInput = N*T;
        if(resultOfDetectMaxInput == 0){
            this->spec = 1;
        }
        // cout<<"O(N)"<<endl;    
    }
    else if(S == "O(N^2)"){
        this->resultOfDetectMaxInput = N*N*T;
        if(resultOfDetectMaxInput == 0){
            this->spec = 1;
        }  
        // cout<<"O(N^2)"<<endl; 
    } 
    else if(S == "O(N^3)" ) {
        this->resultOfDetectMaxInput = N*N*N*T;
        if(resultOfDetectMaxInput == 0){
            this->spec = 1;
        }
        // cout<<"O(N^3)"<<endl;  
    }
    else if(S == "O(2^N)"){
        int temp=1;
        for(int i=0;i<N;i++){
            temp = temp *2;
            if(temp>maxInputable){
                this->spec = 1;
            }
        }
        this->resultOfDetectMaxInput = temp;
        this->resultOfDetectMaxInput *= T;
        if(resultOfDetectMaxInput > maxInputable){
            this->spec = 1;
        }
        if(resultOfDetectMaxInput == 0){
            this->spec = 1;
        }
        // cout<<"O(2^N)"<<endl;  
    }
    else if(S == "O(N!)"){
        while(this->N > 0){
            this->resultOfDetectMaxInput *= this->N;
            --N;
        }
        this->resultOfDetectMaxInput *= T;
        if(resultOfDetectMaxInput == 0){
            this->spec = 1;
        }
        // cout<<"O(N!)"<<endl;  
    }
    // for check
    // cout<<resultOfDetectMaxInput<<endl;
}
void testCase::detectTimeResult(){
    if(spec == 1){
        cout<<"TLE!"<<endl;
        return;
    }
    if(maxInputable>=resultOfDetectMaxInput){
        cout<<"May Pass."<<endl;
        return;
    }
    else if(maxInputable<resultOfDetectMaxInput){
        cout<<"TLE!"<<endl;
        return;
    }
}

int main(void){
    int C;
    cin>>C;
    testCase *arr = new testCase[C];
    string tempString;
    int tempN;
    int tempT;
    int tempL;
    for(int i=0;i<C;i++){
        cin>>tempString;
        cin>>tempN;
        cin>>tempT;
        cin>>tempL;
        arr[i].Initialization(tempString,tempN,tempT,tempL);
    }
    // for check
    // for(int i=0;i<C;i++){
    //     cout<<arr[i].S<<endl;
    // }

    for(int i=0;i<C;i++){
        arr[i].detectMaxInput();
    }
    for(int i=0;i<C;i++){
        arr[i].detectTimeResult();
    }
    return 0;
}