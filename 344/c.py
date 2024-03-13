n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
l = int(input())
C = list(map(int, input().split()))
q = int(input())
X = list(map(int, input().split()))

D = []

for a in A:
  for b in B:
    for c in C: D.append(a + b + c)

D = set(D)

for x in X:  
  if x in D: print("Yes")
  else: print("No")
    