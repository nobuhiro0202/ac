dp = [[10**9] * 105 for _ in range(105)]

for i in range(105): dp[i][0] = 0

t = input()
tl = len(t)
n = int(input())

for i in range(n):
    for j in range(105): dp[i + 1][j] = dp[i][j]
    l = list(input().split())
    m = int(l.pop(0))
    for s in l:
        sl = len(s)
        for j in range(tl - sl + 1):
            if t[j:j+sl] == s: dp[i + 1][j + sl] = min(dp[i + 1][j + sl], dp[i][j] + 1)

if dp[n][tl] > 5 * 10**8: dp[n][tl] = -1

print(dp[n][tl])
