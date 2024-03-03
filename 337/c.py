n = int(input())
a = list(map(int, input().split()))
d = {}
for i in range(1, n + 1): d[a[i - 1]] = i

ans = [None] * n
ans[0] = d[-1]
for i in range(1, n): ans[i] = d[ans[i-1]]
print(*ans)