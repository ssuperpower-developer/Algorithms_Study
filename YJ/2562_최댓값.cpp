/*9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

예를 들어, 서로 다른 9개의 자연수

3, 29, 38, 12, 57, 74, 40, 85, 61

이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.*/


//첫째줄에 최댓값 입력 
//둘째줄에 몇번째 숫자인지


#include<iostream>
using namespace std;

int main(){
    int array[9];
    int max=0;
    int cnt=0;

    for(int i=0;i<9;i++){       
        cin>>array[i];
        if(array[i]>max){
            max=array[i];
            cnt=i+1;
            }
    }

    cout<<max<<endl;
    cout<<cnt<<endl;

}