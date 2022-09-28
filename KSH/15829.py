import sys
L = int(sys.stdin.readline())
alphabet = sys.stdin.readline().rstrip()
alphabet = [(ord(alphabet[i]) % 96) * (31 ** i) for i in range(L)]
print(sum(alphabet) % 1234567891)