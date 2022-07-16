# 내 풀이 : 
# (1) 리스트 함축으로 줄 줄이기
wordList = input().upper()
pureWordList = list(set(wordList))
cnt = []
[ cnt.append(wordList.count(i)) for i in pureWordList ]
[print("?") if cnt.count(max(cnt)) > 1 else print(pureWordList[cnt.index(max(cnt))])]

# 내 풀이:
# (2) 가독성 좋게 풀기
wordList = input().upper()
pureWordList = list(set(wordList))
cnt = []
for i in pureWordList:
    cnt.append(wordList.count(i))

if cnt.count(max(cnt)) > 1:
    print("?") 
    
else :
    print(pureWordList[cnt.index(max(cnt))])

# 다른 사람 풀이들:
# (1): 
# (2): 
# (3): 
# (4):