A = []
S = []

[A.append(list(map(int, input().split()))) for i in range(6)]

[S.append(sum(A[i][j:j+3]+A[i+2][j:j+3])+A[i+1][j+1]) for i in range(4) for j in range(4)]

print(max(S))
