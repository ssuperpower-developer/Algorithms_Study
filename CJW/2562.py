data = []
for i in range(9):
    data.append(int(input()))
print(max(data),data.index(max(data))+1,sep='\n')
