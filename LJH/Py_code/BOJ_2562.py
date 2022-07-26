x = [ int(input()) for k in range(9)]
[print(j,i+1,sep = "\n") for i,j in enumerate(x) if j == max(x)]