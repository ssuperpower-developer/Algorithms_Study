result = []
def o_factorial(N, T, L):
    o_fac = T
    for i in range(1, N + 1):
        o_fac *= i
        if(o_fac > L * 10 ** 8):
            result.append("TLE!")
            return
    result.append("May pass.")

for i in range(int(input())):
    S, N, T, L = input().split()
    N, T, L = int(N), int(T), int(L)
    if(S == "O(N)"):
        if(N * T <= L * 10 ** 8):
            result.append("May pass.")
        else:
            result.append("TLE!")
    elif(S == "O(N^2)"):
        if(N ** 2 * T <= L * 10 ** 8):
            result.append("May pass.")
        else:
            result.append("TLE!")
    elif(S == "O(N^3)"):
        if(N ** 3 * T <= L * 10 ** 8):
            result.append("May pass.")
        else:
            result.append("TLE!")
    elif(S == "O(2^N)"):
        if(2 ** N * T <= L * 10 ** 8):
            result.append("May pass.")
        else:
            result.append("TLE!")
    else:
        o_factorial(N, T, L)

for i in range(len(result)):
    print(result[i])

# def o_n(N, T, L):
#     if(N * T <= L * 10 ** 8):
#         result.append("May pass.")
#     else:
#         result.append("TLE!")

# def o_n_2(N, T, L):
#     if(N ** 2 * T <= L * 10 ** 8):
#         result.append("May pass.")
#     else:
#         result.append("TLE!")

# def o_n_3(N, T, L):
#     if(N ** 3 * T <= L * 10 ** 8):
#         result.append("May pass.")
#     else:
#         result.append("TLE!")

# def o_2_n(N, T, L):
#     if(2 ** N * T <= L * 10 ** 8):
#         result.append("May pass.")
#     else:
#         result.append("TLE!")

# def o_n_factorial(N, T, L):
#     if(factorial(N) * T <= L * 10 ** 8):
#         result.append("May pass.")
#     else:
#         result.append("TLE!")
