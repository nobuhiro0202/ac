import heapq

def calc(t, a, b, c):
  j = a >= b + c // t
  return t * a if j else t * b + c

n, a, b, c = map(int, input().split())
d = []
g = [ list() for _ in range(n) ]

for i in range(n): d.append(list(map(int, input().split())))
for i in range(n):
  for j in range(n):
    if i == j: continue
    g[i].append((j, d[i][j]))

dist = [ 10 ** 12 ] * n
dist[0] = 0
used = [ False ] * n
Q = list()
heapq.heappush(Q, (0, 0))

# ダイクストラ法：優先度付きキューの更新
while len(Q) >= 1:
	pos = heapq.heappop(Q)[0]
	if used[pos] == True: continue
	mx = 10 ** 12
	iiii = 0
	for i in g[pos]: 
		to = i[0]
		cost = dist[pos] + calc(i[1], a, b, c)
		if dist[to] > cost:
			dist[to] = cost
			if mx > dist[to]: 
				mx = dist[to]
				iiii = to
			heapq.heappush(Q, (to, dist[to]))

	used[iiii] = True

# print(heapq.heappop(Q)[1])