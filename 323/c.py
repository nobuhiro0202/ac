from collections import deque

H, W = map(int, input().split())

s = []
d = [[0] * W for _ in range(H)]

for i in range(H):
    row = input()
    s.append(row)

def bfs(x, y):
  queue = deque([(x, y)])
  d[y][x] = 1

  while queue:
    x, y = queue.pop()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)]:
      nx, ny = x + dx, y + dy
      if 0 <= nx < W and 0 <= ny < H and s[ny][nx] == "#" and not d[ny][nx]:
        d[ny][nx] = 1
        queue.append((nx, ny))

sensor_count = 0

for i in range(H):
  for j in range(W):
    if s[i][j] == "#" and not d[i][j]:
      bfs(j, i)
      sensor_count += 1

print(sensor_count)
