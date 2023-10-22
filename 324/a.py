N = int(input())
A = input().split()
a = A[0]

for i in range(1, N):
  if (a!=A[i]):
    print("No")
    break
else: 
  print("Yes")
