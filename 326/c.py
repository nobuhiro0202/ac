n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
a.append(9000000000000)
res = 0
r = 0
for l in range(n):
    while a[r] < a[l]+m:
        r += 1
    res = max(res,r-l)
print(res)