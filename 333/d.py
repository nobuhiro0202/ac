N = int(input())
u = [None] * (N - 1)
v = [None] * (N - 1)
g = [ [] for _ in  range(N + 1) ]
for i in range(N - 1): u[i], v[i] = map(int, input().split())
for i in range(N - 1):
    g[u[i]].append(v[i])
    g[v[i]].append(u[i])

ans = 1
def dfs(s):
    for i in g[s]: ans += dfs(i)
    return 