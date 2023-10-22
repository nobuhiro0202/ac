Vec = [
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0)
]

def is_ok(si, sj):
    if S[si][sj] == '#': return 0
    i, j = si, sj
    for t in T:
        di, dj = Vec[t]
        i, j = i + di, j + dj
        if not (0 <= i < H and 0 <= j < W): return 0
        if S[i][j] == '#': return 0
    return 1

H, W, N = map(int, input().split())
T = list(input())
for i in range(N): T[i] = "LRUD".find(T[i])
S = [input() for _ in range(H)]

ans = 0
for i in range(H):
    for j in range(W): ans += is_ok(i, j)
print(ans)
