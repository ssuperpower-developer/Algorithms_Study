n = int(input())
score = list(map(int, input().split()))
newScore = [ i/max(score)*100 for i in score ]
print(sum(newScore)/len(newScore))