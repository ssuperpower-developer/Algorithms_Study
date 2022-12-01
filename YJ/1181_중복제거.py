#주어진 조건

#중복제거

#길이가 짧은 것부터
#길이가 같으면 사전 순으로

import sys
N=int(input())
wordList=[]

for i in range(N):
    wordList.append(input())

wordList=list(set(wordList))  #set 함수는 중복 제거를 해줌
wordList.sort() #파이썬은 알파벳 정렬도 됨!!
wordList.sort(key=len) #길이가 짧은 것부터

for i in wordList:
    print(i)