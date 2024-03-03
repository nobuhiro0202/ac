n = int(input())
P = list(map(int, input().split()))
q = int(input())
A, B = [None] * q, [None] * q
for i in range(q): A[i], B[i] = map(int, input().split())

d = {}
for i in range(len(P)): d[P[i]] = i
for i in range(q):
  if d[A[i]] < d[B[i]]: print(A[i])
  if d[A[i]] > d[B[i]]: print(B[i])
