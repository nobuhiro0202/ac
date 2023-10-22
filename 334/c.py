n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = [2] * n
for i in range(k): cnt[a[i] - 1] -= 1

x = []
for i in range(n):
    for j in range(cnt[i]): x.append(i)

ans = 0
n = len(x)
if n % 2 == 0:
    for i in range(n // 2): ans += x[i * 2 + 1] - x[i * 2]
else:
    now = 0
    for i in range(n // 2): now += x[i * 2 + 2] - x[i * 2 + 1]
    ans = now
    for i in range(2, n, 2):
        now += x[i - 1] - x[i - 2]
        now -= x[i] - x[i - 1]
        ans = min(ans, now)
print(ans)