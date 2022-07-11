#include<iostream>
#include<string>
using namespace::std;

int main(void){
    int result=0;
    string input;
    getline(cin,input);
    int startIndex;
    for(int i=0;i<(int)input.size();i++){
        if(input[i] != ' '){
            startIndex = i;
            break;
        }
    }
    for(int i=startIndex;i<(int)input.size()-1;i++){
        if(input[i]==' '){
            ++result;            
        }
    }
    ++result;
    if(input.size() == 1){
        if(input[0]==' ')   result = 0;
    }
    cout<<result<<endl;
    return 0;
}