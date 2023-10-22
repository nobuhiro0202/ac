n = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
x = 0
y = 0
d = 0
grid = [ [0] * n for _ in range(n) ]

for i in range(1, n ** 2 + 1):
    grid[y][x] = i if i != n ** 2 else 'T'
    x += dx[d]
    y += dy[d]
    nx = x + dx[d]
    ny = y + dy[d]
    isOut = nx == -1 or nx == n or ny == -1 or ny == n
    if isOut or grid[ny][nx]: d = (d + 1) & 3

for i in range(n): print(*grid[i])