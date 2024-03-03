import math
n = int(input())
A = list(map(int, input().split()));
S, T = [0] * (n - 1), [0] * (n - 1)
for i in range(n - 1): S[i], T[i] = map(int, input().split())

for i in range(n - 1):
  d = math.floor(A[i] // S[i])
  A[i + 1] += d * T[i]

print(A[n - 1])
