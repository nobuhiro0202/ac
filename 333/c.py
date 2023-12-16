import heapq
N = int(input())
s = []
a = N + 1 if N < 13 else 13

for x in range(1, a):
    for y in range(x, a):
        for z in range(y, a): heapq.heappush(s, int(str(1) * x) + int(str(1) * y) + int(str(1) * z))

for _ in range(N - 1): heapq.heappop(s)
print(heapq.heappop(s))