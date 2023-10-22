n, k = map(int, input().split())
A = list(map(int, input().split()))
ans = []
for a in A:
  if a % k == 0: ans.append(a // k)
  
print(*ans)