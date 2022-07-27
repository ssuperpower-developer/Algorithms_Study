N, M = map(int, input().split())
original = []
count = []
for i in range(N):
    original.append(input())
for i in range(N - 7):
    for j in range(M - 7):
        white_index = 0
        black_index = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (i + j) % 2 == 0:
                    if original[a][b] != 'W':
                        white_index += 1
                    if original[a][b] != 'B':
                        black_index += 1
                else:
                    if original[a][b] != 'B':
                        white_index += 1
                    if original[a][b] != 'W':
                        black_index += 1
        count.append(min(white_index, black_index))
print(min(count))
