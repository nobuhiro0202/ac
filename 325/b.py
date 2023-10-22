N = int(input())
A = [list(map(int, input().split())) for _ in range(int(N))]
ans = 0

for i in range(23):
  sum = 0
  for e in A:
    if i >= 16:
        if i <= e[1] or i - e[1] >= 16: sum += e[0]
    else:
        if i <= e[1] and e[1] <= i + 8: sum += e[0]
  if ans <= sum: ans = sum


print(ans)