#include<iostream>
int gcd(int,int);
int lcm(int,int);

int main(){
    int A,B;
    std::cin>>A>>B;
    std::cout<<gcd(A, B)<<std::endl;
    std::cout<<lcm(A, B)<<std::endl;
    
    return 0;
}

// 최대공약수
int gcd(int a, int b) {
  while (b != 0) {
      int temp = b;
      b= a%b;
      a=temp;
  }
    return a;
}

// 최소공배수
int lcm(int a, int b){
    return a * b / gcd(a,b);
}
