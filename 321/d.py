n, m, p = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

ans = 0

for i in range(n):
    k = 0
    while b[k] < p - a[i]: 
      k += 1
      if k == m: break
    f = k * a[i] + (m - k) * p
    for j in range(k): f += b[j]
    ans += f
        
print(ans)