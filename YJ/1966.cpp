#include<iostream>
#include<queue>
using namespace std;

int main(){
    int testcase,N, M,star,count;
    cin>>testcase;
    for(int i=0;i<testcase;i++){
        count=0;
        cin>>N>>M;
        queue<pair<int,int>>q;
        priority_queue<int>pq; //우선순위 큐

        for(int j=0;j<N;j++){
            cin>>star; 
            q.push({j,star}); //인덱스, 중요도
            pq.push(star); //중요도
        }

        while(!q.empty()){
            int curIndex=q.front().first; //인덱스
            int curStar=q.front().second; //중요도
            q.pop();
            if(pq.top()==curStar){ //우선순위 큐의 top이랑 현재 중요도가 같으면 출력하고 카운트 업
                pq.pop();
                count++;
                if(curIndex==M){ //원하던 프린트가 출력되면 현재 카운트 출력
                    cout<<count<<endl;
                    break;
                }
            }
            else q.push({curIndex,curStar});//중요도 낮으면 다시 넣기
        }
    }
}