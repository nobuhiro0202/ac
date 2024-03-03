q = int(input())
a = []
for _ in range(q):
    t, n = map(int, input().split())
    if t == 1: a.insert(0, n)
    if t == 2: print(a[n - 1])