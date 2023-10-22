n = int(input())
s = [input() for _ in range(n)]
bi = [0] * n
bj = [0] * n

for i in range(n):
    for j in range(n):
        if s[i][j] == 'o':
            bi[i] += 1
            bj[j] += 1

res = 0
for i in range(n):
    for j in range(n):
        if s[i][j] == 'o':
            res += (bi[i] - 1) * (bj[j] - 1)

print(res)
